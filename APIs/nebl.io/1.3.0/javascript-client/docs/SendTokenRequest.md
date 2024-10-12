# NeblioRestApiSuite.SendTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **Number** | Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL) | 
**flags** | [**IssueTokenRequestFlags**](IssueTokenRequestFlags.md) |  | [optional] 
**from** | **[String]** | Array of addresses to send the token from | [optional] 
**metadata** | [**IssueTokenRequestMetadata**](IssueTokenRequestMetadata.md) |  | [optional] 
**sendutxo** | **[String]** | Array of UTXOs to send the token from | [optional] 
**to** | [**[BurnTokenRequestTransferInner]**](BurnTokenRequestTransferInner.md) |  | 


