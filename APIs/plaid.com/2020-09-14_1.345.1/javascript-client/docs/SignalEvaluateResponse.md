# ThePlaidApi.SignalEvaluateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coreAttributes** | [**SignalEvaluateCoreAttributes**](SignalEvaluateCoreAttributes.md) |  | [optional] 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**scores** | [**SignalScores**](SignalScores.md) |  | 
**warnings** | [**[SignalWarning]**](SignalWarning.md) | If bank information was not able to be used as features into the Signal model, this array contains warnings describing why we were missing bank data | [optional] 


