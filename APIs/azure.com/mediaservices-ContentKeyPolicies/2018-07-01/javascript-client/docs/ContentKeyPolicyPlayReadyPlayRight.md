# AzureMediaServices.ContentKeyPolicyPlayReadyPlayRight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agcAndColorStripeRestriction** | **Number** | Configures Automatic Gain Control (AGC) and Color Stripe in the license. Must be between 0 and 3 inclusive. | [optional] 
**allowPassingVideoContentToUnknownOutput** | **String** | Configures Unknown output handling settings of the license. | 
**analogVideoOpl** | **Number** | Specifies the output protection level for compressed digital audio. | [optional] 
**compressedDigitalAudioOpl** | **Number** | Specifies the output protection level for compressed digital audio. | [optional] 
**compressedDigitalVideoOpl** | **Number** | Specifies the output protection level for compressed digital video. | [optional] 
**digitalVideoOnlyContentRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. | 
**explicitAnalogTelevisionOutputRestriction** | [**ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction**](ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction.md) |  | [optional] 
**firstPlayExpiration** | **String** | The amount of time that the license is valid after the license is first used to play content. | [optional] 
**imageConstraintForAnalogComponentVideoRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. | 
**imageConstraintForAnalogComputerMonitorRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. | 
**scmsRestriction** | **Number** | Configures the Serial Copy Management System (SCMS) in the license. Must be between 0 and 3 inclusive. | [optional] 
**uncompressedDigitalAudioOpl** | **Number** | Specifies the output protection level for uncompressed digital audio. | [optional] 
**uncompressedDigitalVideoOpl** | **Number** | Specifies the output protection level for uncompressed digital video. | [optional] 



## Enum: AllowPassingVideoContentToUnknownOutputEnum


* `Unknown` (value: `"Unknown"`)

* `NotAllowed` (value: `"NotAllowed"`)

* `Allowed` (value: `"Allowed"`)

* `AllowedWithVideoConstriction` (value: `"AllowedWithVideoConstriction"`)




