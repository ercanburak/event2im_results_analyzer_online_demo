import os
import glob
import json
from pathlib import Path
from collections import OrderedDict


def read_json(fname):
    fname = Path(fname)
    with fname.open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)


def get_filenames(base_path, filename_pattern):
    file_names = []
    glob_pattern = os.path.join(base_path, filename_pattern)
    file_paths = glob.glob(glob_pattern)
    for file_path in file_paths:
        file_name = Path(file_path).stem
        file_names.append(file_name)
    return file_names


def get_eval_config_names(ecnn_path):
    eval_configs_path = os.path.join(ecnn_path, "config")
    eval_configs_filename_pattern = "eval*.json"
    return get_filenames(eval_configs_path, eval_configs_filename_pattern)


def get_dataset_config_names(ecnn_path):
    data_configs_path = os.path.join(ecnn_path, "data")
    data_configs_filename_pattern = "*.json"
    return get_filenames(data_configs_path, data_configs_filename_pattern)


def get_sequence_names(ecnn_path, dataset_name):
    sequences = []
    data_configs_path = os.path.join(ecnn_path, "data")
    dataset_file_name = os.path.join(data_configs_path, dataset_name + ".json")
    dataset_config = read_json(dataset_file_name)
    for sequence in dataset_config['sequences']:
        sequences.append(sequence)
    return sequences