

# TransactionTotals

If Result is Success, contains all the totals, classified as required by the Sale in the message request. At least, transaction totals are provided per Acquirer, Acquirer Settlement, and Card Brand. Result of the Sale to POI Reconciliation processing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acquirerID** | **Integer** | If available. |  [optional] |
|**cardBrand** | **String** | If configured to present totals per card brand, and Response.Result is Success. |  [optional] |
|**hostReconciliationID** | **String** | If available. |  [optional] |
|**loyaltyCurrency** | **String** | If LoyaltyUnit is Monetary. |  [optional] |
|**loyaltyTotals** | [**List&lt;LoyaltyTotals&gt;**](LoyaltyTotals.md) |  |  [optional] |
|**loyaltyUnit** | **LoyaltyUnit** |  |  [optional] |
|**operatorID** | **String** | If requested in the message request. |  [optional] |
|**POIID** | **String** | If requested in the message request. |  [optional] |
|**paymentCurrency** | **String** | Currency of a monetary amount. |  [optional] |
|**paymentInstrumentType** | **PaymentInstrumentType** |  |  |
|**paymentTotals** | [**List&lt;PaymentTotals&gt;**](PaymentTotals.md) |  |  [optional] |
|**saleID** | **String** | If requested in the message request. |  [optional] |
|**shiftNumber** | **String** | If requested in the message request. |  [optional] |
|**totalsGroupID** | **String** | If requested in the message request. |  [optional] |



