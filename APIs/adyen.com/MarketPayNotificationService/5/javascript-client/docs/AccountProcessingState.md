# ClassicPlatformsNotifications.AccountProcessingState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableReason** | **String** | The reason why processing has been disabled. | [optional] 
**disabled** | **Boolean** | Indicates whether the processing of payments is allowed. | [optional] 
**processedFrom** | [**Amount**](Amount.md) | The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier). | [optional] 
**processedTo** | [**Amount**](Amount.md) | The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier). | [optional] 
**tierNumber** | **Number** | The processing tier that the account holder occupies. | [optional] 


