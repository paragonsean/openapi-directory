# GoogleSlidesApi.Shadow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **String** | The alignment point of the shadow, that sets the origin for translate, scale and skew of the shadow. This property is read-only. | [optional] 
**alpha** | **Number** | The alpha of the shadow&#39;s color, from 0.0 to 1.0. | [optional] 
**blurRadius** | [**Dimension**](Dimension.md) |  | [optional] 
**color** | [**OpaqueColor**](OpaqueColor.md) |  | [optional] 
**propertyState** | **String** | The shadow property state. Updating the shadow on a page element will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no shadow on a page element, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other shadow fields set in the same request will be ignored. | [optional] 
**rotateWithShape** | **Boolean** | Whether the shadow should rotate with the shape. This property is read-only. | [optional] 
**transform** | [**AffineTransform**](AffineTransform.md) |  | [optional] 
**type** | **String** | The type of the shadow. This property is read-only. | [optional] 



## Enum: AlignmentEnum


* `RECTANGLE_POSITION_UNSPECIFIED` (value: `"RECTANGLE_POSITION_UNSPECIFIED"`)

* `TOP_LEFT` (value: `"TOP_LEFT"`)

* `TOP_CENTER` (value: `"TOP_CENTER"`)

* `TOP_RIGHT` (value: `"TOP_RIGHT"`)

* `LEFT_CENTER` (value: `"LEFT_CENTER"`)

* `CENTER` (value: `"CENTER"`)

* `RIGHT_CENTER` (value: `"RIGHT_CENTER"`)

* `BOTTOM_LEFT` (value: `"BOTTOM_LEFT"`)

* `BOTTOM_CENTER` (value: `"BOTTOM_CENTER"`)

* `BOTTOM_RIGHT` (value: `"BOTTOM_RIGHT"`)





## Enum: PropertyStateEnum


* `RENDERED` (value: `"RENDERED"`)

* `NOT_RENDERED` (value: `"NOT_RENDERED"`)

* `INHERIT` (value: `"INHERIT"`)





## Enum: TypeEnum


* `SHADOW_TYPE_UNSPECIFIED` (value: `"SHADOW_TYPE_UNSPECIFIED"`)

* `OUTER` (value: `"OUTER"`)




