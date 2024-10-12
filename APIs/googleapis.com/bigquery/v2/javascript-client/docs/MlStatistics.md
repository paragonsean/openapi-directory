# BigQueryApi.MlStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hparamTrials** | [**[HparamTuningTrial]**](HparamTuningTrial.md) | Output only. Trials of a [hyperparameter tuning job](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) sorted by trial_id. | [optional] [readonly] 
**iterationResults** | [**[IterationResult]**](IterationResult.md) | Results for all completed iterations. Empty for [hyperparameter tuning jobs](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview). | [optional] 
**maxIterations** | **String** | Output only. Maximum number of iterations specified as max_iterations in the &#39;CREATE MODEL&#39; query. The actual number of iterations may be less than this number due to early stop. | [optional] [readonly] 
**modelType** | **String** | Output only. The type of the model that is being trained. | [optional] [readonly] 
**trainingType** | **String** | Output only. Training type of the job. | [optional] [readonly] 



## Enum: ModelTypeEnum


* `MODEL_TYPE_UNSPECIFIED` (value: `"MODEL_TYPE_UNSPECIFIED"`)

* `LINEAR_REGRESSION` (value: `"LINEAR_REGRESSION"`)

* `LOGISTIC_REGRESSION` (value: `"LOGISTIC_REGRESSION"`)

* `KMEANS` (value: `"KMEANS"`)

* `MATRIX_FACTORIZATION` (value: `"MATRIX_FACTORIZATION"`)

* `DNN_CLASSIFIER` (value: `"DNN_CLASSIFIER"`)

* `TENSORFLOW` (value: `"TENSORFLOW"`)

* `DNN_REGRESSOR` (value: `"DNN_REGRESSOR"`)

* `XGBOOST` (value: `"XGBOOST"`)

* `BOOSTED_TREE_REGRESSOR` (value: `"BOOSTED_TREE_REGRESSOR"`)

* `BOOSTED_TREE_CLASSIFIER` (value: `"BOOSTED_TREE_CLASSIFIER"`)

* `ARIMA` (value: `"ARIMA"`)

* `AUTOML_REGRESSOR` (value: `"AUTOML_REGRESSOR"`)

* `AUTOML_CLASSIFIER` (value: `"AUTOML_CLASSIFIER"`)

* `PCA` (value: `"PCA"`)

* `DNN_LINEAR_COMBINED_CLASSIFIER` (value: `"DNN_LINEAR_COMBINED_CLASSIFIER"`)

* `DNN_LINEAR_COMBINED_REGRESSOR` (value: `"DNN_LINEAR_COMBINED_REGRESSOR"`)

* `AUTOENCODER` (value: `"AUTOENCODER"`)

* `ARIMA_PLUS` (value: `"ARIMA_PLUS"`)

* `ARIMA_PLUS_XREG` (value: `"ARIMA_PLUS_XREG"`)

* `RANDOM_FOREST_REGRESSOR` (value: `"RANDOM_FOREST_REGRESSOR"`)

* `RANDOM_FOREST_CLASSIFIER` (value: `"RANDOM_FOREST_CLASSIFIER"`)

* `TENSORFLOW_LITE` (value: `"TENSORFLOW_LITE"`)

* `ONNX` (value: `"ONNX"`)





## Enum: TrainingTypeEnum


* `TRAINING_TYPE_UNSPECIFIED` (value: `"TRAINING_TYPE_UNSPECIFIED"`)

* `SINGLE_TRAINING` (value: `"SINGLE_TRAINING"`)

* `HPARAM_TUNING` (value: `"HPARAM_TUNING"`)




