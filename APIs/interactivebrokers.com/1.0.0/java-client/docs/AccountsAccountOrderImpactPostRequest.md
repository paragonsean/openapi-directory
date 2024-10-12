

# AccountsAccountOrderImpactPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auxPrice** | **BigDecimal** | Required price to support Stop and Stop Limit orders |  [optional] |
|**contractId** | **BigDecimal** | The internal IB identifier for the trading product specified as an integer (can be obtained in response to /secdef request) |  [optional] |
|**currency** | **String** | The currency in which the FX pair trades (only for InstrumentType&#x3D;CASH) |  [optional] |
|**customerOrderId** | **String** | The order ID assigned by the customer. |  [optional] |
|**instrumentType** | **String** | The instrument type of the contract |  [optional] |
|**listingExchange** | **String** | The exchange on which the trading product is listed (only for InstrumentType&#x3D;STK) |  [optional] |
|**orderType** | **OrderType** |  |  [optional] |
|**price** | **BigDecimal** | The order price |  [optional] |
|**quantity** | **BigDecimal** | The number of units in the order; contracts or shares |  [optional] |
|**side** | [**SideEnum**](#SideEnum) | Buy &#x3D; &#39;1&#39;, Sell &#x3D; &#39;2&#39; |  [optional] |
|**ticker** | **String** | The symbol that identifies the trading product |  [optional] |
|**timeInForce** | **TimeInForce** |  |  [optional] |



## Enum: SideEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | new BigDecimal(&quot;1&quot;) |
| NUMBER_2 | new BigDecimal(&quot;2&quot;) |



