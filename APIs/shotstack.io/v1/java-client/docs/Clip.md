

# Clip

A clip is a container for a specific type of asset, i.e. a title, image, video, audio or html. You use a Clip to define when an asset will display on the timeline, how long it will play for and transitions, filters and effects to apply to it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | [**ClipAsset**](ClipAsset.md) |  |  |
|**effect** | [**EffectEnum**](#EffectEnum) | A motion effect to apply to the Clip. &lt;ul&gt;   &lt;li&gt;&#x60;zoomIn&#x60; - slow zoom in&lt;/li&gt;   &lt;li&gt;&#x60;zoomOut&#x60; - slow zoom out&lt;/li&gt;   &lt;li&gt;&#x60;slideLeft&#x60; - slow slide (pan) left&lt;/li&gt;   &lt;li&gt;&#x60;slideRight&#x60; - slow slide (pan) right&lt;/li&gt;   &lt;li&gt;&#x60;slideUp&#x60; - slow slide (pan) up&lt;/li&gt;   &lt;li&gt;&#x60;slideDown&#x60; - slow slide (pan) down&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**filter** | [**FilterEnum**](#FilterEnum) | A filter effect to apply to the Clip. &lt;ul&gt;   &lt;li&gt;&#x60;boost&#x60; - boost contrast and saturation&lt;/li&gt;   &lt;li&gt;&#x60;contrast&#x60; - increase contrast&lt;/li&gt;   &lt;li&gt;&#x60;darken&#x60; - darken the scene&lt;/li&gt;   &lt;li&gt;&#x60;greyscale&#x60; - remove colour&lt;/li&gt;   &lt;li&gt;&#x60;lighten&#x60; - lighten the scene&lt;/li&gt;   &lt;li&gt;&#x60;muted&#x60; - reduce saturation and contrast&lt;/li&gt;   &lt;li&gt;&#x60;invert&#x60; - invert colors&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**fit** | [**FitEnum**](#FitEnum) | Set how the asset should be scaled to fit the viewport using one of the following options:    &lt;ul&gt;     &lt;li&gt;&#x60;cover&#x60; - stretch the asset to fill the viewport without maintaining the aspect ratio.&lt;/li&gt;     &lt;li&gt;&#x60;contain&#x60; - fit the entire asset within the viewport while maintaining the original aspect ratio.&lt;/li&gt;     &lt;li&gt;&#x60;crop&#x60; - scale the asset to fill the viewport while maintaining the aspect ratio. The asset will be cropped if it exceeds the bounds of the viewport.&lt;/li&gt;     &lt;li&gt;&#x60;none&#x60; - preserves the original asset dimensions and does not apply any scaling.&lt;/li&gt;   &lt;/ul&gt; |  [optional] |
|**length** | **BigDecimal** | The length, in seconds, the Clip should play for. |  |
|**offset** | [**Offset**](Offset.md) |  |  [optional] |
|**opacity** | **BigDecimal** | Sets the opacity of the Clip where 1 is opaque and 0 is transparent. |  [optional] |
|**position** | [**PositionEnum**](#PositionEnum) | Place the asset in one of nine predefined positions of the viewport. This is most effective for when the asset is scaled and you want to position the element to a specific position. &lt;ul&gt;   &lt;li&gt;&#x60;top&#x60; - top (center)&lt;/li&gt;   &lt;li&gt;&#x60;topRight&#x60; - top right&lt;/li&gt;   &lt;li&gt;&#x60;right&#x60; - right (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomRight&#x60; - bottom right&lt;/li&gt;   &lt;li&gt;&#x60;bottom&#x60; - bottom (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomLeft&#x60; - bottom left&lt;/li&gt;   &lt;li&gt;&#x60;left&#x60; - left (center)&lt;/li&gt;   &lt;li&gt;&#x60;topLeft&#x60; - top left&lt;/li&gt;   &lt;li&gt;&#x60;center&#x60; - center&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**scale** | **BigDecimal** | Scale the asset to a fraction of the viewport size - i.e. setting the scale to 0.5 will scale asset to half the size of the viewport. This is useful for picture-in-picture video and  scaling images such as logos and watermarks. |  [optional] |
|**start** | **BigDecimal** | The start position of the Clip on the timeline, in seconds. |  |
|**transition** | [**Transition**](Transition.md) |  |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| ZOOM_IN | &quot;zoomIn&quot; |
| ZOOM_OUT | &quot;zoomOut&quot; |
| SLIDE_LEFT | &quot;slideLeft&quot; |
| SLIDE_RIGHT | &quot;slideRight&quot; |
| SLIDE_UP | &quot;slideUp&quot; |
| SLIDE_DOWN | &quot;slideDown&quot; |



## Enum: FilterEnum

| Name | Value |
|---- | -----|
| BOOST | &quot;boost&quot; |
| CONTRAST | &quot;contrast&quot; |
| DARKEN | &quot;darken&quot; |
| GREYSCALE | &quot;greyscale&quot; |
| LIGHTEN | &quot;lighten&quot; |
| MUTED | &quot;muted&quot; |
| NEGATIVE | &quot;negative&quot; |



## Enum: FitEnum

| Name | Value |
|---- | -----|
| COVER | &quot;cover&quot; |
| CONTAIN | &quot;contain&quot; |
| CROP | &quot;crop&quot; |
| NONE | &quot;none&quot; |



## Enum: PositionEnum

| Name | Value |
|---- | -----|
| TOP | &quot;top&quot; |
| TOP_RIGHT | &quot;topRight&quot; |
| RIGHT | &quot;right&quot; |
| BOTTOM_RIGHT | &quot;bottomRight&quot; |
| BOTTOM | &quot;bottom&quot; |
| BOTTOM_LEFT | &quot;bottomLeft&quot; |
| LEFT | &quot;left&quot; |
| TOP_LEFT | &quot;topLeft&quot; |
| CENTER | &quot;center&quot; |



