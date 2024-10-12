

# Diagnostic

Represents a diagnostic message (error or warning)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of diagnostic information provided. |  [optional] |
|**location** | **String** | File name and line number of the error or warning. |  [optional] |
|**message** | **String** | Message describing the error or warning. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |



