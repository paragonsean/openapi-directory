

# Shadow

The shadow properties of a page element. If these fields are unset, they may be inherited from a parent placeholder if it exists. If there is no parent, the fields will default to the value used for new page elements created in the Slides editor, which may depend on the page element kind.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alignment** | [**AlignmentEnum**](#AlignmentEnum) | The alignment point of the shadow, that sets the origin for translate, scale and skew of the shadow. This property is read-only. |  [optional] |
|**alpha** | **Float** | The alpha of the shadow&#39;s color, from 0.0 to 1.0. |  [optional] |
|**blurRadius** | [**Dimension**](Dimension.md) |  |  [optional] |
|**color** | [**OpaqueColor**](OpaqueColor.md) |  |  [optional] |
|**propertyState** | [**PropertyStateEnum**](#PropertyStateEnum) | The shadow property state. Updating the shadow on a page element will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no shadow on a page element, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other shadow fields set in the same request will be ignored. |  [optional] |
|**rotateWithShape** | **Boolean** | Whether the shadow should rotate with the shape. This property is read-only. |  [optional] |
|**transform** | [**AffineTransform**](AffineTransform.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the shadow. This property is read-only. |  [optional] |



## Enum: AlignmentEnum

| Name | Value |
|---- | -----|
| RECTANGLE_POSITION_UNSPECIFIED | &quot;RECTANGLE_POSITION_UNSPECIFIED&quot; |
| TOP_LEFT | &quot;TOP_LEFT&quot; |
| TOP_CENTER | &quot;TOP_CENTER&quot; |
| TOP_RIGHT | &quot;TOP_RIGHT&quot; |
| LEFT_CENTER | &quot;LEFT_CENTER&quot; |
| CENTER | &quot;CENTER&quot; |
| RIGHT_CENTER | &quot;RIGHT_CENTER&quot; |
| BOTTOM_LEFT | &quot;BOTTOM_LEFT&quot; |
| BOTTOM_CENTER | &quot;BOTTOM_CENTER&quot; |
| BOTTOM_RIGHT | &quot;BOTTOM_RIGHT&quot; |



## Enum: PropertyStateEnum

| Name | Value |
|---- | -----|
| RENDERED | &quot;RENDERED&quot; |
| NOT_RENDERED | &quot;NOT_RENDERED&quot; |
| INHERIT | &quot;INHERIT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SHADOW_TYPE_UNSPECIFIED | &quot;SHADOW_TYPE_UNSPECIFIED&quot; |
| OUTER | &quot;OUTER&quot; |



