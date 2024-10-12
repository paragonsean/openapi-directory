

# InstanceViewStatus

Instance view status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The status code. |  [optional] |
|**displayStatus** | **String** | The short localizable label for the status. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | The level code. |  [optional] |
|**message** | **String** | The detailed status message, including for alerts and error messages. |  [optional] |
|**time** | **OffsetDateTime** | The time of the status. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| INFO | &quot;Info&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



