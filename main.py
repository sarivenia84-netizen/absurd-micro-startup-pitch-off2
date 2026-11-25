import os

PITCH = "Coffee-fetching simulator: an agent that moves a cursor every 30 minutes to prevent sleep timeout, billing itself as 'keeping the connection alive' for $5/mo per agent."

def main():
    os.makedirs("/output", exist_ok=True)
    text = PITCH.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"Pitch length {len(text)} not in 1-200")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()