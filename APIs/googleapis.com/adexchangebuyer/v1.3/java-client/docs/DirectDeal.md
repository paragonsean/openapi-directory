

# DirectDeal

The configuration data for an Ad Exchange direct deal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Integer** | The account id of the buyer this deal is for. |  [optional] |
|**advertiser** | **String** | The name of the advertiser this deal is for. |  [optional] |
|**allowsAlcohol** | **Boolean** | Whether the publisher for this deal is eligible for alcohol ads. |  [optional] |
|**buyerAccountId** | **String** | The account id that this deal was negotiated for. It is either the buyer or the client that this deal was negotiated on behalf of. |  [optional] |
|**currencyCode** | **String** | The currency code that applies to the fixed_cpm value. If not set then assumed to be USD. |  [optional] |
|**dealTier** | **String** | The deal type such as programmatic reservation or fixed price and so on. |  [optional] |
|**endTime** | **String** | End time for when this deal stops being active. If not set then this deal is valid until manually disabled by the publisher. In seconds since the epoch. |  [optional] |
|**fixedCpm** | **String** | The fixed price for this direct deal. In cpm micros of currency according to currency_code. If set, then this deal is eligible for the fixed price tier of buying (highest priority, pay exactly the configured fixed price). |  [optional] |
|**id** | **String** | Deal id. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**name** | **String** | Deal name. |  [optional] |
|**privateExchangeMinCpm** | **String** | The minimum price for this direct deal. In cpm micros of currency according to currency_code. If set, then this deal is eligible for the private exchange tier of buying (below fixed price priority, run as a second price auction). |  [optional] |
|**publisherBlocksOverriden** | **Boolean** | If true, the publisher has opted to have their blocks ignored when a creative is bid with for this deal. |  [optional] |
|**sellerNetwork** | **String** | The name of the publisher offering this direct deal. |  [optional] |
|**startTime** | **String** | Start time for when this deal becomes active. If not set then this deal is active immediately upon creation. In seconds since the epoch. |  [optional] |



