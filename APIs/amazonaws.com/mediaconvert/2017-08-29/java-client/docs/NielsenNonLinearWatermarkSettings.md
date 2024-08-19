

# NielsenNonLinearWatermarkSettings

Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 5.2.1 Nielsen NLM Watermark Engine Version 1.2.7 Nielsen Watermark Authenticator [SID_TIC] Version [5.0.0]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeWatermarkProcess** | [**NielsenActiveWatermarkProcessType**](NielsenActiveWatermarkProcessType.md) |  |  [optional] |
|**adiFilename** | [**String**](String.md) |  |  [optional] |
|**assetId** | [**String**](String.md) |  |  [optional] |
|**assetName** | [**String**](String.md) |  |  [optional] |
|**cbetSourceId** | [**String**](String.md) |  |  [optional] |
|**episodeId** | [**String**](String.md) |  |  [optional] |
|**metadataDestination** | [**String**](String.md) |  |  [optional] |
|**sourceId** | [**Integer**](Integer.md) |  |  [optional] |
|**sourceWatermarkStatus** | [**NielsenSourceWatermarkStatusType**](NielsenSourceWatermarkStatusType.md) |  |  [optional] |
|**ticServerUrl** | [**String**](String.md) |  |  [optional] |
|**uniqueTicPerAudioTrack** | [**NielsenUniqueTicPerAudioTrackType**](NielsenUniqueTicPerAudioTrackType.md) |  |  [optional] |



