# RequestBasketsApi.ServiceStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgBasketSize** | **Number** | Average size of a basket in the system, empty baskets are not taken into account | [optional] 
**basketsCount** | **Number** | Total number of baskets managed by service | [optional] 
**emptyBasketsCount** | **Number** | Number of empty baskets | [optional] 
**maxBasketSize** | **Number** | Size of the biggest basket that processed the top most number of HTTP requests | [optional] 
**requestsCount** | **Number** | Number of HTTP requests currently stored by service | [optional] 
**requestsTotalCount** | **Number** | Total number of HTTP requests processed by service | [optional] 
**topBasketsRecent** | [**[BasketInfo]**](BasketInfo.md) | Collection of top baskets recently active | [optional] 
**topBasketsSize** | [**[BasketInfo]**](BasketInfo.md) | Collection of top basket by size | [optional] 


