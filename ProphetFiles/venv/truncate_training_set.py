import pandas as pd


def truncate_training_set(training_set):
    return training_set.replace(minute=0, second=0,  microsecond=0)
