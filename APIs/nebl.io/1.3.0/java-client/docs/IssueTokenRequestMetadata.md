

# IssueTokenRequestMetadata

Object representing all metadata at token issuance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Long name or description of token (ex. Nibble) |  [optional] |
|**encryptions** | [**List&lt;IssueTokenRequestMetadataEncryptionsInner&gt;**](IssueTokenRequestMetadataEncryptionsInner.md) | Array of encryption instruction objects for encrypting userData |  [optional] |
|**issuer** | **String** | Name of token issuer |  [optional] |
|**rules** | [**IssueTokenRequestMetadataRules**](IssueTokenRequestMetadataRules.md) |  |  [optional] |
|**tokenName** | **String** | Token Symbol it will be identified by (ex. NIBBL) |  [optional] |
|**urls** | [**List&lt;IssueTokenRequestMetadataUrlsInner&gt;**](IssueTokenRequestMetadataUrlsInner.md) |  |  [optional] |
|**userData** | [**GetTokenMetadataResponseMetadataOfIssuanceDataUserData**](GetTokenMetadataResponseMetadataOfIssuanceDataUserData.md) |  |  [optional] |



