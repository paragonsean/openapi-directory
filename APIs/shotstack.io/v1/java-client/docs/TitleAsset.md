

# TitleAsset

The TitleAsset clip type lets you create video titles from a text string and apply styling and positioning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**background** | **String** | Apply a background color behind the text. Set the text color using hexadecimal color notation. Transparency is supported by setting the first two characters of the hex string (opposite to HTML),  i.e. #80ffffff will be white with 50% transparency. Omit to use transparent background. |  [optional] |
|**color** | **String** | Set the text color using hexadecimal color notation. Transparency is supported by setting the first two characters of the hex string (opposite to HTML),  i.e. #80ffffff will be white with  50% transparency. |  [optional] |
|**offset** | [**Offset**](Offset.md) |  |  [optional] |
|**position** | [**PositionEnum**](#PositionEnum) | Place the title in one of nine predefined positions of the viewport. &lt;ul&gt;   &lt;li&gt;&#x60;top&#x60; - top (center)&lt;/li&gt;   &lt;li&gt;&#x60;topRight&#x60; - top right&lt;/li&gt;   &lt;li&gt;&#x60;right&#x60; - right (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomRight&#x60; - bottom right&lt;/li&gt;   &lt;li&gt;&#x60;bottom&#x60; - bottom (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomLeft&#x60; - bottom left&lt;/li&gt;   &lt;li&gt;&#x60;left&#x60; - left (center)&lt;/li&gt;   &lt;li&gt;&#x60;topLeft&#x60; - top left&lt;/li&gt;   &lt;li&gt;&#x60;center&#x60; - center&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | Set the relative size of the text using predefined sizes from xx-small to xx-large. &lt;ul&gt;   &lt;li&gt;&#x60;xx-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;medium&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;xx-large&#x60;&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**style** | [**StyleEnum**](#StyleEnum) | Uses a preset to apply font properties and styling to the title. &lt;ul&gt;   &lt;li&gt;&#x60;minimal&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;blockbuster&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;vogue&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;sketchy&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;skinny&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunk&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunkLight&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;marker&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;future&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;subtitle&#x60;&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**text** | **String** | The title text string - i.e. \&quot;My Title\&quot;. |  |
|**type** | **String** | The type of asset - set to &#x60;title&#x60; for titles. |  |



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



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| XX_SMALL | &quot;xx-small&quot; |
| X_SMALL | &quot;x-small&quot; |
| SMALL | &quot;small&quot; |
| MEDIUM | &quot;medium&quot; |
| LARGE | &quot;large&quot; |
| X_LARGE | &quot;x-large&quot; |
| XX_LARGE | &quot;xx-large&quot; |



## Enum: StyleEnum

| Name | Value |
|---- | -----|
| MINIMAL | &quot;minimal&quot; |
| BLOCKBUSTER | &quot;blockbuster&quot; |
| VOGUE | &quot;vogue&quot; |
| SKETCHY | &quot;sketchy&quot; |
| SKINNY | &quot;skinny&quot; |
| CHUNK | &quot;chunk&quot; |
| CHUNK_LIGHT | &quot;chunkLight&quot; |
| MARKER | &quot;marker&quot; |
| FUTURE | &quot;future&quot; |
| SUBTITLE | &quot;subtitle&quot; |



