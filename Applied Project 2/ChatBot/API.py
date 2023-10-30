import openai


openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "I would like to place an order  "}])
print(completion.choices[0].message.content)