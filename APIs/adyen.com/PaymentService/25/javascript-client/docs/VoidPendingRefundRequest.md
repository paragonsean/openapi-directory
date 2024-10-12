# AdyenPaymentApi.VoidPendingRefundRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**CancelOrRefundRequestAdditionalData**](CancelOrRefundRequestAdditionalData.md) |  | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**modificationAmount** | [**Amount**](Amount.md) | The amount that needs to be captured/refunded. Required for &#x60;/capture&#x60; and &#x60;/refund&#x60;, not allowed for &#x60;/cancel&#x60;. The &#x60;currency&#x60; must match the currency used in authorisation, the &#x60;value&#x60; must be smaller than or equal to the authorised amount. | [optional] 
**originalReference** | **String** | The original pspReference of the payment to modify. This reference is returned in: * authorisation response * authorisation notification   | [optional] 
**reference** | **String** | Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters. | [optional] 
**tenderReference** | **String** | The transaction reference provided by the PED. For point-of-sale integrations only. | [optional] 
**uniqueTerminalId** | **String** | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. | [optional] 


