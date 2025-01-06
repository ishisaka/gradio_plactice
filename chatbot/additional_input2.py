"""入力の追加、ブロックを使用した方法.

https://www.gradio.app/guides/creating-a-chatbot-fast
"""

import time

import gradio as gr


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.05)
        yield response[: i + 1]


with gr.Blocks() as demo:
    system_prompt = gr.Textbox("You are helpful AI.", label="System Prompt")
    slider = gr.Slider(10, 100, render=False)

    gr.ChatInterface(echo, additional_inputs=[system_prompt, slider], type="messages")

demo.launch()
