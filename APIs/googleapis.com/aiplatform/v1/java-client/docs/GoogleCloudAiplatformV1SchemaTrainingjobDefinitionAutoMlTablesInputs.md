

# GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalExperiments** | **List&lt;String&gt;** | Additional experiment flags for the Tables training pipeline. |  [optional] |
|**disableEarlyStopping** | **Boolean** | Use the entire training budget. This disables the early stopping feature. By default, the early stopping feature is enabled, which means that AutoML Tables might stop training before the entire training budget has been used. |  [optional] |
|**exportEvaluatedDataItemsConfig** | [**GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig**](GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig.md) |  |  [optional] |
|**optimizationObjective** | **String** | Objective function the model is optimizing towards. The training process creates a model that maximizes/minimizes the value of the objective function over the validation set. The supported optimization objectives depend on the prediction type. If the field is not set, a default objective function is used. classification (binary): \&quot;maximize-au-roc\&quot; (default) - Maximize the area under the receiver operating characteristic (ROC) curve. \&quot;minimize-log-loss\&quot; - Minimize log loss. \&quot;maximize-au-prc\&quot; - Maximize the area under the precision-recall curve. \&quot;maximize-precision-at-recall\&quot; - Maximize precision for a specified recall value. \&quot;maximize-recall-at-precision\&quot; - Maximize recall for a specified precision value. classification (multi-class): \&quot;minimize-log-loss\&quot; (default) - Minimize log loss. regression: \&quot;minimize-rmse\&quot; (default) - Minimize root-mean-squared error (RMSE). \&quot;minimize-mae\&quot; - Minimize mean-absolute error (MAE). \&quot;minimize-rmsle\&quot; - Minimize root-mean-squared log error (RMSLE). |  [optional] |
|**optimizationObjectivePrecisionValue** | **Float** | Required when optimization_objective is \&quot;maximize-recall-at-precision\&quot;. Must be between 0 and 1, inclusive. |  [optional] |
|**optimizationObjectiveRecallValue** | **Float** | Required when optimization_objective is \&quot;maximize-precision-at-recall\&quot;. Must be between 0 and 1, inclusive. |  [optional] |
|**predictionType** | **String** | The type of prediction the Model is to produce. \&quot;classification\&quot; - Predict one out of multiple target values is picked for each row. \&quot;regression\&quot; - Predict a value based on its relation to other values. This type is available only to columns that contain semantically numeric values, i.e. integers or floating point number, even if stored as e.g. strings. |  [optional] |
|**targetColumn** | **String** | The column name of the target column that the model is to predict. |  [optional] |
|**trainBudgetMilliNodeHours** | **String** | Required. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend&#39;s discretion. This especially may happen when further model training ceases to provide any improvements. If the budget is set to a value known to be insufficient to train a model for the given dataset, the training won&#39;t be attempted and will error. The train budget must be between 1,000 and 72,000 milli node hours, inclusive. |  [optional] |
|**transformations** | [**List&lt;GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation&gt;**](GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation.md) | Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using \&quot;.\&quot; as the delimiter. |  [optional] |
|**weightColumnName** | **String** | Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1. |  [optional] |



