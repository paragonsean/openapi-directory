

# H265CodecSettings

H265 codec settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOpenGop** | **Boolean** | Specifies whether an open Group of Pictures (GOP) structure should be allowed or not. The default is &#x60;false&#x60;. |  [optional] |
|**aqStrength** | **Double** | Specify the intensity of the adaptive quantizer (AQ). Must be between 0 and 1, where 0 disables the quantizer and 1 maximizes the quantizer. A higher value equals a lower bitrate but smoother image. The default is 0. |  [optional] |
|**bFrameCount** | **Integer** | The number of consecutive B-frames. Must be greater than or equal to zero. Must be less than H265CodecSettings.gop_frame_count if set. The default is 0. |  [optional] |
|**bPyramid** | **Boolean** | Allow B-pyramid for reference frame selection. This may not be supported on all decoders. The default is &#x60;false&#x60;. |  [optional] |
|**bitrateBps** | **Integer** | Required. The video bitrate in bits per second. The minimum value is 1,000. The maximum value is 800,000,000. |  [optional] |
|**crfLevel** | **Integer** | Target CRF level. Must be between 10 and 36, where 10 is the highest quality and 36 is the most efficient compression. The default is 21. |  [optional] |
|**enableTwoPass** | **Boolean** | Use two-pass encoding strategy to achieve better video quality. H265CodecSettings.rate_control_mode must be &#x60;vbr&#x60;. The default is &#x60;false&#x60;. |  [optional] |
|**frameRate** | **Double** | Required. The target video frame rate in frames per second (FPS). Must be less than or equal to 120. |  [optional] |
|**frameRateConversionStrategy** | [**FrameRateConversionStrategyEnum**](#FrameRateConversionStrategyEnum) | Optional. Frame rate conversion strategy for desired frame rate. The default is &#x60;DOWNSAMPLE&#x60;. |  [optional] |
|**gopDuration** | **String** | Select the GOP size based on the specified duration. The default is &#x60;3s&#x60;. Note that &#x60;gopDuration&#x60; must be less than or equal to [&#x60;segmentDuration&#x60;](#SegmentSettings), and [&#x60;segmentDuration&#x60;](#SegmentSettings) must be divisible by &#x60;gopDuration&#x60;. |  [optional] |
|**gopFrameCount** | **Integer** | Select the GOP size based on the specified frame count. Must be greater than zero. |  [optional] |
|**hdr10** | **Object** | Convert the input video to a High Dynamic Range 10 (HDR10) video. |  [optional] |
|**heightPixels** | **Integer** | The height of the video in pixels. Must be an even integer. When not specified, the height is adjusted to match the specified width and input aspect ratio. If both are omitted, the input height is used. For portrait videos that contain horizontal ASR and rotation metadata, provide the height, in pixels, per the horizontal ASR. The API calculates the width per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. |  [optional] |
|**hlg** | **Object** | Convert the input video to a Hybrid Log Gamma (HLG) video. |  [optional] |
|**pixelFormat** | **String** | Pixel format to use. The default is &#x60;yuv420p&#x60;. Supported pixel formats: - &#x60;yuv420p&#x60; pixel format - &#x60;yuv422p&#x60; pixel format - &#x60;yuv444p&#x60; pixel format - &#x60;yuv420p10&#x60; 10-bit HDR pixel format - &#x60;yuv422p10&#x60; 10-bit HDR pixel format - &#x60;yuv444p10&#x60; 10-bit HDR pixel format - &#x60;yuv420p12&#x60; 12-bit HDR pixel format - &#x60;yuv422p12&#x60; 12-bit HDR pixel format - &#x60;yuv444p12&#x60; 12-bit HDR pixel format |  [optional] |
|**preset** | **String** | Enforces the specified codec preset. The default is &#x60;veryfast&#x60;. The available options are [FFmpeg-compatible](https://trac.ffmpeg.org/wiki/Encode/H.265). Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;H265CodecSettings&#x60; message. |  [optional] |
|**profile** | **String** | Enforces the specified codec profile. The following profiles are supported: * 8-bit profiles * &#x60;main&#x60; (default) * &#x60;main-intra&#x60; * &#x60;mainstillpicture&#x60; * 10-bit profiles * &#x60;main10&#x60; (default) * &#x60;main10-intra&#x60; * &#x60;main422-10&#x60; * &#x60;main422-10-intra&#x60; * &#x60;main444-10&#x60; * &#x60;main444-10-intra&#x60; * 12-bit profiles * &#x60;main12&#x60; (default) * &#x60;main12-intra&#x60; * &#x60;main422-12&#x60; * &#x60;main422-12-intra&#x60; * &#x60;main444-12&#x60; * &#x60;main444-12-intra&#x60; The available options are [FFmpeg-compatible](https://x265.readthedocs.io/). Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;H265CodecSettings&#x60; message. |  [optional] |
|**rateControlMode** | **String** | Specify the mode. The default is &#x60;vbr&#x60;. Supported rate control modes: - &#x60;vbr&#x60; - variable bitrate - &#x60;crf&#x60; - constant rate factor |  [optional] |
|**sdr** | **Object** | Convert the input video to a Standard Dynamic Range (SDR) video. |  [optional] |
|**tune** | **String** | Enforces the specified codec tune. The available options are [FFmpeg-compatible](https://trac.ffmpeg.org/wiki/Encode/H.265). Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;H265CodecSettings&#x60; message. |  [optional] |
|**vbvFullnessBits** | **Integer** | Initial fullness of the Video Buffering Verifier (VBV) buffer in bits. Must be greater than zero. The default is equal to 90% of H265CodecSettings.vbv_size_bits. |  [optional] |
|**vbvSizeBits** | **Integer** | Size of the Video Buffering Verifier (VBV) buffer in bits. Must be greater than zero. The default is equal to &#x60;VideoStream.bitrate_bps&#x60;. |  [optional] |
|**widthPixels** | **Integer** | The width of the video in pixels. Must be an even integer. When not specified, the width is adjusted to match the specified height and input aspect ratio. If both are omitted, the input width is used. For portrait videos that contain horizontal ASR and rotation metadata, provide the width, in pixels, per the horizontal ASR. The API calculates the height per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. |  [optional] |



## Enum: FrameRateConversionStrategyEnum

| Name | Value |
|---- | -----|
| FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED | &quot;FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED&quot; |
| DOWNSAMPLE | &quot;DOWNSAMPLE&quot; |
| DROP_DUPLICATE | &quot;DROP_DUPLICATE&quot; |



