

# AzureStorageJob

Azure storage specific job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | Gets or sets the state/actions applicable on this job like cancel/retry. |  [optional] |
|**duration** | **String** | Time elapsed during the execution of this job. |  [optional] |
|**errorDetails** | [**List&lt;AzureStorageErrorInfo&gt;**](AzureStorageErrorInfo.md) | Error details on execution of this job. |  [optional] |
|**extendedInfo** | [**AzureStorageJobExtendedInfo**](AzureStorageJobExtendedInfo.md) |  |  [optional] |
|**storageAccountName** | **String** | Specifies friendly name of the storage account. |  [optional] |
|**storageAccountVersion** | **String** | Specifies whether the Storage account is a Classic or an Azure Resource Manager Storage account. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



