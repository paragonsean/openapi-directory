# AzureMediaServices.H264Video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | **String** | Tells the encoder how to choose its encoding settings. The default value is Balanced. | [optional] 
**layers** | [**[H264Layer]**](H264Layer.md) | The collection of output H.264 layers to be produced by the encoder. | [optional] 
**sceneChangeDetection** | **Boolean** | Whether or not the encoder should insert key frames at scene changes. If not specified, the default is false. This flag should be set to true only when the encoder is being configured to produce a single output video. | [optional] 



## Enum: ComplexityEnum


* `Speed` (value: `"Speed"`)

* `Balanced` (value: `"Balanced"`)

* `Quality` (value: `"Quality"`)




