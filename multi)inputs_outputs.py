import gradio as gr


def great(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation}, {name}. It is {temperature} degrees today."
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=great, inputs=["text", "checkbox", gr.Slider(0, 100)], outputs=["text", "number"]
)
demo.launch()
