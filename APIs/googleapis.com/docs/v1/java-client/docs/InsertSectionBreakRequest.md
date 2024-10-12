

# InsertSectionBreakRequest

Inserts a section break at the given location. A newline character will be inserted before the section break.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endOfSegmentLocation** | [**EndOfSegmentLocation**](EndOfSegmentLocation.md) |  |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | The type of section to insert. |  [optional] |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| SECTION_TYPE_UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| CONTINUOUS | &quot;CONTINUOUS&quot; |
| NEXT_PAGE | &quot;NEXT_PAGE&quot; |



