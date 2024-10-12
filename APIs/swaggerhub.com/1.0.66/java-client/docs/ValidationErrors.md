

# ValidationErrors

Represents a [standardization](https://support.smartbear.com/swaggerhub/docs/organizations/api-standardization.html) error or warning

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The error message |  |
|**line** | **Integer** | The line number (0-based) where the issue occurs. If, for some reason, the broken rule does not include a line number, defaults to 0. |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The issue type: &#x60;CRITICAL&#x60; (error) or &#x60;WARNING&#x60; |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| CRITICAL | &quot;CRITICAL&quot; |
| WARNING | &quot;WARNING&quot; |



