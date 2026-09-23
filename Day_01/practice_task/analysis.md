# Comparing a Chatbot, a Rule-Based Workflow, and an AI Agent
## Scenario: Library Book Fine Calculator

## 1. The Scenario

A college library tracks overdue books with a fine of Rs. 5 per day overdue, capped at
Rs. 100 per book. This is private data — no public LLM has ever seen it:

| Book Code | Title | Days Overdue | Fine |
|---|---|---|---|
| B101 | Introduction to AI | 5 | Rs. 25 |
| B202 | Data Structures | 0 | Rs. 0 |
| B303 | Python Programming | 12 | Rs. 60 |

Four questions were asked of all three systems:
1. What is the fine for book B303?
2. What is the total fine for B101 and B303 after a 10% student discount?
3. Is B303's fine more than B101's, and by how much?
4. Write a two-line reminder message for students returning books late.

## 2. Explanation of Each Approach

### 2.1 Plain Chatbot
<!-- Describe in your own words: does it use an LLM alone? Does it have access to the
real fine data? What happened when you ran it — did it guess fake numbers? Quote or
paraphrase what it actually said for Q1-Q3, and explain WHY it got them wrong (hint:
it has never seen your BOOK_RECORDS dictionary — it can only pattern-match from its
training data). What happened on Q4, and why did that one go fine? -->

(Write 1-2 paragraphs here.)

### 2.2 Rule-Based Workflow
<!-- Describe: no LLM at all, just Python if/else and regex rules. What happened on
Q1 and Q2 — were they instant and exact? Why? What happened on Q3 and Q4, and why
specifically — was it a MISSING rule, not a wrong one? What does this show about
rule-based systems being "reliable but rigid"? -->

(Write 1-2 paragraphs here.)

### 2.3 AI Agent
<!-- Describe: LLM + Tools + Loop. Walk through what actually happened when you ran
agent.py — for Q2, how many steps did it take, which tools did it call, in what order?
Did it correctly compute Rs. 76.50? Did anything go wrong along the way (you saw a
tool-calling error with gpt-oss-20b) — what caused it, and how did switching models
fix it? What does that failure teach you about agent reliability? Did it correctly
skip tool use for Q4? -->

(Write 1-2 paragraphs here.)

## 3. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | | | |
| Decision-making | | | |
| Tool usage | | | |
| Private-data access | | | |
| Multi-step task handling | | | |
| Automation | | | |
| Reliability | | | |

<!-- Fill each cell with a short phrase based on what you actually observed, e.g.
"None — hallucinates" / "None — fixed rules only" / "Chooses tools dynamically" -->

## 4. Suitability Analysis

<!-- Which of the three would you actually deploy for a real library's fine system,
and why? Use specific points from your table above — e.g. if reliability matters most
for a finance-adjacent task, that favors one approach; if the library later wants to
handle open-ended questions ("can I return this book at another branch?"), that favors
a different one. -->

(Write 1-2 paragraphs here.)

## 5. Conclusion

<!-- Zoom out beyond just book fines. In general, when would a plain chatbot make
sense? When does a rule-based workflow make sense? When does an AI agent make sense?
Think about factors like: how predictable the possible questions are, how much the
cost of a wrong answer matters, whether the task needs multiple steps or external
data, and whether new/unseen question types need to be handled. -->

(Write 1-2 paragraphs here.)