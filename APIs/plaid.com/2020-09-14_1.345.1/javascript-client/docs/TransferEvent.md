# ThePlaidApi.TransferEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID associated with the transfer. | 
**eventId** | **Number** | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**eventType** | [**TransferEventType**](TransferEventType.md) |  | 
**failureReason** | [**TransferFailure**](TransferFailure.md) |  | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**originationAccountId** | **String** | The ID of the origination account that this balance belongs to. | 
**originatorClientId** | **String** | The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the transfer was created on behalf of another client as a third-party sender (TPS). | 
**refundId** | **String** | Plaid’s unique identifier for a refund. A non-null value indicates the event is for the associated refund of the transfer. | 
**sweepAmount** | **String** | A signed amount of how much was &#x60;swept&#x60; or &#x60;return_swept&#x60; for this transfer (decimal string with two digits of precision e.g. \&quot;-5.50\&quot;). | 
**sweepId** | **String** | Plaid’s unique identifier for a sweep. | 
**timestamp** | **Date** | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**transferAmount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**transferId** | **String** | Plaid’s unique identifier for a transfer. | 
**transferType** | [**TransferType**](TransferType.md) |  | 


