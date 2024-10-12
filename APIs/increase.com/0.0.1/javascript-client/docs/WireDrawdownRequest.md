# IncreaseApi.WireDrawdownRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumberId** | **String** | The Account Number to which the recipient of this request is being requested to send funds. | 
**amount** | **Number** | The amount being requested in cents. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being requested. Will always be \&quot;USD\&quot;. | 
**fulfillmentTransactionId** | **String** | If the recipient fulfills the drawdown request by sending funds, then this will be the identifier of the corresponding Transaction. | 
**id** | **String** | The Wire drawdown request identifier. | 
**messageToRecipient** | **String** | The message the recipient will see as part of the drawdown request. | 
**recipientAccountNumber** | **String** | The drawdown request&#39;s recipient&#39;s account number. | 
**recipientAddressLine1** | **String** | Line 1 of the drawdown request&#39;s recipient&#39;s address. | 
**recipientAddressLine2** | **String** | Line 2 of the drawdown request&#39;s recipient&#39;s address. | 
**recipientAddressLine3** | **String** | Line 3 of the drawdown request&#39;s recipient&#39;s address. | 
**recipientName** | **String** | The drawdown request&#39;s recipient&#39;s name. | 
**recipientRoutingNumber** | **String** | The drawdown request&#39;s recipient&#39;s routing number. | 
**status** | **String** | The lifecycle status of the drawdown request. | 
**submission** | [**WireDrawdownRequestSubmission**](WireDrawdownRequestSubmission.md) |  | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;wire_drawdown_request&#x60;. | 



## Enum: StatusEnum


* `pending_submission` (value: `"pending_submission"`)

* `pending_response` (value: `"pending_response"`)

* `fulfilled` (value: `"fulfilled"`)

* `refused` (value: `"refused"`)





## Enum: TypeEnum


* `wire_drawdown_request` (value: `"wire_drawdown_request"`)




