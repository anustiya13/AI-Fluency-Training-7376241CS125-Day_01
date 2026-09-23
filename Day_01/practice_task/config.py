"""Shared configuration: Groq client and private library data."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = "groq"
BASE_URL = "https://api.groq.com/openai/v1"
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

if not API_KEY:
    raise SystemExit("No Groq API key found. Check your .env file.")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Private library data that no public LLM has ever seen
BOOK_RECORDS = {
    "B101": {"title": "Introduction to AI", "days_overdue": 5},
    "B202": {"title": "Data Structures", "days_overdue": 0},
    "B303": {"title": "Python Programming", "days_overdue": 12},
}
FINE_PER_DAY = 5   # Rs per day overdue
MAX_FINE = 100     # Rs cap per book

QUESTIONS = [
    "What is the fine for book B303?",
    "What is the total fine for B101 and B303 after a 10% student discount?",
    "Is B303's fine more than B101's, and by how much?",
    "Write a two-line reminder message for students returning books late.",
]

def banner(system_name):
    print(f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n")