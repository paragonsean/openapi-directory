# SquareConnectApi.Refund

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalRecipients** | [**[AdditionalRecipient]**](AdditionalRecipient.md) | Additional recipients (other than the merchant) receiving a portion of this refund. For example, fees assessed on a refund of a purchase by a third party integration. | [optional] 
**amountMoney** | [**Money**](Money.md) |  | 
**createdAt** | **String** | The timestamp for when the refund was created, in RFC 3339 format. | [optional] 
**id** | **String** | The refund&#39;s unique ID. | 
**locationId** | **String** | The ID of the refund&#39;s associated location. | 
**processingFeeMoney** | [**Money**](Money.md) |  | [optional] 
**reason** | **String** | The reason for the refund being issued. | 
**status** | **String** | The current status of the refund (&#x60;PENDING&#x60;, &#x60;APPROVED&#x60;, &#x60;REJECTED&#x60;, or &#x60;FAILED&#x60;). | 
**tenderId** | **String** | The ID of the refunded tender. | 
**transactionId** | **String** | The ID of the transaction that the refunded tender is part of. | 


