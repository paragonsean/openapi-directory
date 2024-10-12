

# Output1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspectRatioHeight** | **Integer** | The height, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is &lt;strong&gt;1080&lt;/strong&gt;. |  [optional] |
|**aspectRatioWidth** | **Integer** | The width, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is &lt;strong&gt;1980&lt;/strong&gt;. |  [optional] |
|**bitrateAudio** | **Integer** | The audio bitrate, in kilobits per second (Kbps). Must be between &lt;strong&gt;0&lt;/strong&gt; (for passthrough audio) and &lt;strong&gt;1000&lt;/strong&gt;. The default is &lt;strong&gt;128&lt;/strong&gt;. |  [optional] |
|**bitrateVideo** | **Integer** | The video bitrate, in kilobits per second (Kbps). Must be between &lt;strong&gt;0&lt;/strong&gt; (for passthrough video) and &lt;strong&gt;10240&lt;/strong&gt;. The default is &lt;strong&gt;4000&lt;/strong&gt;. |  [optional] |
|**framerateReduction** | [**FramerateReductionEnum**](#FramerateReductionEnum) | Reduce the frame rate of the transcoded output rendition. The default, &lt;strong&gt;0&lt;/strong&gt;, uses the encoded stream&#39;s frame rate without reduction. |  [optional] |
|**h264Profile** | [**H264ProfileEnum**](#H264ProfileEnum) | The encoding method. Specify &lt;strong&gt;main&lt;/strong&gt; for desktop streaming, &lt;strong&gt;baseline&lt;/strong&gt; for playback on mobile devices, or &lt;strong&gt;high&lt;/strong&gt; for HD playback. The default is &lt;strong&gt;high&lt;/strong&gt;. |  [optional] |
|**keyframes** | [**KeyframesEnum**](#KeyframesEnum) | The interval used to define the compression applied to a group of frames. The default, &lt;strong&gt;follow_source&lt;/strong&gt;, uses the keyframe interval of the source video. |  [optional] |
|**passthroughAudio** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, sends the audio track to the target without transcoding. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**passthroughVideo** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, sends the video track to the target without transcoding. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**streamFormat** | [**StreamFormatEnum**](#StreamFormatEnum) | The contents of the stream. The default is both audio and video (&lt;strong&gt;audiovideo&lt;/strong&gt;). |  |



## Enum: FramerateReductionEnum

| Name | Value |
|---- | -----|
| _0 | &quot;0&quot; |
| _1_2 | &quot;1/2&quot; |
| _1_4 | &quot;1/4&quot; |
| _1_25 | &quot;1/25&quot; |
| _1_30 | &quot;1/30&quot; |
| _1_50 | &quot;1/50&quot; |
| _1_60 | &quot;1/60&quot; |



## Enum: H264ProfileEnum

| Name | Value |
|---- | -----|
| MAIN | &quot;main&quot; |
| BASELINE | &quot;baseline&quot; |
| HIGH | &quot;high&quot; |



## Enum: KeyframesEnum

| Name | Value |
|---- | -----|
| FOLLOW_SOURCE | &quot;follow_source&quot; |
| _25 | &quot;25&quot; |
| _30 | &quot;30&quot; |
| _50 | &quot;50&quot; |
| _60 | &quot;60&quot; |
| _100 | &quot;100&quot; |
| _120 | &quot;120&quot; |



## Enum: StreamFormatEnum

| Name | Value |
|---- | -----|
| AUDIOVIDEO | &quot;audiovideo&quot; |
| VIDEOONLY | &quot;videoonly&quot; |
| AUDIOONLY | &quot;audioonly&quot; |



