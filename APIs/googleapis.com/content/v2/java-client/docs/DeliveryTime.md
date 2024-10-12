

# DeliveryTime


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cutoffTime** | [**CutoffTime**](CutoffTime.md) |  |  [optional] |
|**handlingBusinessDayConfig** | [**BusinessDayConfig**](BusinessDayConfig.md) |  |  [optional] |
|**holidayCutoffs** | [**List&lt;HolidayCutoff&gt;**](HolidayCutoff.md) | Holiday cutoff definitions. If configured, they specify order cutoff times for holiday-specific shipping. |  [optional] |
|**maxHandlingTimeInDays** | **Integer** | Maximum number of business days spent before an order is shipped. 0 means same day shipped, 1 means next day shipped. Must be greater than or equal to &#x60;minHandlingTimeInDays&#x60;. |  [optional] |
|**maxTransitTimeInDays** | **Integer** | Maximum number of business days that is spent in transit. 0 means same day delivery, 1 means next day delivery. Must be greater than or equal to &#x60;minTransitTimeInDays&#x60;. |  [optional] |
|**minHandlingTimeInDays** | **Integer** | Minimum number of business days spent before an order is shipped. 0 means same day shipped, 1 means next day shipped. |  [optional] |
|**minTransitTimeInDays** | **Integer** | Minimum number of business days that is spent in transit. 0 means same day delivery, 1 means next day delivery. Either &#x60;{min,max}TransitTimeInDays&#x60; or &#x60;transitTimeTable&#x60; must be set, but not both. |  [optional] |
|**transitBusinessDayConfig** | [**BusinessDayConfig**](BusinessDayConfig.md) |  |  [optional] |
|**transitTimeTable** | [**TransitTable**](TransitTable.md) |  |  [optional] |
|**warehouseBasedDeliveryTimes** | [**List&lt;WarehouseBasedDeliveryTime&gt;**](WarehouseBasedDeliveryTime.md) | Indicates that the delivery time should be calculated per warehouse (shipping origin location) based on the settings of the selected carrier. When set, no other transit time related field in DeliveryTime should be set. |  [optional] |



