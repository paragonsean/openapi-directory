# AutomationManagement.SourceControlSyncJobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | The creation time of the job. | [optional] [readonly] 
**endTime** | **Date** | The end time of the job. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the job. | [optional] 
**sourceControlSyncJobId** | **String** | The source control sync job id. | [optional] 
**startTime** | **Date** | The start time of the job. | [optional] [readonly] 
**syncType** | **String** | The sync type. | [optional] 



## Enum: ProvisioningStateEnum


* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)

* `Running` (value: `"Running"`)





## Enum: SyncTypeEnum


* `PartialSync` (value: `"PartialSync"`)

* `FullSync` (value: `"FullSync"`)




