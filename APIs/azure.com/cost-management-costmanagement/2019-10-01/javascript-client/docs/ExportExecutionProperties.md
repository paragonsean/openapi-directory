# CostManagementClient.ExportExecutionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionType** | **String** | The type of the export execution. | [optional] 
**fileName** | **String** | The name of the file export got written to. | [optional] 
**processingEndTime** | **Date** | The time when export execution finished. | [optional] 
**processingStartTime** | **Date** | The time when export was picked up to be executed. | [optional] 
**runSettings** | [**CommonExportProperties**](CommonExportProperties.md) |  | [optional] 
**status** | **String** | The status of the export execution. | [optional] 
**submittedBy** | **String** | The identifier for the entity that executed the export. For OnDemand executions, it is the email id. For Scheduled executions, it is the constant value - System. | [optional] 
**submittedTime** | **Date** | The time when export was queued to be executed. | [optional] 



## Enum: ExecutionTypeEnum


* `OnDemand` (value: `"OnDemand"`)

* `Scheduled` (value: `"Scheduled"`)





## Enum: StatusEnum


* `Queued` (value: `"Queued"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)

* `Timeout` (value: `"Timeout"`)

* `NewDataNotAvailable` (value: `"NewDataNotAvailable"`)

* `DataNotAvailable` (value: `"DataNotAvailable"`)




