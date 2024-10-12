

# Image


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chromaKey** | [**VisualElementChromaKey**](VisualElementChromaKey.md) |  |  [optional] |
|**crop** | [**VisualElementCrop**](VisualElementCrop.md) |  |  [optional] |
|**pan** | [**PanEnum**](#PanEnum) | Pans the element to the specified direction. If &lt;code&gt;zoom&lt;/code&gt; property is not specified, the effect is a non-zooming pan |  [optional] |
|**position** | [**PositionEnum**](#PositionEnum) | Sets the element position in the scene. A value of &#39;custom&#39; sets a custom position based on the provided &#39;x&#39; and &#39;y&#39; properties |  [optional] |
|**rotate** | [**VisualElementRotate**](VisualElementRotate.md) |  |  [optional] |
|**scale** | [**VisualElementScale**](VisualElementScale.md) |  |  [optional] |
|**x** | **BigDecimal** | Sets the horizontal position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the left side |  [optional] |
|**y** | **BigDecimal** | Sets the vertical position of the element in the scene. The value &lt;code&gt;0&lt;/code&gt; is on the top side |  [optional] |
|**zoom** | **Integer** | Zooms the element with the specified level percentage. Positive values zoom in, negative values zoom out, zero does not zoom. Zoom can be combined with the &lt;code&gt;pan&lt;/code&gt; property to set the focus point of the zooming |  [optional] |
|**src** | **URI** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |



