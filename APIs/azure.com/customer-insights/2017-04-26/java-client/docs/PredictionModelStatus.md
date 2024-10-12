

# PredictionModelStatus

The prediction model status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The model status message. |  [optional] [readonly] |
|**modelVersion** | **String** | Version of the model. |  [optional] [readonly] |
|**predictionGuidId** | **String** | The prediction GUID ID. |  [optional] [readonly] |
|**predictionName** | **String** | The prediction name. |  [optional] [readonly] |
|**signalsUsed** | **Integer** | The signals used. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Prediction model life cycle.  When prediction is in PendingModelConfirmation status, it is allowed to update the status to PendingFeaturing or Active through API. |  |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |
|**testSetCount** | **Integer** | Count of the test set. |  [optional] [readonly] |
|**trainingAccuracy** | **Integer** | The training accuracy. |  [optional] [readonly] |
|**trainingSetCount** | **Integer** | Count of the training set. |  [optional] [readonly] |
|**validationSetCount** | **Integer** | Count of the validation set. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| PROVISIONING_FAILED | &quot;ProvisioningFailed&quot; |
| PENDING_DISCOVERING | &quot;PendingDiscovering&quot; |
| DISCOVERING | &quot;Discovering&quot; |
| PENDING_FEATURING | &quot;PendingFeaturing&quot; |
| FEATURING | &quot;Featuring&quot; |
| FEATURING_FAILED | &quot;FeaturingFailed&quot; |
| PENDING_TRAINING | &quot;PendingTraining&quot; |
| TRAINING | &quot;Training&quot; |
| TRAINING_FAILED | &quot;TrainingFailed&quot; |
| EVALUATING | &quot;Evaluating&quot; |
| EVALUATING_FAILED | &quot;EvaluatingFailed&quot; |
| PENDING_MODEL_CONFIRMATION | &quot;PendingModelConfirmation&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETED | &quot;Deleted&quot; |
| HUMAN_INTERVENTION | &quot;HumanIntervention&quot; |
| FAILED | &quot;Failed&quot; |



