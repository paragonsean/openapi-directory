

# ValidationMessage

Represent user-facing validation result message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | A custom code identifying this specific message. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Message severity level (warning or error). |  [optional] |
|**message** | **String** | The result of the validation. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Additional metadata related to the result. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;LEVEL_UNSPECIFIED&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |



