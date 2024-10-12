

# GetMarket200ResponseDataTradeGoodsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**purchasePrice** | **Integer** | The price at which this good can be purchased from the market. |  |
|**sellPrice** | **Integer** | The price at which this good can be sold to the market. |  |
|**supply** | [**SupplyEnum**](#SupplyEnum) | A rough estimate of the total supply of this good in the marketplace. |  |
|**symbol** | **String** | The symbol of the trade good. |  |
|**tradeVolume** | **Integer** | The typical volume flowing through the market for this type of good. The larger the trade volume, the more stable prices will be. |  |



## Enum: SupplyEnum

| Name | Value |
|---- | -----|
| SCARCE | &quot;SCARCE&quot; |
| LIMITED | &quot;LIMITED&quot; |
| MODERATE | &quot;MODERATE&quot; |
| ABUNDANT | &quot;ABUNDANT&quot; |



