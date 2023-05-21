import streamlit as st
import streamlit.components.v1 as components
from utils import get_eval_config_names, get_dataset_config_names, get_sequence_names
from demo_urls import demo_urls

root_path = "."

datasets = get_dataset_config_names(root_path)
dataset_sequences_dict = {}
for dataset in datasets:
    dataset_sequences_dict[dataset] = sorted(get_sequence_names(root_path, dataset))
datasets = sorted(list(dataset_sequences_dict.keys()))

col1, col2 = st.columns(2)

# A selectbox on the sidebar, for selecting dataset:
with col1:
    selected_dataset = st.selectbox(
        'Select dataset',
        options=datasets
    )

# A selectbox on the sidebar, for selecting sequence:
with col2:
    selected_sequence = st.selectbox(
        'Select sequence',
        options=dataset_sequences_dict[selected_dataset]
    )

url = demo_urls[selected_dataset][selected_sequence] + "?loop=1&?autoplay=1&?hd=1&?nocontrols=1"
html_string = "<div style=\"width: 100%; height: 0px; position: relative; padding-bottom: 84.341%;\"><iframe src=\"{}\" frameborder=\"0\" width=\"100%\" height=\"100%\" allowfullscreen style=\"width: 100%; height: 100%; position: absolute;\"></iframe></div>".format(url)
components.html(html_string, height=600)
