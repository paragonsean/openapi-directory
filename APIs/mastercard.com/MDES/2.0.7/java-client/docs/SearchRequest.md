

# SearchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountPan** | **String** | When present, the search will return tokens for the Account matching this Primary Account Number (PAN), for any Wallet Provider or device. Cannot be used together with any of the following search request.  parameters:TokenUniqueReference, Token, PaymentAppInstanceId, CommentId, or AlternateAccountIdentifier. |  [optional] |
|**alternateAccountIdentifier** | **String** | When present, the search will return tokens matching this Alternate Account Identifier, for any Wallet Provider or device. Space characters are not allowed. Cannot be used together with any of the following search request parameters; AccountPan, TokenUniqueReference, Token, PaymentAppInstanceId, or CommentId. |  [optional] |
|**auditInfo** | [**AuditInfo**](AuditInfo.md) |  |  |
|**commentId** | **String** | When present, the search will return one specific token linked to the comment. Cannot be used together with any of the following search request parameters; AccountPan, TokenUniqueReference, Token, PaymentAppInstanceId, or AlternateAccountIdentifier. |  [optional] |
|**excludeDeletedIndicator** | [**ExcludeDeletedIndicatorEnum**](#ExcludeDeletedIndicatorEnum) | Indicates whether deleted tokens should be excluded from the search results. When omitted, deleted tokens are included in the results. \&quot;true\&quot; indicates deleted tokens are excluded from the search results. \&quot;false\&quot; means deleted tokens are included in the search results. |  [optional] |
|**paymentAppInstanceId** | **String** | When present, the search will return tokens already present or to be provisioned to the specified Payment App instance.&lt;br&gt;&lt;br&gt;_Note:_ This may contain the identifier of the Secure Element or a mobile device for some programs. Cannot be used together with any of the following search request parameters; AccountPan, TokenUniqueReference, Token, CommentId, or AlternateAccountIdentifier. |  [optional] |
|**token** | **String** | When present, the search will return one specific token. Cannot be used together with any of the following search request parameters; AccountPan, TokenUniqueReference, PaymentAppInstanceId, CommentId, or AlternateAccountIdentifier. |  [optional] |
|**tokenUniqueReference** | **String** | When present, the search will return one specific matching token. Cannot be used together with any of the following search request parameters; AccountPan, Token, PaymentAppInstanceId, CommentId, or AlternateAccountIdentifier. |  [optional] |



## Enum: ExcludeDeletedIndicatorEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



