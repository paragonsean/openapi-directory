# AdyenRecurringApi.NotifyShopperRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount of the upcoming payment. | 
**billingDate** | **String** | Date on which the subscription amount will be debited from the shopper. In YYYY-MM-DD format | [optional] 
**billingSequenceNumber** | **String** | Sequence of the debit. Depends on Frequency and Billing Attempts Rule. | [optional] 
**displayedReference** | **String** | Reference of Pre-debit notification that is displayed to the shopper. Optional field. Maps to reference if missing | [optional] 
**merchantAccount** | **String** | The merchant account identifier with which you want to process the transaction. | 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**reference** | **String** | Pre-debit notification reference sent by the merchant. This is a mandatory field | 
**shopperReference** | **String** | The ID that uniquely identifies the shopper.  This &#x60;shopperReference&#x60; must be the same as the &#x60;shopperReference&#x60; used in the initial payment. | 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 


