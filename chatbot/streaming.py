"""ストリーミングの例.

https://www.gradio.app/guides/creating-a-chatbot-fast
"""

import time

import gradio as gr


def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i + 1]


gr.ChatInterface(fn=slow_echo, type="messages").launch()
