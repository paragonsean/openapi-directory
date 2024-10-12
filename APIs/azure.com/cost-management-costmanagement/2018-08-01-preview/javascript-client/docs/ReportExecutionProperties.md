# CostManagementClient.ReportExecutionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionType** | **String** | The type of the report execution. | [optional] 
**fileName** | **String** | The name of the file report got written to. | [optional] 
**processingEndTime** | **Date** | The time when report execution finished. | [optional] 
**processingStartTime** | **Date** | The time when report was picked up to be executed. | [optional] 
**reportSettings** | [**CommonReportProperties**](CommonReportProperties.md) |  | [optional] 
**status** | **String** | The status of the report execution. | [optional] 
**submittedBy** | **String** | The identifier for the entity that executed the report. For OnDemand executions, it is the email id. For Scheduled executions, it is the constant value - System. | [optional] 
**submittedTime** | **Date** | The time when report was queued to be executed. | [optional] 



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




