"""入力の追加.

https://www.gradio.app/guides/creating-a-chatbot-fast
"""

import time

import gradio as gr


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.05)
        yield response[: i + 1]


demo = gr.ChatInterface(
    echo,
    type="messages",
    additional_inputs=[
        gr.Textbox("You are helpful AI.", label="System Prompt"),
        gr.Slider(10, 100),
    ],
)

demo.launch()
