

# TicketOffer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**AvailabilityEnum**](#AvailabilityEnum) |  |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**donation** | **Boolean** |  |  [optional] |
|**fee** | **BigDecimal** |  |  [optional] |
|**highPrice** | **BigDecimal** |  |  [optional] |
|**inventory** | [**TicketOfferInventory**](TicketOfferInventory.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**price** | **BigDecimal** |  |  [optional] |
|**priceCurrency** | **String** |  |  [optional] |
|**priceUnknown** | **Boolean** |  |  [optional] |
|**url** | **String** |  |  [optional] |



## Enum: AvailabilityEnum

| Name | Value |
|---- | -----|
| DISCONTINUED | &quot;Discontinued&quot; |
| IN_STOCK | &quot;InStock&quot; |
| IN_STORE_ONLY | &quot;InStoreOnly&quot; |
| LIMITED_AVAILABILITY | &quot;LimitedAvailability&quot; |
| ONLINE_ONLY | &quot;OnlineOnly&quot; |
| OUT_OF_STOCK | &quot;OutOfStock&quot; |
| PRE_ORDER | &quot;PreOrder&quot; |
| SOLD_OUT | &quot;SoldOut&quot; |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| SECONDARY | &quot;secondary&quot; |
| PRESALE | &quot;presale&quot; |
| MEMBER | &quot;member&quot; |
| PREMIUM | &quot;premium&quot; |
| UNKNOWN | &quot;unknown&quot; |



