

# Output

The output format, render range and type of media to generate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspectRatio** | [**AspectRatioEnum**](#AspectRatioEnum) | The aspect ratio (shape) of the video or image. Useful for social media output formats. Options are: &lt;ul&gt;   &lt;li&gt;&#x60;16:9&#x60; - regular landscape/horizontal aspect ratio (default)&lt;/li&gt;   &lt;li&gt;&#x60;9:16&#x60; - vertical/portrait aspect ratio&lt;/li&gt;   &lt;li&gt;&#x60;1:1&#x60; - square aspect ratio&lt;/li&gt;   &lt;li&gt;&#x60;4:5&#x60; - short vertical/portrait aspect ratio&lt;/li&gt;   &lt;li&gt;&#x60;4:3&#x60; - legacy TV aspect ratio&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**destinations** | [**List&lt;OutputDestinationsInner&gt;**](OutputDestinationsInner.md) | A destination is a location where output files can be sent to for serving or hosting. By default all rendered assets are automatically sent to the Shotstack hosting destination. [DestinationShotstack](/#tocs_shotstackdestination) is currently the only option with plans to add more in the future such as S3, YouTube, Vimeo and Mux. If you do not require hosting you can opt-out using the  &#x60;exclude&#x60; property. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The output format and type of media file to generate. &lt;ul&gt;   &lt;li&gt;&#x60;mp4&#x60; - mp4 video file&lt;/li&gt;   &lt;li&gt;&#x60;gif&#x60; - animated gif&lt;/li&gt;   &lt;li&gt;&#x60;jpg&#x60; - jpg image file&lt;/li&gt;   &lt;li&gt;&#x60;png&#x60; - png image file&lt;/li&gt;   &lt;li&gt;&#x60;bmp&#x60; - bmp image file&lt;/li&gt;   &lt;li&gt;&#x60;mp3&#x60; - mp3 audio file (audio only)&lt;/li&gt; &lt;/ul&gt; |  |
|**fps** | [**FpsEnum**](#FpsEnum) | Override the default frames per second. Useful for when the source footage is recorded at 30fps, i.e. on  mobile devices. Lower frame rates can be used to add cinematic quality (24fps) or to create smaller file size/faster render times or animated gifs (12 or 15fps). Default is 25fps. &lt;ul&gt;   &lt;li&gt;&#x60;12&#x60; - 12fps&lt;/li&gt;   &lt;li&gt;&#x60;15&#x60; - 15fps&lt;/li&gt;   &lt;li&gt;&#x60;24&#x60; - 24fps&lt;/li&gt;   &lt;li&gt;&#x60;25&#x60; - 25fps&lt;/li&gt;   &lt;li&gt;&#x60;30&#x60; - 30fps&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**poster** | [**Poster**](Poster.md) |  |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Adjust the output quality of the video, image or audio. Adjusting quality affects  render speed, download speeds and storage requirements due to file size. The default &#x60;medium&#x60; provides the most optimized choice for all three  factors. &lt;ul&gt;   &lt;li&gt;&#x60;low&#x60; - slightly reduced quality, smaller file size&lt;/li&gt;   &lt;li&gt;&#x60;medium&#x60; - optimized quality, render speeds and file size&lt;/li&gt;   &lt;li&gt;&#x60;high&#x60; - slightly increased quality, larger file size&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**range** | [**Range**](Range.md) |  |  [optional] |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | The output resolution of the video or image. &lt;ul&gt;   &lt;li&gt;&#x60;preview&#x60; - 512px x 288px @ 15fps&lt;/li&gt;   &lt;li&gt;&#x60;mobile&#x60; - 640px x 360px @ 25fps&lt;/li&gt;   &lt;li&gt;&#x60;sd&#x60; - 1024px x 576px @ 25fps&lt;/li&gt;   &lt;li&gt;&#x60;hd&#x60; - 1280px x 720px @ 25fps&lt;/li&gt;   &lt;li&gt;&#x60;1080&#x60; - 1920px x 1080px @ 25fps&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**scaleTo** | [**ScaleToEnum**](#ScaleToEnum) | Override the resolution and scale the video or image to render at a different size. When using scaleTo the asset should be edited at the resolution dimensions, i.e. use font sizes that look best at HD, then use scaleTo to output the file at SD and the text will be scaled to the correct size. This is useful if you want to create multiple asset sizes. &lt;ul&gt;   &lt;li&gt;&#x60;preview&#x60; - 512px x 288px @ 15fps&lt;/li&gt;   &lt;li&gt;&#x60;mobile&#x60; - 640px x 360px @ 25fps&lt;/li&gt;   &lt;li&gt;&#x60;sd&#x60; - 1024px x 576px @25fps&lt;/li&gt;   &lt;li&gt;&#x60;hd&#x60; - 1280px x 720px @25fps&lt;/li&gt;   &lt;li&gt;&#x60;1080&#x60; - 1920px x 1080px @25fps&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**size** | [**Size**](Size.md) |  |  [optional] |
|**thumbnail** | [**Thumbnail**](Thumbnail.md) |  |  [optional] |



## Enum: AspectRatioEnum

| Name | Value |
|---- | -----|
| _969 | &quot;969&quot; |
| _556 | &quot;556&quot; |
| _61 | &quot;61&quot; |
| _245 | &quot;245&quot; |
| _243 | &quot;243&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| MP4 | &quot;mp4&quot; |
| GIF | &quot;gif&quot; |
| MP3 | &quot;mp3&quot; |
| JPG | &quot;jpg&quot; |
| PNG | &quot;png&quot; |
| BMP | &quot;bmp&quot; |



## Enum: FpsEnum

| Name | Value |
|---- | -----|
| NUMBER_12 | 12 |
| NUMBER_15 | 15 |
| NUMBER_24 | 24 |
| NUMBER_25 | 25 |
| NUMBER_30 | 30 |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| HIGH | &quot;high&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| PREVIEW | &quot;preview&quot; |
| MOBILE | &quot;mobile&quot; |
| SD | &quot;sd&quot; |
| HD | &quot;hd&quot; |
| _1080 | &quot;1080&quot; |



## Enum: ScaleToEnum

| Name | Value |
|---- | -----|
| PREVIEW | &quot;preview&quot; |
| MOBILE | &quot;mobile&quot; |
| SD | &quot;sd&quot; |
| HD | &quot;hd&quot; |
| _1080 | &quot;1080&quot; |



