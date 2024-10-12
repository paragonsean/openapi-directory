# BatchService.TaskCounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Number** |  | 
**completed** | **Number** |  | 
**failed** | **Number** |  | 
**running** | **Number** |  | 
**succeeded** | **Number** |  | 
**validationStatus** | **String** | If the validationStatus is unvalidated, then the Batch service has not been able to check state counts against the task states as reported in the List Tasks API. The validationStatus may be unvalidated if the job contains more than 200,000 tasks. | 



## Enum: ValidationStatusEnum


* `validated` (value: `"validated"`)

* `unvalidated` (value: `"unvalidated"`)




