# GoogleFormsApi.MediaProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **String** | Position of the media. | [optional] 
**width** | **Number** | The width of the media in pixels. When the media is displayed, it is scaled to the smaller of this value or the width of the displayed form. The original aspect ratio of the media is preserved. If a width is not specified when the media is added to the form, it is set to the width of the media source. Width must be between 0 and 740, inclusive. Setting width to 0 or unspecified is only permitted when updating the media source. | [optional] 



## Enum: AlignmentEnum


* `ALIGNMENT_UNSPECIFIED` (value: `"ALIGNMENT_UNSPECIFIED"`)

* `LEFT` (value: `"LEFT"`)

* `RIGHT` (value: `"RIGHT"`)

* `CENTER` (value: `"CENTER"`)




