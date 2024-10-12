

# AzureWorkloadJob

Azure storage specific job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | Gets or sets the state/actions applicable on this job like cancel/retry. |  [optional] |
|**duration** | **String** | Time elapsed during the execution of this job. |  [optional] |
|**errorDetails** | [**List&lt;AzureWorkloadErrorInfo&gt;**](AzureWorkloadErrorInfo.md) | Error details on execution of this job. |  [optional] |
|**extendedInfo** | [**AzureWorkloadJobExtendedInfo**](AzureWorkloadJobExtendedInfo.md) |  |  [optional] |
|**workloadType** | **String** | Workload type of the job |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



