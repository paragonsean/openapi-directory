

# AccountsAccountOrdersPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auxPrice** | **BigDecimal** | Required Price to support Stop and Stop Limit orders |  [optional] |
|**contractId** | **BigDecimal** | The internal IB identifier for the trading product specified as an integer (can be obtained in response to /secdef request) |  [optional] |
|**currency** | **String** | The currency in which the FX pair trades (only for InstrumentType&#x3D;CASH) |  [optional] |
|**customerOrderId** | **String** | The order ID assigned by the customer. |  [optional] |
|**germanHftAlgo** | **Boolean** | By setting this bool to false the customer attests that the order is not subject to German HFT Act, was not generated using any automated algorithm, and no algorithm determined or changed financial instrument, side, quantity, order type, limit or other price, trading venue or timing of this order. Currently we cannot accept orders where this flag is set to true. Such orders will be rejected. |  [optional] |
|**instrumentType** | **String** | The instrument type of the contract |  [optional] |
|**listingExchange** | **String** | The exchange on which the trading product is listed (only for InstrumentType&#x3D;STK) |  [optional] |
|**mifid2Algo** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for algos that are responsible for investment decisions |  [optional] |
|**mifid2DecisionMaker** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for decision makers. |  [optional] |
|**mifid2ExecutionAlgo** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for algos that are responsible for handling/routing of the order. |  [optional] |
|**mifid2ExecutionTrader** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II person responsible for handling/routing of the order |  [optional] |
|**orderType** | **OrderType** |  |  [optional] |
|**orderRestrictions** | **BigDecimal** | MultiValueString representing the restrictions associated with an order. If more than one restriction is applicable to an order, this field can contain multiple instructions separated by space.  &#39;1&#39; Program Trade &#39;2&#39; Index Arbitrage  &#39;3&#39; Non-Index Arbitrage  |  [optional] |
|**outsideRTH** | **BigDecimal** | Indicates if order is active outside regular trading hours, where defined. 0 &#x3D; no (default), 1 &#x3D; yes |  [optional] |
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



