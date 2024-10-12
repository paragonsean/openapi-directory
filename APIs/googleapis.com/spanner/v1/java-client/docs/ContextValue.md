

# ContextValue

A message representing context for a KeyRangeInfo, including a label, value, unit, and severity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of this context. |  [optional] |
|**unit** | **String** | The unit of the context value. |  [optional] |
|**value** | **Float** | The value for the context. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| INFO | &quot;INFO&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |
| FATAL | &quot;FATAL&quot; |



