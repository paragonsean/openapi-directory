# CloudHealthcareApi.Finding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **String** | Zero-based ending index of the found text, exclusively. | [optional] 
**infoType** | **String** | The type of information stored in this text range. For example, HumanName, BirthDate, or Address. | [optional] 
**quote** | **String** | The snippet of the sensitive text. This field is only populated during deidentification if &#x60;store_quote&#x60; is set to true in DeidentifyConfig. | [optional] 
**start** | **String** | Zero-based starting index of the found text, inclusively. | [optional] 


