import random


def get_difficulty():
    """Prompt user to select a difficulty level."""
    print("\nChoose difficulty:")
    print("  1. Easy   (1 – 50,   10 attempts)")
    print("  2. Medium (1 – 100,   7 attempts)")
    print("  3. Hard   (1 – 200,   5 attempts)")

    settings = {"1": (50, 10), "2": (100, 7), "3": (200, 5)}
    while True:
        choice = input("\nEnter choice (1 / 2 / 3): ").strip()
        if choice in settings:
            return settings[choice]
        print("  ⚠  Invalid choice. Please enter 1, 2, or 3.")


def get_hint(guess, secret):
    """Return a directional hint based on how far off the guess is."""
    diff = abs(guess - secret)
    if guess < secret:
        return "Much higher 🔥" if diff > 20 else "A little higher ↑"
    return "Much lower ❄️" if diff > 20 else "A little lower ↓"


def play_round():
    """Run a single round of the game. Returns the number of attempts used."""
    max_num, max_attempts = get_difficulty()
    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\n  I've picked a number between 1 and {max_num}.")
    print(f"  You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"  Attempt {attempts + 1}/{max_attempts} → Your guess: "))
        except ValueError:
            print("  ⚠  Please enter a whole number.\n")
            continue

        if not (1 <= guess <= max_num):
            print(f"  ⚠  Please enter a number between 1 and {max_num}.\n")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n  🎉 Correct! The number was {secret}.")
            print(f"  You guessed it in {attempts} attempt(s)!\n")
            return attempts

        hint = get_hint(guess, secret)
        print(f"  ✗  Wrong!  {hint}\n")

    print(f"\n  💀 Out of attempts! The number was {secret}.\n")
    return None  # None signals the player did not win


def show_scoreboard(history):
    """Print a summary of all rounds played."""
    print("\n" + "=" * 42)
    print("  📊  SCOREBOARD")
    print("=" * 42)
    wins = [a for a in history if a is not None]
    losses = len(history) - len(wins)
    print(f"  Rounds played : {len(history)}")
    print(f"  Wins          : {len(wins)}")
    print(f"  Losses        : {losses}")
    if wins:
        print(f"  Best round    : {min(wins)} attempt(s)")
        print(f"  Avg attempts  : {sum(wins) / len(wins):.1f}")
    print("=" * 42)


def main():
    print("=" * 42)
    print("       🎯  NUMBER GUESSING GAME")
    print("=" * 42)

    history = []

    while True:
        result = play_round()
        history.append(result)

        again = input("  Play again? (y / n): ").strip().lower()
        if again != "y":
            break

    show_scoreboard(history)
    print("\n  Thanks for playing! Goodbye 👋\n")


if __name__ == "__main__":
    main()
    