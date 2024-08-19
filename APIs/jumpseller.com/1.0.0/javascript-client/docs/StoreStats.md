# JumpsellerApi.StoreStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestSold** | [**[BestSold]**](BestSold.md) | Top 10 best sold products. | [optional] 
**conversions** | [**StoreStatsConversions**](StoreStatsConversions.md) |  | [optional] 
**currency** | **String** | Store currency. | [optional] 
**dailyVisits** | [**[DailyVisits]**](DailyVisits.md) | Visits per day. | [optional] 
**from** | **String** | Statistics start date. | [optional] 
**newVsReturningCustomers** | [**StoreStatsNewVsReturningCustomers**](StoreStatsNewVsReturningCustomers.md) |  | [optional] 
**newVsReturningOrders** | [**StoreStatsNewVsReturningCustomers**](StoreStatsNewVsReturningCustomers.md) |  | [optional] 
**orders** | [**StoreStatsOrders**](StoreStatsOrders.md) |  | [optional] 
**paymentMethods** | [**[PaymentMethodFreq]**](PaymentMethodFreq.md) | Store payment methods and their frequency. | [optional] 
**referrers** | [**[Referrer]**](Referrer.md) | Top 10 referrer sources and their frequency. | [optional] 
**regionOrders** | [**StoreStatsRegionOrders**](StoreStatsRegionOrders.md) |  | [optional] 
**searchFrequenciesAll** | **[Object]** | Number of times each search was conducted under the form of an aggregation query. | [optional] 
**searchFrequenciesWithoutResults** | **[Object]** | Number of times each search with zero results was conducted under the form of an aggregation query. | [optional] 
**shippingMethods** | [**[ShippingMethodFreq]**](ShippingMethodFreq.md) | Store shipping methods and their frequency. | [optional] 
**to** | **String** | Statistics end date. | [optional] 
**trafficType** | [**[TrafficType]**](TrafficType.md) | Type of store traffic and its frequency. | [optional] 
**visits** | **Number** | Total number of visits. | [optional] 


