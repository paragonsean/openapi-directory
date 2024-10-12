# FilesComApi.AutomationRunEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automationId** | **Number** | ID of the associated Automation. | [optional] 
**completedAt** | **Date** | Automation run completion/failure date/time. | [optional] 
**createdAt** | **Date** | Automation run start date/time. | [optional] 
**id** | **Number** | ID. | [optional] 
**status** | **String** | The success status of the AutomationRun. One of &#x60;running&#x60;, &#x60;success&#x60;, &#x60;partial_failure&#x60;, or &#x60;failure&#x60;. | [optional] 
**statusMessagesUrl** | **String** | Link to status messages log file. | [optional] 



## Enum: StatusEnum


* `running` (value: `"running"`)

* `success` (value: `"success"`)

* `partial_failure` (value: `"partial_failure"`)

* `failure` (value: `"failure"`)

* `skipped` (value: `"skipped"`)




