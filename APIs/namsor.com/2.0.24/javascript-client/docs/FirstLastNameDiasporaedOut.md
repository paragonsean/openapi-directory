# NamSorApiV2.FirstLastNameDiasporaedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryIso2** | **String** | From input data, the countryIso2 of geographic context (US,CA etc.) | [optional] 
**ethnicitiesTop** | **[String]** | List most likely ethnicities (top 10) | [optional] 
**ethnicity** | **String** | The most likely ethnicity | [optional] 
**ethnicityAlt** | **String** | The second best alternative ethnicity | [optional] 
**firstName** | **String** | The first name (also known as given name) | [optional] 
**id** | **String** |  | [optional] 
**lastName** | **String** | The last name (also known as family name, or surname) | [optional] 
**lifted** | **Boolean** | Indicates if the output ethnicity is based on machine learning only, or further lifted as a known fact by a country-specific rule. Let us know if you believe ethnicity is incorrect on a specific case where lifted is true. | [optional] 
**probabilityAltCalibrated** | **Number** | The calibrated probability for ethnicity OR ethnicityAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probabilityCalibrated** | **Number** | The calibrated probability for ethnicity to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**score** | **Number** | Compatibility to NamSor_v1 Diaspora score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 


