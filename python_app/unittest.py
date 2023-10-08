import unittest
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib

class TestLogisticRegressionModel(unittest.TestCase):
    def setUp(self):
        # Load the dataset
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        self.dataframe = pd.read_csv(url, names=names)
        self.array = self.dataframe.values
        self.X = self.array[:, 0:8]
        self.Y = self.array[:, 8]
        self.test_size = 0.33
        self.seed = 7
        self.X_train, self.X_test, self.Y_train, self.Y_test = model_selection.train_test_split(self.X, self.Y, test_size=self.test_size, random_state=self.seed)

    def test_model_creation(self):
        # Test if the model is created successfully
        model = LogisticRegression(solver='lbfgs', max_iter=400)
        self.assertIsNotNone(model)

    def test_model_training(self):
        # Test if the model can be trained successfully
        model = LogisticRegression(solver='lbfgs', max_iter=400)
        model.fit(self.X_train, self.Y_train)
        self.assertTrue(hasattr(model, 'coef_'))

    def test_model_saving_and_loading(self):
        # Test if the model can be saved and loaded successfully
        model = LogisticRegression(solver='lbfgs', max_iter=400)
        model.fit(self.X_train, self.Y_train)

        filename = 'logistic_test.sav'
        joblib.dump(model, filename)

        loaded_model = joblib.load(filename)
        result = loaded_model.score(self.X_test, self.Y_test)

        self.assertAlmostEqual(result, 0.0, places=2)  # Adjust the expected score accordingly

if __name__ == '__main__':
    unittest.main()
