# NamSorApiV2.PersonalNameGenderedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genderScale** | **Number** | Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value. | [optional] 
**id** | **String** |  | [optional] 
**likelyGender** | **String** | Most likely gender | [optional] 
**name** | **String** | The input name | [optional] 
**probabilityCalibrated** | **Number** | The calibrated probability for inferred gender to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**score** | **Number** | Compatibility to NamSor_v1 Gender score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 



## Enum: LikelyGenderEnum


* `male` (value: `"male"`)

* `female` (value: `"female"`)

* `unknown` (value: `"unknown"`)




