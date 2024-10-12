

# ServiceStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgBasketSize** | **Integer** | Average size of a basket in the system, empty baskets are not taken into account |  [optional] |
|**basketsCount** | **Integer** | Total number of baskets managed by service |  [optional] |
|**emptyBasketsCount** | **Integer** | Number of empty baskets |  [optional] |
|**maxBasketSize** | **Integer** | Size of the biggest basket that processed the top most number of HTTP requests |  [optional] |
|**requestsCount** | **Integer** | Number of HTTP requests currently stored by service |  [optional] |
|**requestsTotalCount** | **Integer** | Total number of HTTP requests processed by service |  [optional] |
|**topBasketsRecent** | [**List&lt;BasketInfo&gt;**](BasketInfo.md) | Collection of top baskets recently active |  [optional] |
|**topBasketsSize** | [**List&lt;BasketInfo&gt;**](BasketInfo.md) | Collection of top basket by size |  [optional] |



