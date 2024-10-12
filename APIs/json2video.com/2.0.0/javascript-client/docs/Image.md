# Json2VideoApi.Image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromaKey** | [**VisualElementChromaKey**](VisualElementChromaKey.md) |  | [optional] 
**crop** | [**VisualElementCrop**](VisualElementCrop.md) |  | [optional] 
**pan** | **String** | Pans the element to the specified direction. If &lt;code&gt;zoom&lt;/code&gt; property is not specified, the effect is a non-zooming pan | [optional] 
**position** | **String** | Sets the element position in the scene. A value of &#39;custom&#39; sets a custom position based on the provided &#39;x&#39; and &#39;y&#39; properties | [optional] [default to &#39;custom&#39;]
**rotate** | [**VisualElementRotate**](VisualElementRotate.md) |  | [optional] 
**scale** | [**VisualElementScale**](VisualElementScale.md) |  | [optional] 
**x** | **Number** | Sets the horizontal position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the left side | [optional] [default to 0]
**y** | **Number** | Sets the vertical position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the top side | [optional] [default to 0]
**zoom** | **Number** | Zooms the element with the specified level percentage. Positive values zoom in, negative values zoom out, zero does not zoom. Zoom can be combined with the &lt;code&gt;pan&lt;/code&gt; property to set the focus point of the zooming | [optional] 
**src** | **String** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: PanEnum


* `left` (value: `"left"`)

* `top` (value: `"top"`)

* `right` (value: `"right"`)

* `bottom` (value: `"bottom"`)

* `top-left` (value: `"top-left"`)

* `top-right` (value: `"top-right"`)

* `bottom-left` (value: `"bottom-left"`)

* `bottom-right` (value: `"bottom-right"`)





## Enum: PositionEnum


* `top-left` (value: `"top-left"`)

* `top-right` (value: `"top-right"`)

* `bottom-right` (value: `"bottom-right"`)

* `bottom-left` (value: `"bottom-left"`)

* `center-center` (value: `"center-center"`)

* `custom` (value: `"custom"`)





## Enum: TypeEnum


* `image` (value: `"image"`)




