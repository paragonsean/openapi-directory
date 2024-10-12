# BigQueryApi.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestTrialId** | **String** | The best trial_id across all training runs. | [optional] 
**creationTime** | **String** | Output only. The time when this model was created, in millisecs since the epoch. | [optional] [readonly] 
**defaultTrialId** | **String** | Output only. The default trial_id to use in TVFs when the trial_id is not passed in. For single-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the best trial ID. For multi-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the smallest trial ID among all Pareto optimal trials. | [optional] [readonly] 
**description** | **String** | Optional. A user-friendly description of this model. | [optional] 
**encryptionConfiguration** | [**EncryptionConfiguration**](EncryptionConfiguration.md) |  | [optional] 
**etag** | **String** | Output only. A hash of this resource. | [optional] [readonly] 
**expirationTime** | **String** | Optional. The time when this model expires, in milliseconds since the epoch. If not present, the model will persist indefinitely. Expired models will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created models. | [optional] 
**featureColumns** | [**[StandardSqlField]**](StandardSqlField.md) | Output only. Input feature columns for the model inference. If the model is trained with TRANSFORM clause, these are the input of the TRANSFORM clause. | [optional] [readonly] 
**friendlyName** | **String** | Optional. A descriptive name for this model. | [optional] 
**hparamSearchSpaces** | [**HparamSearchSpaces**](HparamSearchSpaces.md) |  | [optional] 
**hparamTrials** | [**[HparamTuningTrial]**](HparamTuningTrial.md) | Output only. Trials of a [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) model sorted by trial_id. | [optional] [readonly] 
**labelColumns** | [**[StandardSqlField]**](StandardSqlField.md) | Output only. Label columns that were used to train this model. The output of the model will have a \&quot;predicted_\&quot; prefix to these columns. | [optional] [readonly] 
**labels** | **{String: String}** | The labels associated with this model. You can use these to organize and group your models. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. | [optional] 
**lastModifiedTime** | **String** | Output only. The time when this model was last modified, in millisecs since the epoch. | [optional] [readonly] 
**location** | **String** | Output only. The geographic location where the model resides. This value is inherited from the dataset. | [optional] [readonly] 
**modelReference** | [**ModelReference**](ModelReference.md) |  | [optional] 
**modelType** | **String** | Output only. Type of the model resource. | [optional] [readonly] 
**optimalTrialIds** | **[String]** | Output only. For single-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it only contains the best trial. For multi-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it contains all Pareto optimal trials sorted by trial_id. | [optional] [readonly] 
**remoteModelInfo** | [**RemoteModelInfo**](RemoteModelInfo.md) |  | [optional] 
**trainingRuns** | [**[TrainingRun]**](TrainingRun.md) | Information for all training runs in increasing order of start_time. | [optional] 
**transformColumns** | [**[TransformColumn]**](TransformColumn.md) | Output only. This field will be populated if a TRANSFORM clause was used to train a model. TRANSFORM clause (if used) takes feature_columns as input and outputs transform_columns. transform_columns then are used to train the model. | [optional] [readonly] 



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




