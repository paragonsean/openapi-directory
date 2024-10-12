# RecoveryServicesBackupClient.AzureIaaSVMJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | Gets or sets the state/actions applicable on this job like cancel/retry. | [optional] 
**duration** | **String** | Time elapsed during the execution of this job. | [optional] 
**errorDetails** | [**[AzureIaaSVMErrorInfo]**](AzureIaaSVMErrorInfo.md) | Error details on execution of this job. | [optional] 
**extendedInfo** | [**AzureIaaSVMJobExtendedInfo**](AzureIaaSVMJobExtendedInfo.md) |  | [optional] 
**virtualMachineVersion** | **String** | Specifies whether the backup item is a Classic or an Azure Resource Manager VM. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




