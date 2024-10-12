

# SectionStyle

The styling that applies to a section.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnProperties** | [**List&lt;SectionColumnProperties&gt;**](SectionColumnProperties.md) | The section&#39;s columns properties. If empty, the section contains one column with the default properties in the Docs editor. A section can be updated to have no more than 3 columns. When updating this property, setting a concrete value is required. Unsetting this property will result in a 400 bad request error. |  [optional] |
|**columnSeparatorStyle** | [**ColumnSeparatorStyleEnum**](#ColumnSeparatorStyleEnum) | The style of column separators. This style can be set even when there&#39;s one column in the section. When updating this property, setting a concrete value is required. Unsetting this property results in a 400 bad request error. |  [optional] |
|**contentDirection** | [**ContentDirectionEnum**](#ContentDirectionEnum) | The content direction of this section. If unset, the value defaults to LEFT_TO_RIGHT. When updating this property, setting a concrete value is required. Unsetting this property results in a 400 bad request error. |  [optional] |
|**defaultFooterId** | **String** | The ID of the default footer. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s default_footer_id. This property is read-only. |  [optional] |
|**defaultHeaderId** | **String** | The ID of the default header. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s default_header_id. This property is read-only. |  [optional] |
|**evenPageFooterId** | **String** | The ID of the footer used only for even pages. If the value of DocumentStyle&#39;s use_even_page_header_footer is true, this value is used for the footers on even pages in the section. If it is false, the footers on even pages use the default_footer_id. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s even_page_footer_id. This property is read-only. |  [optional] |
|**evenPageHeaderId** | **String** | The ID of the header used only for even pages. If the value of DocumentStyle&#39;s use_even_page_header_footer is true, this value is used for the headers on even pages in the section. If it is false, the headers on even pages use the default_header_id. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s even_page_header_id. This property is read-only. |  [optional] |
|**firstPageFooterId** | **String** | The ID of the footer used only for the first page of the section. If use_first_page_header_footer is true, this value is used for the footer on the first page of the section. If it&#39;s false, the footer on the first page of the section uses the default_footer_id. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s first_page_footer_id. This property is read-only. |  [optional] |
|**firstPageHeaderId** | **String** | The ID of the header used only for the first page of the section. If use_first_page_header_footer is true, this value is used for the header on the first page of the section. If it&#39;s false, the header on the first page of the section uses the default_header_id. If unset, the value inherits from the previous SectionBreak&#39;s SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle&#39;s first_page_header_id. This property is read-only. |  [optional] |
|**flipPageOrientation** | **Boolean** | Optional. Indicates whether to flip the dimensions of DocumentStyle&#39;s page_size for this section, which allows changing the page orientation between portrait and landscape. If unset, the value inherits from DocumentStyle&#39;s flip_page_orientation. When updating this property, setting a concrete value is required. Unsetting this property results in a 400 bad request error. |  [optional] |
|**marginBottom** | [**Dimension**](Dimension.md) |  |  [optional] |
|**marginFooter** | [**Dimension**](Dimension.md) |  |  [optional] |
|**marginHeader** | [**Dimension**](Dimension.md) |  |  [optional] |
|**marginLeft** | [**Dimension**](Dimension.md) |  |  [optional] |
|**marginRight** | [**Dimension**](Dimension.md) |  |  [optional] |
|**marginTop** | [**Dimension**](Dimension.md) |  |  [optional] |
|**pageNumberStart** | **Integer** | The page number from which to start counting the number of pages for this section. If unset, page numbering continues from the previous section. If the value is unset in the first SectionBreak, refer to DocumentStyle&#39;s page_number_start. When updating this property, setting a concrete value is required. Unsetting this property results in a 400 bad request error. |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Output only. The type of section. |  [optional] |
|**useFirstPageHeaderFooter** | **Boolean** | Indicates whether to use the first page header / footer IDs for the first page of the section. If unset, it inherits from DocumentStyle&#39;s use_first_page_header_footer for the first section. If the value is unset for subsequent sectors, it should be interpreted as false. When updating this property, setting a concrete value is required. Unsetting this property results in a 400 bad request error. |  [optional] |



## Enum: ColumnSeparatorStyleEnum

| Name | Value |
|---- | -----|
| COLUMN_SEPARATOR_STYLE_UNSPECIFIED | &quot;COLUMN_SEPARATOR_STYLE_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| BETWEEN_EACH_COLUMN | &quot;BETWEEN_EACH_COLUMN&quot; |



## Enum: ContentDirectionEnum

| Name | Value |
|---- | -----|
| CONTENT_DIRECTION_UNSPECIFIED | &quot;CONTENT_DIRECTION_UNSPECIFIED&quot; |
| LEFT_TO_RIGHT | &quot;LEFT_TO_RIGHT&quot; |
| RIGHT_TO_LEFT | &quot;RIGHT_TO_LEFT&quot; |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| SECTION_TYPE_UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| CONTINUOUS | &quot;CONTINUOUS&quot; |
| NEXT_PAGE | &quot;NEXT_PAGE&quot; |



