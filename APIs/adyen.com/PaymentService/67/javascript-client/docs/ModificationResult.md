# AdyenPaymentApi.ModificationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | **{String: String}** | This field contains additional data, which may be returned in a particular modification response. | [optional] 
**pspReference** | **String** | Adyen&#39;s 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. | 
**response** | **String** | Indicates if the modification request has been received for processing. | 



## Enum: ResponseEnum


* `capture-received]` (value: `"[capture-received]"`)

* `cancel-received]` (value: `"[cancel-received]"`)

* `refund-received]` (value: `"[refund-received]"`)

* `cancelOrRefund-received]` (value: `"[cancelOrRefund-received]"`)

* `adjustAuthorisation-received]` (value: `"[adjustAuthorisation-received]"`)

* `donation-received]` (value: `"[donation-received]"`)

* `technical-cancel-received]` (value: `"[technical-cancel-received]"`)

* `voidPendingRefund-received]` (value: `"[voidPendingRefund-received]"`)




