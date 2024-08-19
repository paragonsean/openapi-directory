# TranscoderApi.AudioMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomKey** | **String** | Required. The EditAtom.key that references the atom with audio inputs in the JobConfig.edit_list. | [optional] 
**gainDb** | **Number** | Audio volume control in dB. Negative values decrease volume, positive values increase. The default is 0. | [optional] 
**inputChannel** | **Number** | Required. The zero-based index of the channel in the input audio stream. | [optional] 
**inputKey** | **String** | Required. The Input.key that identifies the input file. | [optional] 
**inputTrack** | **Number** | Required. The zero-based index of the track in the input file. | [optional] 
**outputChannel** | **Number** | Required. The zero-based index of the channel in the output audio stream. | [optional] 


