

# CreateHeaderRequest

Creates a Header. The new header is applied to the SectionStyle at the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle. If a header of the specified type already exists, a 400 bad request error is returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sectionBreakLocation** | [**Location**](Location.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of header to create. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEADER_FOOTER_TYPE_UNSPECIFIED | &quot;HEADER_FOOTER_TYPE_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |



