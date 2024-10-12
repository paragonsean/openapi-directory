

# GoogleCloudApigeeV1OperationMetadataProgress

Information about operation progress.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the operation&#39;s progress. |  [optional] |
|**details** | **Map&lt;String, Object&gt;** | The additional details of the progress. |  [optional] |
|**percentDone** | **Integer** | The percentage of the operation progress. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| FINISHED | &quot;FINISHED&quot; |



