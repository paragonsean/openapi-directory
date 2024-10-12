# ThePlaidApi.WalletTransactionGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**WalletTransactionAmount**](WalletTransactionAmount.md) |  | 
**counterparty** | [**WalletTransactionCounterparty**](WalletTransactionCounterparty.md) |  | 
**createdAt** | **Date** | Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**lastStatusUpdate** | **Date** | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | 
**paymentId** | **String** | The payment id that this transaction is associated with, if any. This is present only for transaction types &#x60;PIS_PAY_IN&#x60; and &#x60;REFUND&#x60;. | [optional] 
**reference** | **String** | A reference for the transaction | 
**status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**transactionId** | **String** | A unique ID identifying the transaction | 
**type** | **String** | The type of the transaction. The supported transaction types that are returned are: &#x60;BANK_TRANSFER:&#x60; a transaction which credits an e-wallet through an external bank transfer.  &#x60;PAYOUT:&#x60; a transaction which debits an e-wallet by disbursing funds to a counterparty.  &#x60;PIS_PAY_IN:&#x60; a payment which credits an e-wallet through Plaid&#39;s Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;REFUND:&#x60; a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid&#39;s [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;FUNDS_SWEEP&#x60;: an automated transaction which debits funds from an e-wallet to a designated client-owned account. | 
**walletId** | **String** | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 



## Enum: TypeEnum


* `BANK_TRANSFER` (value: `"BANK_TRANSFER"`)

* `PAYOUT` (value: `"PAYOUT"`)

* `PIS_PAY_IN` (value: `"PIS_PAY_IN"`)

* `REFUND` (value: `"REFUND"`)

* `FUNDS_SWEEP` (value: `"FUNDS_SWEEP"`)




