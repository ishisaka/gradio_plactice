"""Chatobot1.

Chatobotインターフェイスの基本的な例。
参考: https://www.gradio.app/guides/creating-a-chatbot-fast
"""

import random

import gradio as gr


def random_response(message, history):
    return random.choice(["yes", "No"])


gr.ChatInterface(
    fn=random_response,
    type="messages",
).launch()
