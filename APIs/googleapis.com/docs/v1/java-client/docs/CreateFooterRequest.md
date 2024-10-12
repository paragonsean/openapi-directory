

# CreateFooterRequest

Creates a Footer. The new footer is applied to the SectionStyle at the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle. If a footer of the specified type already exists, a 400 bad request error is returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sectionBreakLocation** | [**Location**](Location.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of footer to create. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEADER_FOOTER_TYPE_UNSPECIFIED | &quot;HEADER_FOOTER_TYPE_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |



