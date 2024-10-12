

# BatchOperationMetadata

Metadata used for long running operations returned by CTS batch APIs. It's used to replace google.longrunning.Operation.metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time when the batch operation is created. |  [optional] |
|**endTime** | **String** | The time when the batch operation is finished and google.longrunning.Operation.done is set to &#x60;true&#x60;. |  [optional] |
|**failureCount** | **Integer** | Count of failed item(s) inside an operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of a long running operation. |  [optional] |
|**stateDescription** | **String** | More detailed information about operation state. |  [optional] |
|**successCount** | **Integer** | Count of successful item(s) inside an operation. |  [optional] |
|**totalCount** | **Integer** | Count of total item(s) inside an operation. |  [optional] |
|**updateTime** | **String** | The time when the batch operation status is updated. The metadata and the update_time is refreshed every minute otherwise cached data is returned. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



