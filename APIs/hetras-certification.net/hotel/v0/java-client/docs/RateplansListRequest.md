

# RateplansListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseRateplan** | **String** | Return all rateplans having the specified rateplan as base rateplan |  [optional] |
|**channelCode** | **String** | Return all rateplans sold through the specified channel |  [optional] |
|**channelGroup** | **String** | Return all rateplans that are sold through at least one channel out of the specified channel group |  [optional] |
|**commissionable** | **Boolean** | Return all rateplans having commisionable status |  [optional] |
|**group** | **String** | Return all rateplans belonging to the specified rateplan group |  [optional] |
|**includedServices** | **List&lt;String&gt;** | Return all rateplans having at least one of the specified services included |  [optional] |
|**marketCodes** | **List&lt;String&gt;** | Return all rateplans having one of the specified values as a market code |  [optional] |
|**roomTypes** | **List&lt;String&gt;** | Return all rateplans by which at least one of the specified room types are sold |  [optional] |
|**sellingStatus** | [**SellingStatusEnum**](#SellingStatusEnum) | Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans. |  [optional] |



## Enum: SellingStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |
| ALL | &quot;All&quot; |



