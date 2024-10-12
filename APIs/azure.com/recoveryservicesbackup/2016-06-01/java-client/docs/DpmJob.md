

# DpmJob

The DPM workload-specific job object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | The state or actions applicable on this job, such as Cancel or Retry. |  [optional] |
|**containerName** | **String** | The name of the cluster or server protecting the current backup item, if any. |  [optional] |
|**containerType** | **String** | The type of container. |  [optional] |
|**dpmServerName** | **String** | DPM server name managing the backup item or backup job. |  [optional] |
|**duration** | **String** | The time elapsed for the job. |  [optional] |
|**errorDetails** | [**List&lt;DpmErrorInfo&gt;**](DpmErrorInfo.md) | The errors. |  [optional] |
|**extendedInfo** | [**DpmJobExtendedInfo**](DpmJobExtendedInfo.md) |  |  [optional] |
|**workloadType** | **String** | The type of backup item. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



