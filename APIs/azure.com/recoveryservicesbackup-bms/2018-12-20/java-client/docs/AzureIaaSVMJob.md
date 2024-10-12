

# AzureIaaSVMJob

Azure IaaS VM workload-specific job object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | Gets or sets the state/actions applicable on this job like cancel/retry. |  [optional] |
|**duration** | **String** | Time elapsed during the execution of this job. |  [optional] |
|**errorDetails** | [**List&lt;AzureIaaSVMErrorInfo&gt;**](AzureIaaSVMErrorInfo.md) | Error details on execution of this job. |  [optional] |
|**extendedInfo** | [**AzureIaaSVMJobExtendedInfo**](AzureIaaSVMJobExtendedInfo.md) |  |  [optional] |
|**virtualMachineVersion** | **String** | Specifies whether the backup item is a Classic or an Azure Resource Manager VM. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



