from abc import abstractmethod, ABCMeta


class Classifier():
    __metaclass__ = ABCMeta

    def passes_filter(self, datum):
        return True

    @abstractmethod
    def load_pkl_classifier(self, pkl_classifier):
        return NotImplementedError

    @abstractmethod
    def pkl_classifier(self):
        return NotImplementedError

    @abstractmethod
    def prepare_prediction_data(self, data):
        return NotImplementedError

    @abstractmethod
    def prepare_training_data(self, data):
        return NotImplementedError