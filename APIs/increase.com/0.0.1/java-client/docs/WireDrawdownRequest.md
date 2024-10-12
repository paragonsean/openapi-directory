

# WireDrawdownRequest

Wire drawdown requests enable you to request that someone else send you a wire. This feature is in beta; reach out to [support@increase.com](mailto:support@increase.com) to learn more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumberId** | **String** | The Account Number to which the recipient of this request is being requested to send funds. |  |
|**amount** | **Integer** | The amount being requested in cents. |  |
|**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being requested. Will always be \&quot;USD\&quot;. |  |
|**fulfillmentTransactionId** | **String** | If the recipient fulfills the drawdown request by sending funds, then this will be the identifier of the corresponding Transaction. |  |
|**id** | **String** | The Wire drawdown request identifier. |  |
|**messageToRecipient** | **String** | The message the recipient will see as part of the drawdown request. |  |
|**recipientAccountNumber** | **String** | The drawdown request&#39;s recipient&#39;s account number. |  |
|**recipientAddressLine1** | **String** | Line 1 of the drawdown request&#39;s recipient&#39;s address. |  |
|**recipientAddressLine2** | **String** | Line 2 of the drawdown request&#39;s recipient&#39;s address. |  |
|**recipientAddressLine3** | **String** | Line 3 of the drawdown request&#39;s recipient&#39;s address. |  |
|**recipientName** | **String** | The drawdown request&#39;s recipient&#39;s name. |  |
|**recipientRoutingNumber** | **String** | The drawdown request&#39;s recipient&#39;s routing number. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the drawdown request. |  |
|**submission** | [**WireDrawdownRequestSubmission**](WireDrawdownRequestSubmission.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;wire_drawdown_request&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_SUBMISSION | &quot;pending_submission&quot; |
| PENDING_RESPONSE | &quot;pending_response&quot; |
| FULFILLED | &quot;fulfilled&quot; |
| REFUSED | &quot;refused&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WIRE_DRAWDOWN_REQUEST | &quot;wire_drawdown_request&quot; |



