import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You're a stock manager which manage stocks and gaining orders"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Kalix ChatBot")

demo.launch(share=True)