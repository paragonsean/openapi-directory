

# OperationMetadata

Metadata describing an operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the operation was submitted to the server. |  [optional] |
|**endTime** | **String** | Output only. The time when the operation terminated, regardless of its success. This field is unset if the operation is still ongoing. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | Output only. The type of operation being performed. |  [optional] |
|**resource** | **String** | Output only. The resource being operated on, as a [relative resource name]( /apis/design/resource_names#relative_resource_name). |  [optional] |
|**resourceUuid** | **String** | Output only. The UUID of the resource being operated on. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current operation state. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| DELETE | &quot;DELETE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| CHECK | &quot;CHECK&quot; |
| SAVE_SNAPSHOT | &quot;SAVE_SNAPSHOT&quot; |
| LOAD_SNAPSHOT | &quot;LOAD_SNAPSHOT&quot; |
| DATABASE_FAILOVER | &quot;DATABASE_FAILOVER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |



