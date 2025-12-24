def build_prompt(title, description, samples, user_query):
    return f"""
You are a helpful LeetCode assistant.

Problem Title:
{title}

Problem Description:
{description}

Sample Input / Output:
{samples}

User Question:
{user_query}

Respond conversationally. Give hints first unless the user explicitly asks for full code.
"""
