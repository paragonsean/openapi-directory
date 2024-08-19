# ThePlaidApi.WalletTransactionStatusUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**newStatus** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**oldStatus** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**paymentId** | **String** | The &#x60;payment_id&#x60; associated with the transaction. This will be present in case of &#x60;REFUND&#x60; and &#x60;PIS_PAY_IN&#x60; | [optional] 
**timestamp** | **Date** | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. &#x60;\&quot;2017-09-14T14:42:19.350Z\&quot;&#x60; | 
**transactionId** | **String** | The &#x60;transaction_id&#x60; for the wallet transaction being updated | 
**walletId** | **String** | The EMI (E-Money Institution) wallet that this payment is associated with. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**webhookCode** | **String** | &#x60;WALLET_TRANSACTION_STATUS_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;WALLET&#x60; | 


