

# GetTemplateResponse

The response to a GetTemplate request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  |  [optional] |
|**runtimeMetadata** | [**RuntimeMetadata**](RuntimeMetadata.md) |  |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**templateType** | [**TemplateTypeEnum**](#TemplateTypeEnum) | Template Type. |  [optional] |



## Enum: TemplateTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LEGACY | &quot;LEGACY&quot; |
| FLEX | &quot;FLEX&quot; |



