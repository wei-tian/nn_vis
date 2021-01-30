from data.mnist_data_handler import get_prepared_data
from data.model_data import ModelData
from evaluation.evaluator import ImportanceEvaluator
from utility.log_handling import setup_logger

setup_logger("sample_evaluation")

name: str = "5_class"
model_data: ModelData = ModelData(name)
model_data.reload_model()
importance_handler: ImportanceEvaluator = ImportanceEvaluator(model_data)
importance_handler.setup(relevant_classes=[0, 1, 2, 3, 4])
(x_train, y_train), (x_test, y_test), input_shape, num_classes = get_prepared_data(model_data.get_class_selection())
importance_handler.set_train_and_test_data(x_train, y_train, x_test, y_test)
importance_handler.create_evaluation_data(10)
