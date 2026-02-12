import random

print("Fake News Detection System")

news = input("Enter a news headline: ")

# Simple logic (demo purpose)
if "government" in news.lower() or "official" in news.lower():
    print("This news is likely Real")
else:
    print("This news might be Fake")
