

# FirstLastNameGeoSubclassificationOut

Represents the geographic name origin at a country subclassification level (usually regional or state level).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryIso2** | **String** | The input country ISO2 code |  [optional] |
|**firstName** | **String** | The first name (also known as given name) |  [optional] |
|**id** | **String** |  |  [optional] |
|**lastName** | **String** | The last name (also known as family name, or surname) |  [optional] |
|**probabilityAltCalibrated** | **Double** | The calibrated probability for subclassification OR subclassificationAlt to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**probabilityCalibrated** | **Double** | The calibrated probability for subclassification to have been guessed correctly. -1 &#x3D; still calibrating.  |  [optional] |
|**score** | **Double** | Compatibility to NamSor_v1 Origin score value. Higher score is better, but score is not normalized. Use calibratedProbability if available.  |  [optional] |
|**script** | **String** |  |  [optional] |
|**subClassification** | **String** | Most likely subclassification ISO_3166-2 code |  [optional] |
|**subClassificationAlt** | **String** | Second best alternative : subclassification ISO_3166-2 code |  [optional] |
|**subclassificationTop** | **List&lt;String&gt;** | List subclassification ISO_3166-2 codes (top 10) |  [optional] |



