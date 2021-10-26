# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:11:47 2021

@author: Nikhil
"""

import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@func_to_container_op
def show_results(logistic_regression:float,random_forest_classifier:float,linear_regression: float,random_forest_regressor:float) -> None:
    # The outputs from classifier and regressor models are shown

    print(f"Logistic regression (accuracy): {logistic_regression}")
    print(f"Random Forest Classifier (accuracy): {random_forest_classifier}")
    print(f"Linear regression (r2_score): {linear_regression}")
    print(f"Random Forest Regressor (r2_score): {random_forest_regressor}")


@dsl.pipeline(name='First Pipeline', description='Applies Logistic Regression & Random Forest classifier for classification and Linear Regression & Random Forest Regressor for regression problem.')
def first_pipeline():

    # Loads the yaml manifest for extract component
    extract_data = kfp.components.load_component_from_file('yaml_files/extract_data.yaml')
    
    # Loads the yaml manifest for process components for classifier & regression
    process_data_classifier = kfp.components.load_component_from_file('yaml_files/process_data_classifier.yaml')
    process_data_regressor = kfp.components.load_component_from_file('yaml_files/process_data_regressor.yaml')
    
    # Loads the yaml manifest for training all models
    logistic_regression = kfp.components.load_component_from_file('yaml_files/logistic_regression.yaml')
    linear_regression = kfp.components.load_component_from_file('yaml_files/linear_regression.yaml')
    random_forest_classifier = kfp.components.load_component_from_file('yaml_files/random_forest_classifier.yaml')
    random_forest_regressor = kfp.components.load_component_from_file('yaml_files/random_forest_regressor.yaml')

    # Run extract_data task
    extract_task = extract_data()

    # Run process data tasks for classifier and regressor
    process_data_classifier_task = process_data_classifier(extract_task.output)
    process_data_regressor_task = process_data_regressor(extract_task.output)
    
    # Run different modelling tasks give the processed data
    logistic_regression_task = logistic_regression(process_data_classifier_task.output)
    linear_regression_task = linear_regression(process_data_regressor_task.output)
    random_forest_classifier_task = random_forest_classifier(process_data_classifier_task.output)
    random_forest_regressor_task = random_forest_regressor(process_data_regressor_task.output)

    # The component "show_results" is called to print the results.
    show_results(logistic_regression_task.output,random_forest_classifier_task.output, linear_regression_task.output,random_forest_regressor_task.output)

# submit the pipeline for execution.
if __name__ == '__main__':
    pipeline = kfp.Client(host='https://6d07d799306957bb-dot-us-central1.pipelines.googleusercontent.com').create_run_from_pipeline_func(first_pipeline, arguments={})
