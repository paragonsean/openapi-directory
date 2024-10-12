

# AccountsAccountOrdersCustomerOrderIdPutRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auxPrice** | **BigDecimal** | Required Price to support Stop and Stop Limit orders |  [optional] |
|**customerOrderId** | **String** | The new order ID assigned by the customer for the modification. |  [optional] |
|**germanHftAlgo** | **Boolean** | By setting this bool to false the customer attests that the order is not subject to German HFT Act, was not generated using any automated algorithm, and no algorithm determined or changed financial instrument, side, quantity, order type, limit or other price, trading venue or timing of this order. Currently we cannot accept orders where this flag is set to true. Such orders will be rejected. |  [optional] |
|**mifid2Algo** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for algos that are responsible for investment decisions |  [optional] |
|**mifid2DecisionMaker** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for decision makers. |  [optional] |
|**mifid2ExecutionAlgo** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II short code for algos that are responsible for handling/routing of the order. |  [optional] |
|**mifid2ExecutionTrader** | **String** | This field permits specification of the user&#39;s preregistered (via account management) MiFID II person responsible for handling/routing of the order |  [optional] |
|**orderType** | **OrderType** |  |  [optional] |
|**origCustomerOrderId** | **String** | The order ID assigned by the customer |  [optional] |
|**outsideRTH** | **BigDecimal** | Indicates if order is active outside regular trading hours, where defined. 0 &#x3D; no (default), 1 &#x3D; yes |  [optional] |
|**price** | **BigDecimal** | The order price |  [optional] |
|**quantity** | **BigDecimal** | The number of units in the order; contracts or shares |  [optional] |
|**side** | [**SideEnum**](#SideEnum) | Buy &#x3D; &#39;1&#39;, Sell &#x3D; &#39;2&#39; |  [optional] |
|**timeInForce** | **TimeInForce** |  |  [optional] |



## Enum: SideEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | new BigDecimal(&quot;1&quot;) |
| NUMBER_2 | new BigDecimal(&quot;2&quot;) |



