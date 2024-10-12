# WowzaStreamingCloudRestApiReferenceDocumentation.Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspectRatioHeight** | **Number** | The height, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is &lt;strong&gt;1080&lt;/strong&gt;. | [optional] 
**aspectRatioWidth** | **Number** | The width, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is &lt;strong&gt;1980&lt;/strong&gt;. | [optional] 
**bitrateAudio** | **Number** | The audio bitrate, in kilobits per second (Kbps). Must be between &lt;strong&gt;0&lt;/strong&gt; (for passthrough audio) and &lt;strong&gt;1000&lt;/strong&gt;. The default is &lt;strong&gt;128&lt;/strong&gt;. | [optional] 
**bitrateVideo** | **Number** | The video bitrate, in kilobits per second (Kbps). Must be between &lt;strong&gt;0&lt;/strong&gt; (for passthrough video) and &lt;strong&gt;10240&lt;/strong&gt;. The default is &lt;strong&gt;4000&lt;/strong&gt;. | [optional] 
**createdAt** | **Date** | The date and time that the output rendition was created. | [optional] 
**framerateReduction** | **String** | Reduce the frame rate of the transcoded output rendition. The default, &lt;strong&gt;0&lt;/strong&gt;, uses the encoded stream&#39;s frame rate without reduction. | [optional] 
**h264Profile** | **String** | The encoding method. Specify &lt;strong&gt;main&lt;/strong&gt; for desktop streaming, &lt;strong&gt;baseline&lt;/strong&gt; for playback on mobile devices, or &lt;strong&gt;high&lt;/strong&gt; for HD playback. The default is &lt;strong&gt;high&lt;/strong&gt;. | [optional] 
**id** | **String** | The unique alphanumeric string that identifies the output rendition. | [optional] 
**keyframes** | **String** | The interval used to define the compression applied to a group of frames. The default, &lt;strong&gt;follow_source&lt;/strong&gt;, uses the keyframe interval of the source video. | [optional] 
**name** | **String** | A descriptive name for the output (generated, not writable). | [optional] 
**outputStreamTargets** | [**[OutputStreamTarget]**](OutputStreamTarget.md) |  | [optional] 
**passthroughAudio** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, sends the audio track to the target without transcoding. The default is &lt;strong&gt;false&lt;/strong&gt;. | [optional] 
**passthroughVideo** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, sends the video track to the target without transcoding. The default is &lt;strong&gt;false&lt;/strong&gt;. | [optional] 
**streamFormat** | **String** | The contents of the stream. The default is both audio and video (&lt;strong&gt;audiovideo&lt;/strong&gt;). | [optional] 
**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder. | [optional] 
**updatedAt** | **Date** | The date and time that the output rendition was updated. | [optional] 



## Enum: FramerateReductionEnum


* `0` (value: `"0"`)

* `1/2` (value: `"1/2"`)

* `1/4` (value: `"1/4"`)

* `1/25` (value: `"1/25"`)

* `1/30` (value: `"1/30"`)

* `1/50` (value: `"1/50"`)

* `1/60` (value: `"1/60"`)





## Enum: H264ProfileEnum


* `main` (value: `"main"`)

* `baseline` (value: `"baseline"`)

* `high` (value: `"high"`)





## Enum: KeyframesEnum


* `follow_source` (value: `"follow_source"`)

* `25` (value: `"25"`)

* `30` (value: `"30"`)

* `50` (value: `"50"`)

* `60` (value: `"60"`)

* `100` (value: `"100"`)

* `120` (value: `"120"`)





## Enum: StreamFormatEnum


* `audiovideo` (value: `"audiovideo"`)

* `videoonly` (value: `"videoonly"`)

* `audioonly` (value: `"audioonly"`)




