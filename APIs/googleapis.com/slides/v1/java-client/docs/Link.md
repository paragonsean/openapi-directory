

# Link

A hypertext link.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageObjectId** | **String** | If set, indicates this is a link to the specific page in this presentation with this ID. A page with this ID may not exist. |  [optional] |
|**relativeLink** | [**RelativeLinkEnum**](#RelativeLinkEnum) | If set, indicates this is a link to a slide in this presentation, addressed by its position. |  [optional] |
|**slideIndex** | **Integer** | If set, indicates this is a link to the slide at this zero-based index in the presentation. There may not be a slide at this index. |  [optional] |
|**url** | **String** | If set, indicates this is a link to the external web page at this URL. |  [optional] |



## Enum: RelativeLinkEnum

| Name | Value |
|---- | -----|
| RELATIVE_SLIDE_LINK_UNSPECIFIED | &quot;RELATIVE_SLIDE_LINK_UNSPECIFIED&quot; |
| NEXT_SLIDE | &quot;NEXT_SLIDE&quot; |
| PREVIOUS_SLIDE | &quot;PREVIOUS_SLIDE&quot; |
| FIRST_SLIDE | &quot;FIRST_SLIDE&quot; |
| LAST_SLIDE | &quot;LAST_SLIDE&quot; |



