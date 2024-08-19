# NamSorApiV2.PersonalNameReligionedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**name** | **String** | The input name. | [optional] 
**probabilityAltCalibrated** | **Number** | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probabilityCalibrated** | **Number** | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**religion** | **String** | Most likely religion | [optional] 
**religionAlt** | **String** | Second best alternative : religion  | [optional] 
**religionsTop** | **[String]** | List countries (top 10) | [optional] 
**score** | **Number** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 


