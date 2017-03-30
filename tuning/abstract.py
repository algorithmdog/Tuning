#!/bin/python

class Architectures_HyperParameters:
    def get_tf_code(self):
        raise NotImplementedError("The get_tf_code function hasn't been implemented")

class DeepLearningAlgorithm:
    def get_metrics_score(self, architectures_hyperparameters):
        raise NotImplementedError("The get_metric_score function hasn't been implementd") 

class TuningAlgorithm:
    def run(self, DeepLearningAlgorithm):
        raise NotImplementedError("The run function hasn't been implemented")
