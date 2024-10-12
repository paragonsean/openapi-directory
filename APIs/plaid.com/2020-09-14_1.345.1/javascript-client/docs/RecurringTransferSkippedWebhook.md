# ThePlaidApi.RecurringTransferSkippedWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationDecision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**authorizationDecisionRationaleCode** | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) |  | [optional] 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**recurringTransferId** | **String** | Plaid’s unique identifier for a recurring transfer. | 
**skippedOriginationDate** | **Date** | The planned date on which Plaid is unable to originate a new ACH transaction of the recurring transfer. This will be of the form YYYY-MM-DD. | 
**webhookCode** | **String** | &#x60;RECURRING_TRANSFER_SKIPPED&#x60; | 
**webhookType** | **String** | &#x60;TRANSFER&#x60; | 


