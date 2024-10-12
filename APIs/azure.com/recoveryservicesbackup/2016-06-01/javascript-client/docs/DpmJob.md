# RecoveryServicesBackupClient.DpmJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | The state or actions applicable on this job, such as Cancel or Retry. | [optional] 
**containerName** | **String** | The name of the cluster or server protecting the current backup item, if any. | [optional] 
**containerType** | **String** | The type of container. | [optional] 
**dpmServerName** | **String** | DPM server name managing the backup item or backup job. | [optional] 
**duration** | **String** | The time elapsed for the job. | [optional] 
**errorDetails** | [**[DpmErrorInfo]**](DpmErrorInfo.md) | The errors. | [optional] 
**extendedInfo** | [**DpmJobExtendedInfo**](DpmJobExtendedInfo.md) |  | [optional] 
**workloadType** | **String** | The type of backup item. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




