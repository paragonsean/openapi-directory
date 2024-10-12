

# OrderListRequestWithoutPagination


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;Integer&gt;** | Account Id list |  [optional] |
|**beezUPOrderStatuses** | **List&lt;String&gt;** |  |  [optional] |
|**beginPeriodUtcDate** | **OffsetDateTime** | The begin period you want to make the search. \\ The period MUST not be greater than 62 days. The begin period MUST be lower than the end period.  |  |
|**dateSearchType** | **DateSearchType** |  |  [optional] |
|**endPeriodUtcDate** | **OffsetDateTime** | The end period of you search. \\ The period MUST not be greater than 62 days. \\ The end period MUST be greater than the begin period. The end period MUST be lower to the current date.  |  |
|**invoiceAvailabilityType** | **String** | Indicates on which invoice availability to filter |  [optional] |
|**marketplaceBusinessCodes** | **List&lt;String&gt;** |  |  [optional] |
|**marketplaceOrderIds** | **List&lt;String&gt;** |  |  [optional] |
|**marketplaceTechnicalCodes** | **List&lt;String&gt;** |  |  [optional] |
|**orderMerchantInfoSynchronizationStatus** | **String** | Indicates on which order merchant info synchronization status to filter |  [optional] |
|**orderBuyerName** | **String** | Buyer full name |  [optional] |
|**orderMerchantOrderIds** | **List&lt;String&gt;** | Merchant order id list |  [optional] |
|**storeIds** | **List&lt;String&gt;** | Store Id list |  [optional] |



