

# DpmJob

DPM workload-specific job object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | The state/actions applicable on this job like cancel/retry. |  [optional] |
|**containerName** | **String** | Name of cluster/server protecting current backup item, if any. |  [optional] |
|**containerType** | **String** | Type of container. |  [optional] |
|**dpmServerName** | **String** | DPM server name managing the backup item or backup job. |  [optional] |
|**duration** | **String** | Time elapsed for job. |  [optional] |
|**errorDetails** | [**List&lt;DpmErrorInfo&gt;**](DpmErrorInfo.md) | The errors. |  [optional] |
|**extendedInfo** | [**DpmJobExtendedInfo**](DpmJobExtendedInfo.md) |  |  [optional] |
|**workloadType** | **String** | Type of backup item. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



