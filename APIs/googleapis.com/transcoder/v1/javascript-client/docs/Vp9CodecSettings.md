# TranscoderApi.Vp9CodecSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitrateBps** | **Number** | Required. The video bitrate in bits per second. The minimum value is 1,000. The maximum value is 480,000,000. | [optional] 
**crfLevel** | **Number** | Target CRF level. Must be between 10 and 36, where 10 is the highest quality and 36 is the most efficient compression. The default is 21. **Note:** This field is not supported. | [optional] 
**frameRate** | **Number** | Required. The target video frame rate in frames per second (FPS). Must be less than or equal to 120. | [optional] 
**frameRateConversionStrategy** | **String** | Optional. Frame rate conversion strategy for desired frame rate. The default is &#x60;DOWNSAMPLE&#x60;. | [optional] 
**gopDuration** | **String** | Select the GOP size based on the specified duration. The default is &#x60;3s&#x60;. Note that &#x60;gopDuration&#x60; must be less than or equal to [&#x60;segmentDuration&#x60;](#SegmentSettings), and [&#x60;segmentDuration&#x60;](#SegmentSettings) must be divisible by &#x60;gopDuration&#x60;. | [optional] 
**gopFrameCount** | **Number** | Select the GOP size based on the specified frame count. Must be greater than zero. | [optional] 
**heightPixels** | **Number** | The height of the video in pixels. Must be an even integer. When not specified, the height is adjusted to match the specified width and input aspect ratio. If both are omitted, the input height is used. For portrait videos that contain horizontal ASR and rotation metadata, provide the height, in pixels, per the horizontal ASR. The API calculates the width per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. | [optional] 
**hlg** | **Object** | Convert the input video to a Hybrid Log Gamma (HLG) video. | [optional] 
**pixelFormat** | **String** | Pixel format to use. The default is &#x60;yuv420p&#x60;. Supported pixel formats: - &#x60;yuv420p&#x60; pixel format - &#x60;yuv422p&#x60; pixel format - &#x60;yuv444p&#x60; pixel format - &#x60;yuv420p10&#x60; 10-bit HDR pixel format - &#x60;yuv422p10&#x60; 10-bit HDR pixel format - &#x60;yuv444p10&#x60; 10-bit HDR pixel format - &#x60;yuv420p12&#x60; 12-bit HDR pixel format - &#x60;yuv422p12&#x60; 12-bit HDR pixel format - &#x60;yuv444p12&#x60; 12-bit HDR pixel format | [optional] 
**profile** | **String** | Enforces the specified codec profile. The following profiles are supported: * &#x60;profile0&#x60; (default) * &#x60;profile1&#x60; * &#x60;profile2&#x60; * &#x60;profile3&#x60; The available options are [WebM-compatible](https://www.webmproject.org/vp9/profiles/). Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;Vp9CodecSettings&#x60; message. | [optional] 
**rateControlMode** | **String** | Specify the mode. The default is &#x60;vbr&#x60;. Supported rate control modes: - &#x60;vbr&#x60; - variable bitrate | [optional] 
**sdr** | **Object** | Convert the input video to a Standard Dynamic Range (SDR) video. | [optional] 
**widthPixels** | **Number** | The width of the video in pixels. Must be an even integer. When not specified, the width is adjusted to match the specified height and input aspect ratio. If both are omitted, the input width is used. For portrait videos that contain horizontal ASR and rotation metadata, provide the width, in pixels, per the horizontal ASR. The API calculates the height per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. | [optional] 



## Enum: FrameRateConversionStrategyEnum


* `FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED` (value: `"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED"`)

* `DOWNSAMPLE` (value: `"DOWNSAMPLE"`)

* `DROP_DUPLICATE` (value: `"DROP_DUPLICATE"`)




