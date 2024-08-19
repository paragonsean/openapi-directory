# AdyenTerminalApi.TransactionTotals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirerID** | **Number** | If available. | [optional] 
**cardBrand** | **String** | If configured to present totals per card brand, and Response.Result is Success. | [optional] 
**hostReconciliationID** | **String** | If available. | [optional] 
**loyaltyCurrency** | **String** | If LoyaltyUnit is Monetary. | [optional] 
**loyaltyTotals** | [**[LoyaltyTotals]**](LoyaltyTotals.md) |  | [optional] 
**loyaltyUnit** | [**LoyaltyUnit**](LoyaltyUnit.md) |  | [optional] 
**operatorID** | **String** | If requested in the message request. | [optional] 
**POIID** | **String** | If requested in the message request. | [optional] 
**paymentCurrency** | **String** | Currency of a monetary amount. | [optional] 
**paymentInstrumentType** | [**PaymentInstrumentType**](PaymentInstrumentType.md) |  | 
**paymentTotals** | [**[PaymentTotals]**](PaymentTotals.md) |  | [optional] 
**saleID** | **String** | If requested in the message request. | [optional] 
**shiftNumber** | **String** | If requested in the message request. | [optional] 
**totalsGroupID** | **String** | If requested in the message request. | [optional] 


