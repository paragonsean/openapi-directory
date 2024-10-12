# GoogleSlidesApi.Autofit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autofitType** | **String** | The autofit type of the shape. If the autofit type is AUTOFIT_TYPE_UNSPECIFIED, the autofit type is inherited from a parent placeholder if it exists. The field is automatically set to NONE if a request is made that might affect text fitting within its bounding text box. In this case the font_scale is applied to the font_size and the line_spacing_reduction is applied to the line_spacing. Both properties are also reset to default values. | [optional] 
**fontScale** | **Number** | The font scale applied to the shape. For shapes with autofit_type NONE or SHAPE_AUTOFIT, this value is the default value of 1. For TEXT_AUTOFIT, this value multiplied by the font_size gives the font size that is rendered in the editor. This property is read-only. | [optional] 
**lineSpacingReduction** | **Number** | The line spacing reduction applied to the shape. For shapes with autofit_type NONE or SHAPE_AUTOFIT, this value is the default value of 0. For TEXT_AUTOFIT, this value subtracted from the line_spacing gives the line spacing that is rendered in the editor. This property is read-only. | [optional] 



## Enum: AutofitTypeEnum


* `AUTOFIT_TYPE_UNSPECIFIED` (value: `"AUTOFIT_TYPE_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `TEXT_AUTOFIT` (value: `"TEXT_AUTOFIT"`)

* `SHAPE_AUTOFIT` (value: `"SHAPE_AUTOFIT"`)




