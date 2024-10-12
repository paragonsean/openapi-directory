

# BurnTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**burn** | [**List&lt;BurnTokenRequestBurnInner&gt;**](BurnTokenRequestBurnInner.md) | Array of objects representing tokens to be burned |  |
|**fee** | **BigDecimal** | Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL) |  |
|**from** | **List&lt;String&gt;** | Array of addresses to send the token from |  [optional] |
|**transfer** | [**List&lt;BurnTokenRequestTransferInner&gt;**](BurnTokenRequestTransferInner.md) |  |  [optional] |



