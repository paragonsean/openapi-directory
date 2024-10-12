# SpaceTradersApi.GetMarket200ResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | **[Object]** | The list of goods that are bought and sold between agents at this market. | 
**exports** | [**[GetMarket200ResponseDataExportsInner]**](GetMarket200ResponseDataExportsInner.md) | The list of goods that are exported from this market. | 
**imports** | **[Object]** | The list of goods that are sought as imports in this market. | 
**symbol** | **String** | The symbol of the market. The symbol is the same as the waypoint where the market is located. | 
**tradeGoods** | [**[GetMarket200ResponseDataTradeGoodsInner]**](GetMarket200ResponseDataTradeGoodsInner.md) | The list of goods that are traded at this market. Visible only when a ship is present at the market. | [optional] 
**transactions** | [**[GetMarket200ResponseDataTransactionsInner]**](GetMarket200ResponseDataTransactionsInner.md) | The list of recent transactions at this market. Visible only when a ship is present at the market. | [optional] 


