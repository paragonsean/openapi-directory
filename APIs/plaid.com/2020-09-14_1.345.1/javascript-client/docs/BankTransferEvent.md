# ThePlaidApi.BankTransferEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID associated with the bank transfer. | 
**bankTransferAmount** | **String** | The bank transfer amount. | 
**bankTransferId** | **String** | Plaid’s unique identifier for a bank transfer. | 
**bankTransferIsoCurrencyCode** | **String** | The currency of the bank transfer amount. | 
**bankTransferType** | [**BankTransferType**](BankTransferType.md) |  | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**eventId** | **Number** | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**eventType** | [**BankTransferEventType**](BankTransferEventType.md) |  | 
**failureReason** | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**originationAccountId** | **String** | The ID of the origination account that this balance belongs to. | 
**timestamp** | **Date** | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 


