

# PersonalNameGenderedOut

Classified genderized names

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**genderScale** | **Double** | Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value. |  [optional] |
|**id** | **String** |  |  [optional] |
|**likelyGender** | [**LikelyGenderEnum**](#LikelyGenderEnum) | Most likely gender |  [optional] |
|**name** | **String** | The input name |  [optional] |
|**probabilityCalibrated** | **Double** | The calibrated probability for inferred gender to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**score** | **Double** | Compatibility to NamSor_v1 Gender score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  |  [optional] |
|**script** | **String** |  |  [optional] |



## Enum: LikelyGenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |
| UNKNOWN | &quot;unknown&quot; |



