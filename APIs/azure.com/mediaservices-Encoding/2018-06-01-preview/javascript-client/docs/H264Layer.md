# AzureMediaServices.H264Layer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bufferWindow** | **String** | The VBV buffer window length. The value should be in ISO 8601 format. The value should be in the range [0.1-100] seconds. The default is 5 seconds (for example, PT5S). | [optional] 
**entropyMode** | **String** | The entropy mode to be used for this layer. If not specified, the encoder chooses the mode that is appropriate for the profile and level. | [optional] 
**level** | **String** | Which level of the H.264 standard should be used when encoding this layer. The value can be Auto, or a number that matches the H.264 profile. If not specified, the default is Auto, which lets the encoder choose the Level that is appropriate for this layer. | [optional] 
**profile** | **String** | Which profile of the H.264 standard should be used when encoding this layer. Default is Auto. | [optional] 
**referenceFrames** | **Number** | The number of reference frames to be used when encoding this layer. If not specified, the encoder determines an appropriate number based on the encoder complexity setting. | [optional] 



## Enum: EntropyModeEnum


* `Cabac` (value: `"Cabac"`)

* `Cavlc` (value: `"Cavlc"`)





## Enum: ProfileEnum


* `Auto` (value: `"Auto"`)

* `Baseline` (value: `"Baseline"`)

* `Main` (value: `"Main"`)

* `High` (value: `"High"`)

* `High422` (value: `"High422"`)

* `High444` (value: `"High444"`)




