import gradio as gr


def great(name, intensity):
    return f"Hello, {name}! {int(intensity)}"


demo = gr.Interface(
    fn=great,
    inputs=["text", gr.Slider(value=1, minimum=1, maximum=10, step=1)],
    outputs=gr.Textbox(label="挨拶", lines=3),
)

demo.launch()
