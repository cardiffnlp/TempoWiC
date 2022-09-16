"""
Outputs instance data stored as .jl in a more readable format. For easier inspection.
"""

import sys
import json


def load_instances(fn):

    instances = []
    with open(fn) as f:
        for jl_str in f:
            instances.append(json.loads(jl_str))
    
    return instances


if __name__ == '__main__':

    data_fn = sys.argv[1]
    assert data_fn.endswith('.jl')

    instances = load_instances(data_fn)

    for inst_idx, inst in enumerate(instances):

        print(f"#{inst_idx+1}/{len(instances)} Instance ID: {inst['id']}")
        print()
        print(inst['tweet1']['date'])
        print(inst['tweet1']['text'])
        print()
        print(inst['tweet2']['date'])
        print(inst['tweet2']['text'])
        print()
        input('--- Press Enter for next instance ---')
        print()
