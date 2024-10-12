# GoogleSlidesApi.Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageObjectId** | **String** | If set, indicates this is a link to the specific page in this presentation with this ID. A page with this ID may not exist. | [optional] 
**relativeLink** | **String** | If set, indicates this is a link to a slide in this presentation, addressed by its position. | [optional] 
**slideIndex** | **Number** | If set, indicates this is a link to the slide at this zero-based index in the presentation. There may not be a slide at this index. | [optional] 
**url** | **String** | If set, indicates this is a link to the external web page at this URL. | [optional] 



## Enum: RelativeLinkEnum


* `RELATIVE_SLIDE_LINK_UNSPECIFIED` (value: `"RELATIVE_SLIDE_LINK_UNSPECIFIED"`)

* `NEXT_SLIDE` (value: `"NEXT_SLIDE"`)

* `PREVIOUS_SLIDE` (value: `"PREVIOUS_SLIDE"`)

* `FIRST_SLIDE` (value: `"FIRST_SLIDE"`)

* `LAST_SLIDE` (value: `"LAST_SLIDE"`)




