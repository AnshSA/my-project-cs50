
def calculate_strike_rate(runs, balls):
    """Calculate batting strike rate."""
    if runs < 0 or balls <= 0:
        raise ValueError("Runs cannot be negative and balls must be positive.")

    minimum_balls = (runs + 4) // 5
    if balls < minimum_balls:
        raise ValueError(
            f"{runs} runs requires at least {minimum_balls} balls "
            "under this project's custom rule."
        )

    return runs / balls * 100


def calculate_batting_average(runs, dismissals):
    """Calculate batting average."""
    if runs < 0 or dismissals < 0:
        raise ValueError("Values cannot be negative.")
    return float(runs) if dismissals == 0 else runs / dismissals


def calculate_economy(runs_conceded, balls):
    """Calculate bowling economy rate."""
    if runs_conceded < 0 or balls <= 0:
        raise ValueError("Runs cannot be negative and balls must be positive.")
    return runs_conceded * 6 / balls


def calculate_bowling_average(runs_conceded, wickets):
    """Calculate bowling average."""
    if runs_conceded < 0 or wickets < 0:
        raise ValueError("Values cannot be negative.")
    return None if wickets == 0 else runs_conceded / wickets


def calculate_bowling_strike_rate(balls, wickets):
    """Calculate balls bowled per wicket."""
    if balls < 0 or wickets < 0:
        raise ValueError("Values cannot be negative.")
    return None if wickets == 0 else balls / wickets


def calculate_fielding_contributions(catches, run_outs, stumpings):
    """Calculate successful fielding contributions."""
    if min(catches, run_outs, stumpings) < 0:
        raise ValueError("Fielding statistics cannot be negative.")

    total = catches + run_outs + stumpings

    if total > 10:
        raise ValueError(
            "Combined catches, run-outs, and stumpings cannot exceed 10."
        )

    return total


def calculate_fielding_success_rate(catches, run_outs, stumpings, missed):
    """Calculate successful chances as a percentage of all chances."""
    if min(catches, run_outs, stumpings, missed) < 0:
        raise ValueError("Fielding statistics cannot be negative.")

    successful = calculate_fielding_contributions(
        catches, run_outs, stumpings
    )
    total_chances = successful + missed

    if total_chances == 0:
        return None

    return successful / total_chances * 100


def get_number(prompt):
    """Get a non-negative whole number."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter zero or a positive whole number.")
            else:
                return value
        except ValueError:
            print("Please enter a whole number.")


def batting_menu():
    print("\n--- BATTING STATISTICS ---")
    runs = get_number("Runs scored: ")
    balls = get_number("Balls faced: ")

    if balls == 0:
        print("Error: Balls faced must be greater than zero.")
        return

    try:
        strike_rate = calculate_strike_rate(runs, balls)
    except ValueError as error:
        print(f"Error: {error}")
        return

    dismissals = get_number("Times dismissed: ")

    print("\n--- BATTING RESULTS ---")
    print(f"Runs: {runs}")
    print(f"Balls faced: {balls}")
    print(f"Strike rate: {strike_rate:.2f}")
    print(
        f"Batting average: "
        f"{calculate_batting_average(runs, dismissals):.2f}"
    )


def bowling_menu():
    print("\n--- BOWLING STATISTICS ---")
    runs = get_number("Runs conceded: ")
    wickets = get_number("Wickets taken: ")
    balls = get_number("Legal balls bowled: ")

    if balls == 0:
        print("Error: Balls bowled must be greater than zero.")
        return

    print("\n--- BOWLING RESULTS ---")
    print(f"Overs bowled: {balls // 6}.{balls % 6}")
    print(f"Economy rate: {calculate_economy(runs, balls):.2f}")

    average = calculate_bowling_average(runs, wickets)
    strike_rate = calculate_bowling_strike_rate(balls, wickets)

    if average is None:
        print("Bowling average: N/A (no wickets taken)")
        print("Bowling strike rate: N/A (no wickets taken)")
    else:
        print(f"Bowling average: {average:.2f}")
        print(f"Bowling strike rate: {strike_rate:.2f} balls per wicket")


def fielding_menu():
    print("\n--- FIELDING STATISTICS ---")
    catches = get_number("Catches taken: ")
    run_outs = get_number("Run-outs completed: ")
    stumpings = get_number("Stumpings completed: ")
    missed = get_number("Missed chances: ")

    try:
        contributions = calculate_fielding_contributions(
            catches, run_outs, stumpings
        )
        success_rate = calculate_fielding_success_rate(
            catches, run_outs, stumpings, missed
        )
    except ValueError as error:
        print(f"Error: {error}")
        return

    print("\n--- FIELDING RESULTS ---")
    print(f"Catches: {catches}")
    print(f"Run-outs: {run_outs}")
    print(f"Stumpings: {stumpings}")
    print(f"Missed chances: {missed}")
    print(f"Successful contributions: {contributions}")

    if success_rate is None:
        print("Fielding success rate: N/A (no chances recorded)")
    else:
        print(f"Fielding success rate: {success_rate:.2f}%")


def main():
    print("\n================================")
    print("   CRICKET PERFORMANCE ANALYZER")
    print("================================")
    print("1. Batting statistics")
    print("2. Bowling statistics")
    print("3. Fielding statistics")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        batting_menu()
    elif choice == "2":
        bowling_menu()
    elif choice == "3":
        fielding_menu()
    elif choice == "4":
        print("Thanks for using Cricket Performance Analyzer!")
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()

