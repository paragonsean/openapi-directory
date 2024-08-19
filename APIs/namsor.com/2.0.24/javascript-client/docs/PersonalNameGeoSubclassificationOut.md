# NamSorApiV2.PersonalNameGeoSubclassificationOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryIso2** | **String** | The input country ISO2 code | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** | The input name | [optional] 
**probabilityAltCalibrated** | **Number** | The calibrated probability for subclassification OR subclassificationAlt to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**probabilityCalibrated** | **Number** | The calibrated probability for subclassification to have been guessed correctly. -1 &#x3D; still calibrating.  | [optional] 
**score** | **Number** | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 
**subClassification** | **String** | Most likely subclassification ISO_3166-2 code | [optional] 
**subClassificationAlt** | **String** | Second best alternative : subclassification ISO_3166-2 code | [optional] 
**subclassificationTop** | **[String]** | List subclassification ISO_3166-2 codes (top 10) | [optional] 


