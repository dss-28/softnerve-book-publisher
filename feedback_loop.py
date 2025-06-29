def human_feedback_loop(draft_path="output/final_draft.txt"):
    with open(draft_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n===== CURRENT VERSION =====\n")

    try:
        print(content[:500])  # Safe print for UTF-8 terminals
    except UnicodeEncodeError:
        print(content[:500].encode('ascii', errors='ignore').decode())

    decision = input("\nApprove (a), Edit (e), Reject (r): ").strip().lower()

    if decision == "e":
        print("\nEnter your edits below (end with '###'):")
        lines = []
        while True:
            line = input()
            if line.strip() == "###":
                break
            lines.append(line)
        with open(draft_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    elif decision == "r":
        print("\n❌ Rejected. Restart the flow.")
    else:
        print("\n✅ Approved. Final version ready.")

if __name__ == "__main__":
    human_feedback_loop()
