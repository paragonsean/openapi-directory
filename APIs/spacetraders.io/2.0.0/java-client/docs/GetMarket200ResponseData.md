

# GetMarket200ResponseData



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exchange** | **List&lt;Object&gt;** | The list of goods that are bought and sold between agents at this market. |  |
|**exports** | [**List&lt;GetMarket200ResponseDataExportsInner&gt;**](GetMarket200ResponseDataExportsInner.md) | The list of goods that are exported from this market. |  |
|**imports** | **List&lt;Object&gt;** | The list of goods that are sought as imports in this market. |  |
|**symbol** | **String** | The symbol of the market. The symbol is the same as the waypoint where the market is located. |  |
|**tradeGoods** | [**List&lt;GetMarket200ResponseDataTradeGoodsInner&gt;**](GetMarket200ResponseDataTradeGoodsInner.md) | The list of goods that are traded at this market. Visible only when a ship is present at the market. |  [optional] |
|**transactions** | [**List&lt;GetMarket200ResponseDataTransactionsInner&gt;**](GetMarket200ResponseDataTransactionsInner.md) | The list of recent transactions at this market. Visible only when a ship is present at the market. |  [optional] |



