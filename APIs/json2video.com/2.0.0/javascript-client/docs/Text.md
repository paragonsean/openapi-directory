# Json2VideoApi.Text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **Boolean** | Element&#39;s cache policy. When true, the cached version (if exists) is used. When false, the assets is downloaded. | [optional] [default to true]
**comment** | **String** | Used for adding your comments | [optional] 
**duration** | **Number** | Element&#39;s duration in seconds. A value of -1 auto calculates the duration based on the asset intrinsic length or the scene duration. | [optional] [default to -1]
**extraTime** | **Number** | Element&#39;s time span added after the playback. | [optional] [default to 0]
**fadeIn** | **Number** | Adds a fade in effect to the element. Value in seconds. | [optional] 
**fadeOut** | **Number** | Adds a fade out effect to the element. Value in seconds. | [optional] 
**start** | **Number** | Element&#39;s starting time in seconds relative to the container scene or the movie if the element is in the Movie&#39;s elements array. | [optional] [default to 0]
**zIndex** | **Number** | Element&#39;s z-index. Use this property to reorganize the layering of the elements like in HTML | [optional] [default to 0]
**chromaKey** | [**VisualElementChromaKey**](VisualElementChromaKey.md) |  | [optional] 
**crop** | [**VisualElementCrop**](VisualElementCrop.md) |  | [optional] 
**pan** | **String** | Pans the element to the specified direction. If &lt;code&gt;zoom&lt;/code&gt; property is not specified, the effect is a non-zooming pan | [optional] 
**position** | **String** | Sets the element position in the scene. A value of &#39;custom&#39; sets a custom position based on the provided &#39;x&#39; and &#39;y&#39; properties | [optional] [default to &#39;custom&#39;]
**rotate** | [**VisualElementRotate**](VisualElementRotate.md) |  | [optional] 
**scale** | [**VisualElementScale**](VisualElementScale.md) |  | [optional] 
**x** | **Number** | Sets the horizontal position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the left side | [optional] [default to 0]
**y** | **Number** | Sets the vertical position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the top side | [optional] [default to 0]
**zoom** | **Number** | Zooms the element with the specified level percentage. Positive values zoom in, negative values zoom out, zero does not zoom. Zoom can be combined with the &lt;code&gt;pan&lt;/code&gt; property to set the focus point of the zooming | [optional] 
**height** | **Number** | Desired text element height, but can be overriden by the style defaults. A value of &lt;code&gt;-1&lt;/code&gt; means inherits scenes or movie height | [optional] [default to -1]
**settings** | **Object** | Text formatting settings. In general, these are CSS properties such as &lt;code&gt;font-size&lt;/code&gt;, &lt;code&gt;colour&lt;/code&gt; or &lt;code&gt;font-weight&lt;/code&gt;. See the styles to confirm which properties are available. | [optional] 
**style** | **String** | Style of the text element. Check all available text style at &lt;a href&#x3D;&#39;https://json2video.com/docs/resources/text/&#39;&gt;https://json2video.com/resources/text/&lt;/a&gt; | [optional] [default to &#39;001&#39;]
**text** | **String** | Text to be printed. The text string does not accept HTML formatting. | 
**type** | **String** |  | 
**width** | **Number** | Desired text element width, but can be overriden by the style defaults. A value of &lt;code&gt;-1&lt;/code&gt; means inherits scenes or movie width | [optional] [default to -1]



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


* `text` (value: `"text"`)




