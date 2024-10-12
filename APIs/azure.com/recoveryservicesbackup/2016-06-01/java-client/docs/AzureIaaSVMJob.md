

# AzureIaaSVMJob

The Azure IaaS VM workload-specific job object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | Gets or sets the state, or actions, applicable on this job. Examples of the actions are: Cancel or Retry. |  [optional] |
|**duration** | **String** | The time that elapsed during the execution of this job. |  [optional] |
|**errorDetails** | [**List&lt;AzureIaaSVMErrorInfo&gt;**](AzureIaaSVMErrorInfo.md) | Error details about this job. |  [optional] |
|**extendedInfo** | [**AzureIaaSVMJobExtendedInfo**](AzureIaaSVMJobExtendedInfo.md) |  |  [optional] |
|**virtualMachineVersion** | **String** | Specifies whether the backup item is a Classic VM or a Resource Manager VM. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



