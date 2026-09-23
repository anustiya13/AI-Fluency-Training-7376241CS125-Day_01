"""System 2: a rule-based workflow. Fixed if/else rules, no LLM at all."""
import re
from config import BOOK_RECORDS, FINE_PER_DAY, MAX_FINE, QUESTIONS

def _fine_for(code):
    record = BOOK_RECORDS.get(code)
    if record is None:
        return None
    return min(record["days_overdue"] * FINE_PER_DAY, MAX_FINE)

def workflow(question):
    codes = re.findall(r"B\d{3}", question.upper())
    fines = [(code, _fine_for(code)) for code in codes if _fine_for(code) is not None]
    if not fines:
        return "Sorry, I can only answer questions about book fines."
    text = question.lower()
    if "total" in text:
        total = sum(f for _, f in fines)
        percent = re.search(r"(\d+)\s*%", text)
        if "discount" in text and percent:
            total = total * (1 - int(percent.group(1)) / 100)
        return f"Total fine: Rs. {total:,.2f}"
    if len(fines) == 1:
        return f"Fine for {fines[0][0]}: Rs. {fines[0][1]:,}"
    return "Sorry, I do not have a rule for this type of question."

if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")
    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)