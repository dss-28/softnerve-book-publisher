def ai_writer(text):
    """Mock AI Writer (replace with Gemini API call)"""
    return f"[AI-WRITTEN VERSION]\n{text[:200]}..."

def ai_reviewer(text):
    """Mock AI Reviewer (simulate improvements)"""
    return text.replace("[AI-WRITTEN VERSION]", "[AI-REVIEWED VERSION]").replace("...", "\n[Reviewed for clarity, grammar, and flow]")

if __name__ == "__main__":
    with open("output/chapter.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    written = ai_writer(raw_text)
    reviewed = ai_reviewer(written)
    with open("output/final_draft.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)