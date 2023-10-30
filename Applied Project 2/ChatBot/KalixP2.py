import openai

openai.api_key = "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"

messages = []
system_msg = input("What would you like to order?\n")
messages.append({"role": "system", "content": system_msg})

print("Thabj you for placing the order with Kalix Wholesalers !")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")