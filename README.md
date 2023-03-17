# TempoWiC - An Evaluation Benchmark for Detecting Meaning Shift in Social Media

This repository contains the starting kit for the TempoWiC Shared Task for EvoNLP: The First Workshop on Ever Evolving NLP, co-located with EMNLP 2022.

For more details about the task, please visit:
https://sites.google.com/view/evonlp/shared-task

The TempoWiC dataset is described in the following paper, accepted to COLING 2022:
https://aclanthology.org/2022.coling-1.296/


Below you may find some details about the contents of this repository.

Code for fine-tuning and similarity baselines will be added soon.


## Instances (data/*.jl)

Contains instances with pairs of tweets and respective dates. It's organized as jsonlines (one instance per line), using the following structure for each instance:

```
{
  "id": str,            # instance id
  "word": str,          # target word (lemmatized)
  "tweet1": {
    "text": str,        # raw text
    "tokens": list,     # tokenized text
    "token_idx": int,   # token index for the target word in the tokenized text
    "text_start": int,  # character index for the first position of target word in the raw text
    "text_end": int,    # character index for the last position of target word in the raw text
    "date": str         # tweet1's date in YYYY-MM format
  },
  "tweet2": {
    "text": str,        # raw text
    "tokens": list,     # tokenized text
    "token_idx": int,   # token index for the target word
    "text_start": int,  # character index for the first position of target word
    "text_end": int,    # character index for the last position of target word
    "date": str         # tweet2's date in YYYY-MM format
  }
}
```

Tweets have been tokenized using NLTK's TweetTokenizer and both the raw and tokenized versions of the tweets are provided.

This starting kit includes the following sets:
- Trial (20 instances, for practicing submissions on Codalab)
- Training (1,428 instances)
- Validation (396 instances)
- Test (10,000 instances, includes dummy instances to discourage cheating)


UPDATE 2023/03/17: Gold test labels are now available (data/test.gold.tsv - without entries for dummy instances).


## Labels (data/*.labels.tsv)

Contains gold labels for each instance. One id/label per line, following the format "`<instance id><tab><0 if False, 1 if True>`".

Labels for test instances will remain hidden.


## Printing JSON

Outputs instance data stored as .jl in a more readable format. For easier inspection.

```bash
python pprint.py data/trial.data.jl
```


## Random baseline

A script showing how to load the dataset and generate a predictions file compatible with the scorer.

```bash
python baselines/random_baseline.py data/trial.data.jl predictions/trial.random-preds.tsv
```


## Scoring script

A simple python script to generate official scores for the task. Reports Accuracy and Macro-F1. To be used as follows:

```bash
python score.py predictions/trial.random-preds.tsv data/trial.gold.tsv
```

Predictions need to be stored in a .tsv file where each line corresponds to the tweet id of the instance and 1 (if the meaning of the target word has not changed) or 0 (if the meaning of the target word is different in both tweets). See "predictions/trial.random-preds.tsv" for an example.
