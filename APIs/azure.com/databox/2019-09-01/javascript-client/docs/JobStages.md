# DataBoxManagementClient.JobStages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Display name of the job stage. | [optional] [readonly] 
**errorDetails** | [**[JobErrorDetails]**](JobErrorDetails.md) | Error details for the stage. | [optional] [readonly] 
**jobStageDetails** | **Object** | Job Stage Details | [optional] [readonly] 
**stageName** | **String** | Name of the job stage. | [optional] [readonly] 
**stageStatus** | **String** | Status of the job stage. | [optional] [readonly] 
**stageTime** | **Date** | Time for the job stage in UTC ISO 8601 format. | [optional] [readonly] 



## Enum: StageNameEnum


* `DeviceOrdered` (value: `"DeviceOrdered"`)

* `DevicePrepared` (value: `"DevicePrepared"`)

* `Dispatched` (value: `"Dispatched"`)

* `Delivered` (value: `"Delivered"`)

* `PickedUp` (value: `"PickedUp"`)

* `AtAzureDC` (value: `"AtAzureDC"`)

* `DataCopy` (value: `"DataCopy"`)

* `Completed` (value: `"Completed"`)

* `CompletedWithErrors` (value: `"CompletedWithErrors"`)

* `Cancelled` (value: `"Cancelled"`)

* `Failed_IssueReportedAtCustomer` (value: `"Failed_IssueReportedAtCustomer"`)

* `Failed_IssueDetectedAtAzureDC` (value: `"Failed_IssueDetectedAtAzureDC"`)

* `Aborted` (value: `"Aborted"`)

* `CompletedWithWarnings` (value: `"CompletedWithWarnings"`)

* `ReadyToDispatchFromAzureDC` (value: `"ReadyToDispatchFromAzureDC"`)

* `ReadyToReceiveAtAzureDC` (value: `"ReadyToReceiveAtAzureDC"`)





## Enum: StageStatusEnum


* `None` (value: `"None"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Cancelling` (value: `"Cancelling"`)

* `SucceededWithErrors` (value: `"SucceededWithErrors"`)




