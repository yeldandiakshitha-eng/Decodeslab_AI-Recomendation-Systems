# AI Recommendation System (Improved Version)

print("========== AI RECOMMENDATION SYSTEM ==========")

while True:

    # Store recommendations
    recommendations = {
        "movies": [
            "Interstellar",
            "Avatar",
            "Inception"
        ],

        "music": [
            "Pop Songs",
            "Lofi Music",
            "Classical Music"
        ],

        "books": [
            "Atomic Habits",
            "Rich Dad Poor Dad",
            "Ikigai"
        ],

        "games": [
            "Minecraft",
            "Chess",
            "Subway Surfers"
        ]
    }

    print("\nAvailable Categories:")
    print("Movies")
    print("Music")
    print("Books")
    print("Games")

    interest = input(
        "\nEnter your interest: "
    ).lower()

    # Recommendation Logic
    if interest in recommendations:

        print("\nRecommended for you:")

        for item in recommendations[interest]:
            print("→", item)

    else:
        print("\nInvalid choice!")

    again = input(
        "\nDo you want recommendations again? (yes/no): "
    ).lower()

    if again != "yes":
        print("\nThank you for using AI Recommendation System")
        break