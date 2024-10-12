# Ibkr3rdPartyWebApi.AccountsAccountOrderImpactPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxPrice** | **Number** | Required price to support Stop and Stop Limit orders | [optional] 
**contractId** | **Number** | The internal IB identifier for the trading product specified as an integer (can be obtained in response to /secdef request) | [optional] 
**currency** | **String** | The currency in which the FX pair trades (only for InstrumentType&#x3D;CASH) | [optional] 
**customerOrderId** | **String** | The order ID assigned by the customer. | [optional] 
**instrumentType** | **String** | The instrument type of the contract | [optional] 
**listingExchange** | **String** | The exchange on which the trading product is listed (only for InstrumentType&#x3D;STK) | [optional] 
**orderType** | [**OrderType**](OrderType.md) |  | [optional] 
**price** | **Number** | The order price | [optional] 
**quantity** | **Number** | The number of units in the order; contracts or shares | [optional] 
**side** | **Number** | Buy &#x3D; &#39;1&#39;, Sell &#x3D; &#39;2&#39; | [optional] 
**ticker** | **String** | The symbol that identifies the trading product | [optional] 
**timeInForce** | [**TimeInForce**](TimeInForce.md) |  | [optional] 



## Enum: SideEnum


* `1` (value: `1`)

* `2` (value: `2`)




