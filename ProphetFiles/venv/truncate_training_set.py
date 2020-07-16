import pandas as pd


def truncate_training_set(training_set):
    try:
        return training_set.replace(minute=0, second=0,  microsecond=0)
    except TypeError:
        print("These function is meant to take individual values of a date/time column and truncate them. ")
        print("The input should be an individual date/time value")

