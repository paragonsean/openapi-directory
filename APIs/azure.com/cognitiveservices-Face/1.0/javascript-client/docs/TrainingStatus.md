# FaceClient.TrainingStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDateTime** | **Date** | A combined UTC date and time string that describes the created time of the person group, large person group or large face list. | 
**lastActionDateTime** | **Date** | A combined UTC date and time string that describes the last modify time of the person group, large person group or large face list, could be null value when the group is not successfully trained. | [optional] 
**lastSuccessfulTrainingDateTime** | **Date** | A combined UTC date and time string that describes the last successful training time of the person group, large person group or large face list. | [optional] 
**message** | **String** | Show failure message when training failed (omitted when training succeed). | [optional] 
**status** | **String** | Training status: notstarted, running, succeeded, failed. If the training process is waiting to perform, the status is notstarted. If the training is ongoing, the status is running. Status succeed means this person group or large person group is ready for Face - Identify, or this large face list is ready for Face - Find Similar. Status failed is often caused by no person or no persisted face exist in the person group or large person group, or no persisted face exist in the large face list. | 



## Enum: StatusEnum


* `nonstarted` (value: `"nonstarted"`)

* `running` (value: `"running"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)




