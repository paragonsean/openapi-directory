# RecoveryServicesBackupClient.DpmJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | The state/actions applicable on this job like cancel/retry. | [optional] 
**containerName** | **String** | Name of cluster/server protecting current backup item, if any. | [optional] 
**containerType** | **String** | Type of container. | [optional] 
**dpmServerName** | **String** | DPM server name managing the backup item or backup job. | [optional] 
**duration** | **String** | Time elapsed for job. | [optional] 
**errorDetails** | [**[DpmErrorInfo]**](DpmErrorInfo.md) | The errors. | [optional] 
**extendedInfo** | [**DpmJobExtendedInfo**](DpmJobExtendedInfo.md) |  | [optional] 
**workloadType** | **String** | Type of backup item. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




