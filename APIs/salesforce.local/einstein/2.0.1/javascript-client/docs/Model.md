# EinsteinVisionAndEinsteinLanguage.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Algorithm used to create the model. Returned only when the modelType is image-detection. | [optional] 
**createdAt** | **Date** | Date and time that the model was created. | [optional] 
**datasetId** | **Number** | ID of the dataset trained to create the model. | 
**datasetVersionId** | **Number** | Not available yet | 
**failureMsg** | **String** | Reason the dataset training failed. Returned only if the training status is FAILED. | [optional] 
**language** | **String** | Model language inherited from the dataset language. For image datasets, default is N/A. For text datasets, default is en_US. | [optional] 
**modelId** | **String** | ID of the model. Contains letters and numbers. | 
**modelType** | **String** | Type of data from which the model was created. | [optional] 
**name** | **String** | Name of the model. | 
**object** | **String** | Object returned; in this case, model. | [optional] 
**progress** | **Number** | How far the dataset training has progressed. Values are between 0�1. | 
**status** | **String** | Status of the model. | 
**updatedAt** | **Date** | Date and time that the model was last updated. | [optional] 



## Enum: StatusEnum


* `QUEUED` (value: `"QUEUED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `KILLED` (value: `"KILLED"`)

* `FAILED_WITH_RETRIES` (value: `"FAILED_WITH_RETRIES"`)




