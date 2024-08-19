

# FirstLastNameOriginedOut

Represents the output of inferring the LIKELY country of Origin from a personal name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countriesOriginTop** | **List&lt;String&gt;** | List countries of Origin (top 10) |  [optional] |
|**countryOrigin** | **String** | Most likely country of Origin |  [optional] |
|**countryOriginAlt** | **String** | Second best alternative : country of Origin |  [optional] |
|**firstName** | **String** | The first name (also known as given name) |  [optional] |
|**id** | **String** |  |  [optional] |
|**lastName** | **String** | The last name (also known as family name, or surname) |  [optional] |
|**probabilityAltCalibrated** | **Double** | The calibrated probability for countryOrigin OR countryOriginAlt to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**probabilityCalibrated** | **Double** | The calibrated probability for countryOrigin to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**regionOrigin** | **String** | Most likely region of Origin (based on countryOrigin ISO2 code) |  [optional] |
|**score** | **Double** | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  |  [optional] |
|**script** | **String** |  |  [optional] |
|**subRegionOrigin** | **String** | Most likely sub region of Origin (based on countryOrigin ISO2 code) |  [optional] |
|**topRegionOrigin** | **String** | Most likely top region of Origin (based on countryOrigin ISO2 code) |  [optional] |



