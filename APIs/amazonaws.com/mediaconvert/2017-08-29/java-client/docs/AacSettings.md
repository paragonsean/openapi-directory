

# AacSettings

Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to \"VBR\" or \"CBR\". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioDescriptionBroadcasterMix** | [**AacAudioDescriptionBroadcasterMix**](AacAudioDescriptionBroadcasterMix.md) |  |  [optional] |
|**bitrate** | [**Integer**](Integer.md) |  |  [optional] |
|**codecProfile** | [**AacCodecProfile**](AacCodecProfile.md) |  |  [optional] |
|**codingMode** | [**AacCodingMode**](AacCodingMode.md) |  |  [optional] |
|**rateControlMode** | [**AacRateControlMode**](AacRateControlMode.md) |  |  [optional] |
|**rawFormat** | [**AacRawFormat**](AacRawFormat.md) |  |  [optional] |
|**sampleRate** | [**Integer**](Integer.md) |  |  [optional] |
|**specification** | [**AacSpecification**](AacSpecification.md) |  |  [optional] |
|**vbrQuality** | [**AacVbrQuality**](AacVbrQuality.md) |  |  [optional] |



