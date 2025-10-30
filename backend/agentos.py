from dotenv import load_dotenv; load_dotenv()
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="chat.db")

bot = Agent(
    name="chat",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    db=db,
)

os = AgentOS(agents=[bot])
app = os.get_app()
