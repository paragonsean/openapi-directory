# BeezUpMerchantApi.OrderListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountIds** | **[Number]** | Account Id list | [optional] 
**beezUPOrderStatuses** | **[String]** |  | [optional] 
**beginPeriodUtcDate** | **Date** | The begin period you want to make the search. \\ The period MUST not be greater than 62 days. The begin period MUST be lower than the end period.  | 
**dateSearchType** | [**DateSearchType**](DateSearchType.md) |  | [optional] 
**endPeriodUtcDate** | **Date** | The end period of you search. \\ The period MUST not be greater than 62 days. \\ The end period MUST be greater than the begin period. The end period MUST be lower to the current date.  | 
**invoiceAvailabilityType** | **String** | Indicates on which invoice availability to filter | [optional] 
**marketplaceBusinessCodes** | **[String]** |  | [optional] 
**marketplaceOrderIds** | **[String]** |  | [optional] 
**marketplaceTechnicalCodes** | **[String]** |  | [optional] 
**orderMerchantInfoSynchronizationStatus** | **String** | Indicates on which order merchant info synchronization status to filter | [optional] 
**orderBuyerName** | **String** | Buyer full name | [optional] 
**orderMerchantOrderIds** | **[String]** | Merchant order id list | [optional] 
**storeIds** | **[String]** | Store Id list | [optional] 
**pageNumber** | **Number** | Indicates the page number | 
**pageSize** | **Number** | Indicate the order count per page | 


