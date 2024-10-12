

# StartEnvironmentMetadata

Message included in the metadata field of operations returned from StartEnvironment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | Current state of the environment being started. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STARTING | &quot;STARTING&quot; |
| UNARCHIVING_DISK | &quot;UNARCHIVING_DISK&quot; |
| AWAITING_COMPUTE_RESOURCES | &quot;AWAITING_COMPUTE_RESOURCES&quot; |
| FINISHED | &quot;FINISHED&quot; |



