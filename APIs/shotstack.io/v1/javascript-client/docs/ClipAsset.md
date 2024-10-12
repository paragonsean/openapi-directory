# Shotstack.ClipAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crop** | [**Crop**](Crop.md) |  | [optional] 
**src** | **String** | The luma matte source URL. The URL must be publicly accessible or include credentials. | 
**trim** | **Number** | The start trim point of the luma matte clip, in seconds (defaults to 0). Videos will start from the in trim point. A luma matte video will play until the file ends or the Clip length is reached. | [optional] 
**type** | **String** | The type of asset - set to &#x60;luma&#x60; for luma mattes. | [default to &#39;luma&#39;]
**volume** | **Number** | Set the volume for the audio clip between 0 and 1 where 0 is muted and 1 is full volume (defaults to 1). | [optional] [default to 1]
**background** | **String** | Apply a background color behind the HTML bounding box using. Set the text color using hexadecimal  color notation. Transparency is supported by setting the first two characters of the hex string  (opposite to HTML), i.e. #80ffffff will be white with 50% transparency. | [optional] [default to &#39;transparent&#39;]
**color** | **String** | Set the text color using hexadecimal color notation. Transparency is supported by setting the first two characters of the hex string (opposite to HTML),  i.e. #80ffffff will be white with  50% transparency. | [optional] [default to &#39;#ffffff&#39;]
**offset** | [**Offset**](Offset.md) |  | [optional] 
**position** | **String** | Place the HTML in one of nine predefined positions within the HTML area. &lt;ul&gt;   &lt;li&gt;&#x60;top&#x60; - top (center)&lt;/li&gt;   &lt;li&gt;&#x60;topRight&#x60; - top right&lt;/li&gt;   &lt;li&gt;&#x60;right&#x60; - right (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomRight&#x60; - bottom right&lt;/li&gt;   &lt;li&gt;&#x60;bottom&#x60; - bottom (center)&lt;/li&gt;   &lt;li&gt;&#x60;bottomLeft&#x60; - bottom left&lt;/li&gt;   &lt;li&gt;&#x60;left&#x60; - left (center)&lt;/li&gt;   &lt;li&gt;&#x60;topLeft&#x60; - top left&lt;/li&gt;   &lt;li&gt;&#x60;center&#x60; - center&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;center&#39;]
**size** | **String** | Set the relative size of the text using predefined sizes from xx-small to xx-large. &lt;ul&gt;   &lt;li&gt;&#x60;xx-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;small&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;medium&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;x-large&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;xx-large&#x60;&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;medium&#39;]
**style** | **String** | Uses a preset to apply font properties and styling to the title. &lt;ul&gt;   &lt;li&gt;&#x60;minimal&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;blockbuster&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;vogue&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;sketchy&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;skinny&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunk&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;chunkLight&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;marker&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;future&#x60;&lt;/li&gt;   &lt;li&gt;&#x60;subtitle&#x60;&lt;/li&gt; &lt;/ul&gt; | [optional] 
**text** | **String** | The title text string - i.e. \&quot;My Title\&quot;. | 
**css** | **String** | The CSS text string to apply styling to the HTML. See list of  [support CSS properties](https://shotstack.gitbook.io/docs/guides/architecting-an-application/html-support#supported-html-tags). | [optional] 
**height** | **Number** | Set the width of the HTML asset bounding box in pixels. Text and elements will be masked if they exceed the  height of the bounding box. | [optional] 
**html** | **String** | The HTML text string. See list of [supported HTML tags](https://shotstack.gitbook.io/docs/guides/architecting-an-application/html-support#supported-html-tags). | 
**width** | **Number** | Set the width of the HTML asset bounding box in pixels. Text will wrap to fill the bounding box. | [optional] 
**effect** | **String** | The effect to apply to the audio asset &lt;ul&gt;   &lt;li&gt;&#x60;fadeIn&#x60; - fade volume in only&lt;/li&gt;   &lt;li&gt;&#x60;fadeOut&#x60; - fade volume out only&lt;/li&gt;   &lt;li&gt;&#x60;fadeInFadeOut&#x60; - fade volume in and out&lt;/li&gt; &lt;/ul&gt; | [optional] 



## Enum: PositionEnum


* `top` (value: `"top"`)

* `topRight` (value: `"topRight"`)

* `right` (value: `"right"`)

* `bottomRight` (value: `"bottomRight"`)

* `bottom` (value: `"bottom"`)

* `bottomLeft` (value: `"bottomLeft"`)

* `left` (value: `"left"`)

* `topLeft` (value: `"topLeft"`)

* `center` (value: `"center"`)





## Enum: SizeEnum


* `xx-small` (value: `"xx-small"`)

* `x-small` (value: `"x-small"`)

* `small` (value: `"small"`)

* `medium` (value: `"medium"`)

* `large` (value: `"large"`)

* `x-large` (value: `"x-large"`)

* `xx-large` (value: `"xx-large"`)





## Enum: StyleEnum


* `minimal` (value: `"minimal"`)

* `blockbuster` (value: `"blockbuster"`)

* `vogue` (value: `"vogue"`)

* `sketchy` (value: `"sketchy"`)

* `skinny` (value: `"skinny"`)

* `chunk` (value: `"chunk"`)

* `chunkLight` (value: `"chunkLight"`)

* `marker` (value: `"marker"`)

* `future` (value: `"future"`)

* `subtitle` (value: `"subtitle"`)





## Enum: EffectEnum


* `fadeIn` (value: `"fadeIn"`)

* `fadeOut` (value: `"fadeOut"`)

* `fadeInFadeOut` (value: `"fadeInFadeOut"`)




