

# MSDeployLogEntry

MSDeploy log entry

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Log entry message |  [optional] [readonly] |
|**time** | **OffsetDateTime** | Timestamp of log entry |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Log entry type |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MESSAGE | &quot;Message&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



