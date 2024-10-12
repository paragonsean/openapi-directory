# AdyenPayoutApi.SubmitResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | **{String: String}** | This field contains additional data, which may be returned in a particular response. | [optional] 
**pspReference** | **String** | A new reference to uniquely identify this request. | 
**refusalReason** | **String** | In case of refusal, an informational message for the reason. | [optional] 
**resultCode** | **String** | The response: * In case of success, it is &#x60;payout-submit-received&#x60;. * In case of an error, an informational message is returned. | 


