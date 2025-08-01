def respond(message):
    message = message.lower()

    if "destiny 2 story" in message:
        return (
            "*Destiny 2* is an online multiplayer shooter developed by Bungie.\n\n"
            "The story begins after the events of *Destiny 1*, when the Last City is attacked by the Red Legion, "
            "led by Dominus Ghaul. Guardians lose their connection to the Light — the source of their power — and must regain it to fight back and defeat Ghaul.\n\n"
            "Throughout the expansions, players face threats like Savathûn, the Vex, the Darkness, and many others. "
            "The narrative deepens with ongoing conflict between Light and Darkness, the discovery of ancient powers, "
            "the fall of allies, and the rise of new enemies.\n\n"
            "Would you like to hear about a specific expansion like *Forsaken*, *Shadowkeep*, or *The Final Shape*?"
        )

    elif "bye" in message or "exit" in message:
        return "👋 See you later, Guardian!"

    else:
        return "I didn't quite catch that. Try asking me: 'What is the Destiny 2 story?'"

print("🤖 Ask me about Destiny 2. (Type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: 👋 See you next time!")
        break

    response = respond(user_input)
    print("Bot:", response)
