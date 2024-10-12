# DataShareManagementClient.ShareSynchronization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerEmail** | **String** | Email of the user who created the synchronization | [optional] 
**consumerName** | **String** | Name of the user who created the synchronization | [optional] 
**consumerTenantName** | **String** | Tenant name of the consumer who created the synchronization | [optional] 
**durationMs** | **Number** | synchronization duration | [optional] 
**endTime** | **Date** | End time of synchronization | [optional] 
**message** | **String** | message of synchronization | [optional] 
**startTime** | **Date** | start time of synchronization | [optional] 
**status** | **String** | Raw Status | [optional] 
**synchronizationId** | **String** | Synchronization id | [optional] 
**synchronizationMode** | **String** | Synchronization mode | [optional] [readonly] 



## Enum: SynchronizationModeEnum


* `Incremental` (value: `"Incremental"`)

* `FullSync` (value: `"FullSync"`)




