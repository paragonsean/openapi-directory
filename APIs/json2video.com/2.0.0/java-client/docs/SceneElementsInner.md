

# SceneElementsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**src** | **URI** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**cache** | **Boolean** | Element&#39;s cache policy. When true, the cached version (if exists) is used. When false, the assets is downloaded. |  [optional] |
|**comment** | **String** | Used for adding your comments |  [optional] |
|**duration** | **Float** | Element&#39;s duration in seconds. A value of -1 auto calculates the duration based on the asset intrinsic length or the scene duration. |  [optional] |
|**extraTime** | **Float** | Element&#39;s time span added after the playback. |  [optional] |
|**fadeIn** | **Float** | Adds a fade in effect to the element. Value in seconds. |  [optional] |
|**fadeOut** | **Float** | Adds a fade out effect to the element. Value in seconds. |  [optional] |
|**start** | **Float** | Element&#39;s starting time in seconds relative to the container scene or the movie if the element is in the Movie&#39;s elements array. |  [optional] |
|**zIndex** | **BigDecimal** | Element&#39;s z-index. Use this property to reorganize the layering of the elements like in HTML |  [optional] |
|**chromaKey** | [**VisualElementChromaKey**](VisualElementChromaKey.md) |  |  [optional] |
|**crop** | [**VisualElementCrop**](VisualElementCrop.md) |  |  [optional] |
|**pan** | [**PanEnum**](#PanEnum) | Pans the element to the specified direction. If &lt;code&gt;zoom&lt;/code&gt; property is not specified, the effect is a non-zooming pan |  [optional] |
|**position** | [**PositionEnum**](#PositionEnum) | Sets the element position in the scene. A value of &#39;custom&#39; sets a custom position based on the provided &#39;x&#39; and &#39;y&#39; properties |  [optional] |
|**rotate** | [**VisualElementRotate**](VisualElementRotate.md) |  |  [optional] |
|**scale** | [**VisualElementScale**](VisualElementScale.md) |  |  [optional] |
|**x** | **BigDecimal** | Sets the horizontal position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the left side |  [optional] |
|**y** | **BigDecimal** | Sets the vertical position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the top side |  [optional] |
|**zoom** | **Integer** | Zooms the element with the specified level percentage. Positive values zoom in, negative values zoom out, zero does not zoom. Zoom can be combined with the &lt;code&gt;pan&lt;/code&gt; property to set the focus point of the zooming |  [optional] |
|**loop** | **Integer** | Sets the number of loops the video to play. Use -1 for an infinite loop. The default value of 1 plays the video just once. |  [optional] |
|**muted** | **Boolean** | Mutes the audio |  [optional] |
|**volume** | **BigDecimal** |  |  [optional] |
|**height** | **Integer** | Desired text element height, but can be overriden by the component defaults. A value of &lt;code&gt;-1&lt;/code&gt; means inherits scenes or movie height |  [optional] |
|**settings** | **Object** | Settings to be passed to the component |  [optional] |
|**style** | **String** | Style of the text element. Check all available text style at &lt;a href&#x3D;&#39;https://json2video.com/docs/resources/text/&#39;&gt;https://json2video.com/resources/text/&lt;/a&gt; |  [optional] |
|**text** | **String** | The sentence or sentences to be converted to voice audio |  |
|**width** | **Integer** | Desired text element width, but can be overriden by the component defaults. A value of &lt;code&gt;-1&lt;/code&gt; means inherits scenes or movie width |  [optional] |
|**html** | **String** | HTML snippet to render. Compatible with HTML5, CSS3 and Javascript |  |
|**tailwindcss** | **Boolean** | Enables usage of TailwindCSS for the HTML snippet |  [optional] |
|**component** | **String** | ID of the Component element. Check all available components in the &lt;a href&#x3D;&#39;https://json2video.com/docs/resources/basic/&#39;&gt;library&lt;/a&gt; |  |
|**voice** | **String** | The voice name to be used. Check &lt;a href&#x3D;\&quot;/docs/tutorial/voice-elements/\&quot;&gt;available voices&lt;/a&gt;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VIDEO | &quot;video&quot; |
| IMAGE | &quot;image&quot; |
| TEXT | &quot;text&quot; |
| HTML | &quot;html&quot; |
| COMPONENT | &quot;component&quot; |
| AUDIO | &quot;audio&quot; |
| VOICE | &quot;voice&quot; |



## Enum: PanEnum

| Name | Value |
|---- | -----|
| LEFT | &quot;left&quot; |
| TOP | &quot;top&quot; |
| RIGHT | &quot;right&quot; |
| BOTTOM | &quot;bottom&quot; |
| TOP_LEFT | &quot;top-left&quot; |
| TOP_RIGHT | &quot;top-right&quot; |
| BOTTOM_LEFT | &quot;bottom-left&quot; |
| BOTTOM_RIGHT | &quot;bottom-right&quot; |



## Enum: PositionEnum

| Name | Value |
|---- | -----|
| TOP_LEFT | &quot;top-left&quot; |
| TOP_RIGHT | &quot;top-right&quot; |
| BOTTOM_RIGHT | &quot;bottom-right&quot; |
| BOTTOM_LEFT | &quot;bottom-left&quot; |
| CENTER_CENTER | &quot;center-center&quot; |
| CUSTOM | &quot;custom&quot; |



