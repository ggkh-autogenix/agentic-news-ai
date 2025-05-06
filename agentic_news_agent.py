from langchain.chat_models import ChatOpenAI
from langchain.tools import tool
from langgraph.graph import StateGraph, END
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
import requests

@tool
def search_news(topic: str) -> str:
    """Search real-time news for a topic."""
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={topic}&apiKey=YOUR_NEWSAPI_KEY"
    )
    articles = response.json().get("articles", [])[:3]
    return "\n".join([f"- {a['title']}" for a in articles])

@tool
def summarize(text: str) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    return llm.predict("Summarize this: " + text)

embedding = OpenAIEmbeddings()
memory = ConversationBufferMemory(memory_key="chat_history")

class AgentState(dict):
    topic: str
    news: str
    summary: str
    chat_history: str

def plan_node(state):
    return {"topic": state["topic"]}

def search_node(state):
    news = search_news(state["topic"])
    return {"news": news}

def summarize_node(state):
    summary = summarize(state["news"])
    return {"summary": summary}

def memory_node(state):
    memory.save_context({"input": state["topic"]}, {"output": state["summary"]})
    return {"chat_history": memory.buffer}

workflow = StateGraph(AgentState)
workflow.add_node("plan", plan_node)
workflow.add_node("search", search_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("memory", memory_node)
workflow.set_entry_point("plan")
workflow.add_edge("plan", "search")
workflow.add_edge("search", "summarize")
workflow.add_edge("summarize", "memory")
workflow.add_edge("memory", END)

graph = workflow.compile()

def run_agentic_news(topic):
    result = graph.invoke({"topic": topic})
    return result["summary"]