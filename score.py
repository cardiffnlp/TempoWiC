"""
A simple python script to generate official scores for the task. Reports accuracy and macro-f1.
Requires a single id / label tab-separated prediction per line.
Use label 0 for False and 1 for True.

This script should be compatible with Python 2.7+
"""

import sys


def f1_macro(gold, preds, debug=False):
    # unweighted, penalizes recall for missing instances
    
    def f1(gold, preds, label):

        tp, fp, fn, tn, unknown = 0.0, 0.0, 0.0, 0.0, 0.0
        for idx in range(len(gold)):
            if (preds[idx]==-1):
                unknown+=1
            elif (gold[idx] == label) and (preds[idx] == label):
                tp += 1
            elif (preds[idx] != label) and (gold[idx] == label):
                fn += 1
            elif (gold[idx] != label) and (preds[idx] == label):
                fp += 1
            elif (gold[idx] != label) and (preds[idx] != label):
                tn += 1
        try:
            precision = tp/(tp+fp)
            
            recall = tp/(tp+fn+unknown)

            f1 = 2 * (precision * recall) / (precision + recall)
        except ZeroDivisionError:
            f1 = 0

        if debug:
            print('label:%d' % label)
            print('tp:%f' % tp)
            print('fn:%f' % fn)
            print('fp:%f' % fp)
            print('tn:%f' % tn)
            print('unknown:%f' % unknown)
            print('sum:%f' % (tp+fn+fp+tn+unknown))
            print('precision:%f' % precision)
            print('recall:%f' % recall)
            print('f1:%f' % f1)
        
        return f1

    return sum([f1(gold, preds, label) for label in [0, 1]])/2


def accuracy(gold, preds):

    correct = 0.0
    for idx in range(len(gold)):
        if (gold[idx] == preds[idx]):
            correct += 1

    return correct / len(gold)


def load_labels(fn):

    labels = {}
    with open(fn) as f:
        for line in f:
            id_, lb = line.strip().split()
            labels[id_] = int(lb)
    
    return labels


if __name__ == '__main__':

    pred_fn = sys.argv[1]
    gold_fn = sys.argv[2]

    assert pred_fn.endswith('.tsv')
    assert gold_fn.endswith('.tsv')

    pred_labels_dict = load_labels(pred_fn)
    gold_labels_dict = load_labels(gold_fn)
    
    print('Loaded %d prediction labels.' % len(pred_labels_dict))
    print('Loaded %d gold labels.' % len(gold_labels_dict))

    # try:
    #     assert set(list(pred_labels_dict.keys())) == set(list(gold_labels_dict.keys()))
    # except AssertionError:
    #     print('Warning: Mismatched instance ids.')


    pred_labels, gold_labels = [], []
    for inst_id in sorted(gold_labels_dict.keys()):
        gold_labels.append(gold_labels_dict[inst_id])
        try:
            pred_labels.append(pred_labels_dict[inst_id])
        except KeyError:
            pred_labels.append(-1)  # missing instances labeled with -1

    print("Accuracy: %.4f" % accuracy(gold_labels, pred_labels))
    print("Macro-F1: %.4f" % f1_macro(gold_labels, pred_labels))
