# ThePlaidApi.DocumentRiskSignal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualValue** | **String** | The derived value obtained in the risk signal calculation process for this field | 
**expectedValue** | **String** | The expected value of the field, as seen on the document | 
**field** | **String** | The field which the risk signal was computed for | 
**hasFraudRisk** | **Boolean** | A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent | 
**institutionMetadata** | [**DocumentRiskSignalInstitutionMetadata**](DocumentRiskSignalInstitutionMetadata.md) |  | 
**pageNumber** | **Number** | The relevant page associated with the risk signal | 
**signalDescription** | **String** | A human-readable explanation providing more detail into the particular risk signal | 
**type** | **String** | The result from the risk signal check. | 


