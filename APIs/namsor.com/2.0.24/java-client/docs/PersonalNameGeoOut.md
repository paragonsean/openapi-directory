

# PersonalNameGeoOut

Classified geo names

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countriesTop** | **List&lt;String&gt;** | List countries (top 10) |  [optional] |
|**country** | **String** | Most likely country  |  [optional] |
|**countryAlt** | **String** | Second best alternative : country  |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** | The input name. |  [optional] |
|**probabilityAltCalibrated** | **Double** | The calibrated probability for country OR countryAlt to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**probabilityCalibrated** | **Double** | The calibrated probability for country to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**region** | **String** | Most likely region (based on country ISO2 code) |  [optional] |
|**score** | **Double** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  |  [optional] |
|**script** | **String** |  |  [optional] |
|**subRegion** | **String** | Most likely sub region (based on country ISO2 code) |  [optional] |
|**topRegion** | **String** | Most likely top region (based on country ISO2 code) |  [optional] |



