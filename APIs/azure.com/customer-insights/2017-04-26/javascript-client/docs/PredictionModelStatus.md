# CustomerInsightsManagementClient.PredictionModelStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | The model status message. | [optional] [readonly] 
**modelVersion** | **String** | Version of the model. | [optional] [readonly] 
**predictionGuidId** | **String** | The prediction GUID ID. | [optional] [readonly] 
**predictionName** | **String** | The prediction name. | [optional] [readonly] 
**signalsUsed** | **Number** | The signals used. | [optional] [readonly] 
**status** | **String** | Prediction model life cycle.  When prediction is in PendingModelConfirmation status, it is allowed to update the status to PendingFeaturing or Active through API. | 
**tenantId** | **String** | The hub name. | [optional] [readonly] 
**testSetCount** | **Number** | Count of the test set. | [optional] [readonly] 
**trainingAccuracy** | **Number** | The training accuracy. | [optional] [readonly] 
**trainingSetCount** | **Number** | Count of the training set. | [optional] [readonly] 
**validationSetCount** | **Number** | Count of the validation set. | [optional] [readonly] 



## Enum: StatusEnum


* `New` (value: `"New"`)

* `Provisioning` (value: `"Provisioning"`)

* `ProvisioningFailed` (value: `"ProvisioningFailed"`)

* `PendingDiscovering` (value: `"PendingDiscovering"`)

* `Discovering` (value: `"Discovering"`)

* `PendingFeaturing` (value: `"PendingFeaturing"`)

* `Featuring` (value: `"Featuring"`)

* `FeaturingFailed` (value: `"FeaturingFailed"`)

* `PendingTraining` (value: `"PendingTraining"`)

* `Training` (value: `"Training"`)

* `TrainingFailed` (value: `"TrainingFailed"`)

* `Evaluating` (value: `"Evaluating"`)

* `EvaluatingFailed` (value: `"EvaluatingFailed"`)

* `PendingModelConfirmation` (value: `"PendingModelConfirmation"`)

* `Active` (value: `"Active"`)

* `Deleted` (value: `"Deleted"`)

* `HumanIntervention` (value: `"HumanIntervention"`)

* `Failed` (value: `"Failed"`)




