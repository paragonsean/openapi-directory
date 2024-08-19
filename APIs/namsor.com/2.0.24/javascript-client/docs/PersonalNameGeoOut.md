# NamSorApiV2.PersonalNameGeoOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countriesTop** | **[String]** | List countries (top 10) | [optional] 
**country** | **String** | Most likely country  | [optional] 
**countryAlt** | **String** | Second best alternative : country  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** | The input name. | [optional] 
**probabilityAltCalibrated** | **Number** | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probabilityCalibrated** | **Number** | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**region** | **String** | Most likely region (based on country ISO2 code) | [optional] 
**score** | **Number** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 
**subRegion** | **String** | Most likely sub region (based on country ISO2 code) | [optional] 
**topRegion** | **String** | Most likely top region (based on country ISO2 code) | [optional] 


