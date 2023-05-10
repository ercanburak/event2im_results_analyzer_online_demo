import streamlit as st
from streamlit_player import st_player
from utils import get_eval_config_names, get_dataset_config_names, get_sequence_names
from demo_urls import demo_urls

root_path = "."

# eval_configs = get_eval_config_names(root_path)
datasets = get_dataset_config_names(root_path)
dataset_sequences_dict = {}
for dataset in datasets:
    dataset_sequences_dict[dataset] = get_sequence_names(root_path, dataset)
datasets = list(dataset_sequences_dict.keys())

# st.sidebar.title("Event2Im Results Analyzer - Online Demo")


# A selectbox on the sidebar, for selecting eval config:
# selected_eval_config = st.sidebar.selectbox(
#     'Select eval config',
#     options=eval_configs
# )

col1, col2, col3 = st.columns(3)

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
# with col3:
#     st.text("")
#     st.text("")
#     if not st.button('Run'):
#         st.stop()

url = demo_urls[selected_dataset][selected_sequence]
st_player(url)
