# Json2VideoApi.Video

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
**muted** | **Boolean** | Mutes the audio | [optional] [default to false]
**volume** | **Number** |  | [optional] [default to 5]
**src** | **String** | URL to the asset file. Videos can be in MP4, MKV, MOV but MP4 is recommended. | [optional] 
**type** | **String** |  | 
**loop** | **Number** | Sets the number of loops the video to play. Use -1 for an infinite loop. The default value of 1 plays the video just once. | [optional] 



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


* `video` (value: `"video"`)




