"""Chatbot2.

Chatbot1にユーザー入力と履歴を組み合わせた例
https://www.gradio.app/guides/creating-a-chatbot-fast
"""

import gradio as gr


def alternatingly_agree(message, history):
    """同意と反対を交互に繰り返す."""
    if len([h for h in history if h["role"] == "assistant"]) % 2 == 0:
        return f"Yes, I do think that: {message}"
    else:
        return "I don't think so"


gr.ChatInterface(fn=alternatingly_agree, type="messages").launch()
