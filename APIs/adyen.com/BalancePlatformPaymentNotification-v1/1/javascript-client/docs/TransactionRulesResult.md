# PaymentWebhooksDeprecated.TransactionRulesResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advice** | **String** | The advice given by the Risk analysis. | [optional] 
**allRulesPassed** | **Boolean** | Indicates whether the transaction passed the evaluation for all transaction rules. | [optional] 
**failedTransactionRules** | [**[TransactionEventViolation]**](TransactionEventViolation.md) | Array containing all the transaction rules that the transaction violated. This list is only sent when &#x60;allRulesPassed&#x60; is **false**. | [optional] 
**score** | **Number** | The score of the Risk analysis. | [optional] 


