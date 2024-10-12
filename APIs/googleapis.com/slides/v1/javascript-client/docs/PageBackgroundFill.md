# GoogleSlidesApi.PageBackgroundFill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**propertyState** | **String** | The background fill property state. Updating the fill on a page will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no fill on a page, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other fill fields set in the same request will be ignored. | [optional] 
**solidFill** | [**SolidFill**](SolidFill.md) |  | [optional] 
**stretchedPictureFill** | [**StretchedPictureFill**](StretchedPictureFill.md) |  | [optional] 



## Enum: PropertyStateEnum


* `RENDERED` (value: `"RENDERED"`)

* `NOT_RENDERED` (value: `"NOT_RENDERED"`)

* `INHERIT` (value: `"INHERIT"`)




