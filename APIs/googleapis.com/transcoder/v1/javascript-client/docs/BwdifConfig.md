# TranscoderApi.BwdifConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deinterlaceAllFrames** | **Boolean** | Deinterlace all frames rather than just the frames identified as interlaced. The default is &#x60;false&#x60;. | [optional] 
**mode** | **String** | Specifies the deinterlacing mode to adopt. The default is &#x60;send_frame&#x60;. Supported values: - &#x60;send_frame&#x60;: Output one frame for each frame - &#x60;send_field&#x60;: Output one frame for each field | [optional] 
**parity** | **String** | The picture field parity assumed for the input interlaced video. The default is &#x60;auto&#x60;. Supported values: - &#x60;tff&#x60;: Assume the top field is first - &#x60;bff&#x60;: Assume the bottom field is first - &#x60;auto&#x60;: Enable automatic detection of field parity | [optional] 


