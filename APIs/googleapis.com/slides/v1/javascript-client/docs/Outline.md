# GoogleSlidesApi.Outline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashStyle** | **String** | The dash style of the outline. | [optional] 
**outlineFill** | [**OutlineFill**](OutlineFill.md) |  | [optional] 
**propertyState** | **String** | The outline property state. Updating the outline on a page element will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no outline on a page element, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other outline fields set in the same request will be ignored. | [optional] 
**weight** | [**Dimension**](Dimension.md) |  | [optional] 



## Enum: DashStyleEnum


* `DASH_STYLE_UNSPECIFIED` (value: `"DASH_STYLE_UNSPECIFIED"`)

* `SOLID` (value: `"SOLID"`)

* `DOT` (value: `"DOT"`)

* `DASH` (value: `"DASH"`)

* `DASH_DOT` (value: `"DASH_DOT"`)

* `LONG_DASH` (value: `"LONG_DASH"`)

* `LONG_DASH_DOT` (value: `"LONG_DASH_DOT"`)





## Enum: PropertyStateEnum


* `RENDERED` (value: `"RENDERED"`)

* `NOT_RENDERED` (value: `"NOT_RENDERED"`)

* `INHERIT` (value: `"INHERIT"`)




