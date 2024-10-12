# RecoveryServicesBackupClient.AzureWorkloadJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | Gets or sets the state/actions applicable on this job like cancel/retry. | [optional] 
**duration** | **String** | Time elapsed during the execution of this job. | [optional] 
**errorDetails** | [**[AzureWorkloadErrorInfo]**](AzureWorkloadErrorInfo.md) | Error details on execution of this job. | [optional] 
**extendedInfo** | [**AzureWorkloadJobExtendedInfo**](AzureWorkloadJobExtendedInfo.md) |  | [optional] 
**workloadType** | **String** | Workload type of the job | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




