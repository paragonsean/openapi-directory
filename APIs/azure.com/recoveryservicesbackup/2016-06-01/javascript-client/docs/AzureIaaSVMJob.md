# RecoveryServicesBackupClient.AzureIaaSVMJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | Gets or sets the state, or actions, applicable on this job. Examples of the actions are: Cancel or Retry. | [optional] 
**duration** | **String** | The time that elapsed during the execution of this job. | [optional] 
**errorDetails** | [**[AzureIaaSVMErrorInfo]**](AzureIaaSVMErrorInfo.md) | Error details about this job. | [optional] 
**extendedInfo** | [**AzureIaaSVMJobExtendedInfo**](AzureIaaSVMJobExtendedInfo.md) |  | [optional] 
**virtualMachineVersion** | **String** | Specifies whether the backup item is a Classic VM or a Resource Manager VM. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




