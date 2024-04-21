import gradio as gr
import pandas as pd
from prohibition_of_changes import Prohibition

df1 = pd.read_csv('test.csv', sep=';')
df = pd.DataFrame({'col1': ['row1', 'row2'], 'col2': ['', ''], 'col3': ['', '']})

proh = Prohibition(dataFrame=df1, column='col1')

with gr.Blocks() as testTask:
    with gr.Row():
        low_percent_frame = gr.DataFrame(
            value=proh.dFrame(flag='frame'),
            label="Записи для перепроверки",
            interactive=True,
            col_count=(len(proh.dFrame(flag='columns')), 'fixed'),
        )
    low_percent_frame.input(proh.check, [low_percent_frame], [low_percent_frame])

testTask.launch()
