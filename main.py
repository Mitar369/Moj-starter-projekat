import os
import sys

def review_code(code_text):
    print("--- [1/3] Pokrećem AI pregled koda... ---")
    return "AI Analiza: Kod je stabilan."

def generate_readme(project_summary):
    print("--- [2/3] Generišem dokumentaciju... ---")
    return f"# Proizvod Automatski Generisan\n\n## Opis\n{project_summary}"

def fix_issue(issue_description):
    print(f"--- [3/3] Analiziram Issue: '{issue_description}'... ---")
    return f"Predlog rešenja za '{issue_description}': Proveriti funkciju."

if __name__ == "__main__":
    print("=== AUTOMATED OPEN SOURCE DEVELOPER BOT ===")
    print(review_code("def add(a, b): return a + b"))
    print(generate_readme("Ovo je automatski generisan projekat."))
    print(fix_issue("Dugme za login ne reaguje"))
