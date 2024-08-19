

# FirstLastNameGenderedOut

Represents the output of inferring the LIKELY gender from a personal name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** | The first name (also known as given name) |  [optional] |
|**genderScale** | **Double** | Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value. |  [optional] |
|**id** | **String** |  |  [optional] |
|**lastName** | **String** | The last name (also known as family name, or surname) |  [optional] |
|**likelyGender** | [**LikelyGenderEnum**](#LikelyGenderEnum) | Most likely gender |  [optional] |
|**probabilityCalibrated** | **Double** | The calibrated probability for inferred gender to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**score** | **Double** | Compatibility to NamSor_v1 Gender score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  |  [optional] |
|**script** | **String** |  |  [optional] |



## Enum: LikelyGenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |
| UNKNOWN | &quot;unknown&quot; |



