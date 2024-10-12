

# SendTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fee** | **BigDecimal** | Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL) |  |
|**flags** | [**IssueTokenRequestFlags**](IssueTokenRequestFlags.md) |  |  [optional] |
|**from** | **List&lt;String&gt;** | Array of addresses to send the token from |  [optional] |
|**metadata** | [**IssueTokenRequestMetadata**](IssueTokenRequestMetadata.md) |  |  [optional] |
|**sendutxo** | **List&lt;String&gt;** | Array of UTXOs to send the token from |  [optional] |
|**to** | [**List&lt;BurnTokenRequestTransferInner&gt;**](BurnTokenRequestTransferInner.md) |  |  |



