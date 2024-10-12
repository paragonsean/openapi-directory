# NeblioRestApiSuite.IssueTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Number of tokens to issue | 
**divisibility** | **Number** | Number of decimal places the token should be divisble by (0-7) | 
**fee** | **Number** | Fee in satoshi to include in the issuance transaction min 1000000000 (10 NEBL) | 
**flags** | [**IssueTokenRequestFlags**](IssueTokenRequestFlags.md) |  | [optional] 
**issueAddress** | **String** | Address issuing the token | 
**metadata** | [**IssueTokenRequestMetadata**](IssueTokenRequestMetadata.md) |  | [optional] 
**reissuable** | **Boolean** | whether the token should be reissuable | 
**transfer** | [**[IssueTokenRequestTransferInner]**](IssueTokenRequestTransferInner.md) |  | 


