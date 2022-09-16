"""
A script showing how to load the dataset and generate a predictions file compatible with the scorer.
"""

import sys
import json
import random


def load_instances(fn):

    instances = []
    with open(fn) as f:
        for jl_str in f:
            instances.append(json.loads(jl_str))
    
    return instances


if __name__ == '__main__':

    data_fn = sys.argv[1] 
    pred_fn = sys.argv[2]

    instances = load_instances(data_fn)

    # generate predictions
    predictions = {}
    for inst in instances:
        pred = random.choice([0, 1])
        predictions[inst['id']] = pred


    # output predictions
    with open(pred_fn, 'w') as preds_f:
        for inst_id, pred in predictions.items():
            preds_f.write(f"{inst_id}\t{pred}\n")

