

# MlStatistics

Job statistics specific to a BigQuery ML training job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hparamTrials** | [**List&lt;HparamTuningTrial&gt;**](HparamTuningTrial.md) | Output only. Trials of a [hyperparameter tuning job](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) sorted by trial_id. |  [optional] [readonly] |
|**iterationResults** | [**List&lt;IterationResult&gt;**](IterationResult.md) | Results for all completed iterations. Empty for [hyperparameter tuning jobs](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview). |  [optional] |
|**maxIterations** | **String** | Output only. Maximum number of iterations specified as max_iterations in the &#39;CREATE MODEL&#39; query. The actual number of iterations may be less than this number due to early stop. |  [optional] [readonly] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) | Output only. The type of the model that is being trained. |  [optional] [readonly] |
|**trainingType** | [**TrainingTypeEnum**](#TrainingTypeEnum) | Output only. Training type of the job. |  [optional] [readonly] |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| MODEL_TYPE_UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| LINEAR_REGRESSION | &quot;LINEAR_REGRESSION&quot; |
| LOGISTIC_REGRESSION | &quot;LOGISTIC_REGRESSION&quot; |
| KMEANS | &quot;KMEANS&quot; |
| MATRIX_FACTORIZATION | &quot;MATRIX_FACTORIZATION&quot; |
| DNN_CLASSIFIER | &quot;DNN_CLASSIFIER&quot; |
| TENSORFLOW | &quot;TENSORFLOW&quot; |
| DNN_REGRESSOR | &quot;DNN_REGRESSOR&quot; |
| XGBOOST | &quot;XGBOOST&quot; |
| BOOSTED_TREE_REGRESSOR | &quot;BOOSTED_TREE_REGRESSOR&quot; |
| BOOSTED_TREE_CLASSIFIER | &quot;BOOSTED_TREE_CLASSIFIER&quot; |
| ARIMA | &quot;ARIMA&quot; |
| AUTOML_REGRESSOR | &quot;AUTOML_REGRESSOR&quot; |
| AUTOML_CLASSIFIER | &quot;AUTOML_CLASSIFIER&quot; |
| PCA | &quot;PCA&quot; |
| DNN_LINEAR_COMBINED_CLASSIFIER | &quot;DNN_LINEAR_COMBINED_CLASSIFIER&quot; |
| DNN_LINEAR_COMBINED_REGRESSOR | &quot;DNN_LINEAR_COMBINED_REGRESSOR&quot; |
| AUTOENCODER | &quot;AUTOENCODER&quot; |
| ARIMA_PLUS | &quot;ARIMA_PLUS&quot; |
| ARIMA_PLUS_XREG | &quot;ARIMA_PLUS_XREG&quot; |
| RANDOM_FOREST_REGRESSOR | &quot;RANDOM_FOREST_REGRESSOR&quot; |
| RANDOM_FOREST_CLASSIFIER | &quot;RANDOM_FOREST_CLASSIFIER&quot; |
| TENSORFLOW_LITE | &quot;TENSORFLOW_LITE&quot; |
| ONNX | &quot;ONNX&quot; |



## Enum: TrainingTypeEnum

| Name | Value |
|---- | -----|
| TRAINING_TYPE_UNSPECIFIED | &quot;TRAINING_TYPE_UNSPECIFIED&quot; |
| SINGLE_TRAINING | &quot;SINGLE_TRAINING&quot; |
| HPARAM_TUNING | &quot;HPARAM_TUNING&quot; |



