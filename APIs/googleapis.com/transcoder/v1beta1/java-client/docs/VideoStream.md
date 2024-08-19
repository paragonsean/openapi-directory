

# VideoStream

Video stream resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOpenGop** | **Boolean** | Specifies whether an open Group of Pictures (GOP) structure should be allowed or not. The default is &#x60;false&#x60;. |  [optional] |
|**aqStrength** | **Double** | Specify the intensity of the adaptive quantizer (AQ). Must be between 0 and 1, where 0 disables the quantizer and 1 maximizes the quantizer. A higher value equals a lower bitrate but smoother image. The default is 0. |  [optional] |
|**bFrameCount** | **Integer** | The number of consecutive B-frames. Must be greater than or equal to zero. Must be less than &#x60;VideoStream.gop_frame_count&#x60; if set. The default is 0. |  [optional] |
|**bPyramid** | **Boolean** | Allow B-pyramid for reference frame selection. This may not be supported on all decoders. The default is &#x60;false&#x60;. |  [optional] |
|**bitrateBps** | **Integer** | Required. The video bitrate in bits per second. The minimum value is 1,000. The maximum value for H264/H265 is 800,000,000. The maximum value for VP9 is 480,000,000. |  [optional] |
|**codec** | **String** | Codec type. The following codecs are supported: * &#x60;h264&#x60; (default) * &#x60;h265&#x60; * &#x60;vp9&#x60; |  [optional] |
|**crfLevel** | **Integer** | Target CRF level. Must be between 10 and 36, where 10 is the highest quality and 36 is the most efficient compression. The default is 21. |  [optional] |
|**enableTwoPass** | **Boolean** | Use two-pass encoding strategy to achieve better video quality. &#x60;VideoStream.rate_control_mode&#x60; must be &#x60;\&quot;vbr\&quot;&#x60;. The default is &#x60;false&#x60;. |  [optional] |
|**entropyCoder** | **String** | The entropy coder to use. The default is &#x60;\&quot;cabac\&quot;&#x60;. Supported entropy coders: - &#39;cavlc&#39; - &#39;cabac&#39; |  [optional] |
|**frameRate** | **Double** | Required. The target video frame rate in frames per second (FPS). Must be less than or equal to 120. Will default to the input frame rate if larger than the input frame rate. The API will generate an output FPS that is divisible by the input FPS, and smaller or equal to the target FPS. See [Calculate frame rate](https://cloud.google.com/transcoder/docs/concepts/frame-rate) for more information. |  [optional] |
|**gopDuration** | **String** | Select the GOP size based on the specified duration. The default is &#x60;\&quot;3s\&quot;&#x60;. Note that &#x60;gopDuration&#x60; must be less than or equal to [&#x60;segmentDuration&#x60;](#SegmentSettings), and [&#x60;segmentDuration&#x60;](#SegmentSettings) must be divisible by &#x60;gopDuration&#x60;. |  [optional] |
|**gopFrameCount** | **Integer** | Select the GOP size based on the specified frame count. Must be greater than zero. |  [optional] |
|**heightPixels** | **Integer** | The height of the video in pixels. Must be an even integer. When not specified, the height is adjusted to match the specified width and input aspect ratio. If both are omitted, the input height is used. |  [optional] |
|**pixelFormat** | **String** | Pixel format to use. The default is &#x60;\&quot;yuv420p\&quot;&#x60;. Supported pixel formats: - &#39;yuv420p&#39; pixel format. - &#39;yuv422p&#39; pixel format. - &#39;yuv444p&#39; pixel format. - &#39;yuv420p10&#39; 10-bit HDR pixel format. - &#39;yuv422p10&#39; 10-bit HDR pixel format. - &#39;yuv444p10&#39; 10-bit HDR pixel format. - &#39;yuv420p12&#39; 12-bit HDR pixel format. - &#39;yuv422p12&#39; 12-bit HDR pixel format. - &#39;yuv444p12&#39; 12-bit HDR pixel format. |  [optional] |
|**preset** | **String** | Enforces the specified codec preset. The default is &#x60;veryfast&#x60;. The available options are FFmpeg-compatible. Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;VideoStream&#x60; message. |  [optional] |
|**profile** | **String** | Enforces the specified codec profile. The following profiles are supported: * &#x60;baseline&#x60; * &#x60;main&#x60; * &#x60;high&#x60; (default) The available options are FFmpeg-compatible. Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;VideoStream&#x60; message. |  [optional] |
|**rateControlMode** | **String** | Specify the &#x60;rate_control_mode&#x60;. The default is &#x60;\&quot;vbr\&quot;&#x60;. Supported rate control modes: - &#39;vbr&#39; - variable bitrate - &#39;crf&#39; - constant rate factor |  [optional] |
|**tune** | **String** | Enforces the specified codec tune. The available options are FFmpeg-compatible. Note that certain values for this field may cause the transcoder to override other fields you set in the &#x60;VideoStream&#x60; message. |  [optional] |
|**vbvFullnessBits** | **Integer** | Initial fullness of the Video Buffering Verifier (VBV) buffer in bits. Must be greater than zero. The default is equal to 90% of &#x60;VideoStream.vbv_size_bits&#x60;. |  [optional] |
|**vbvSizeBits** | **Integer** | Size of the Video Buffering Verifier (VBV) buffer in bits. Must be greater than zero. The default is equal to &#x60;VideoStream.bitrate_bps&#x60;. |  [optional] |
|**widthPixels** | **Integer** | The width of the video in pixels. Must be an even integer. When not specified, the width is adjusted to match the specified height and input aspect ratio. If both are omitted, the input width is used. |  [optional] |



