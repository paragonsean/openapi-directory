

# AccountHolderMessagingRequestSchema


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditInfo** | [**AuditInfo**](AuditInfo.md) |  |  |
|**issuerApplicationMessageDisplay** | **String** | This is the indicator if the message can be viewed in the Issuer Application using the MessageIdentifier. &lt;br&gt;Please refer to the Apple Card Notification Specification for Notification Deep Linking. Mandatory field.  Valid values are;&lt;br&gt;TRUE ? The message can be viewed in the issuer application&lt;br&gt;FALSE ? The message cannot be viewed in the issuer application. |  |
|**messageExpiration** | **String** | Date and time after which the message is no longer valid.  Maximum value of 30 days in the future. Mandatory field.  __ISO 8601 format ? YYYY-MM-DDThh:mm:ssTZD__ |  |
|**messageIdentifier** | **String** | This is the message identifier. This could be used for linking into the issuer application. Mandatory field. |  |
|**messageLanguageCode** | **String** | The language of the message.  Only messages with the requested language code will be presented to the account holder. Mandatory field.  &lt;br&gt;__ISO 639-1 format__ |  |
|**messageText** | **String** | This is the message which will be displayed to the cardholder. Mandatory field. |  |
|**tokenUniqueReference** | **String** | When present, the search will return one specific matching token. Cannot be used together with any of the following search request parameters; AccountPan, Token, PaymentAppInstanceId, CommentId, or AlternateAccountIdentifier. Mandatory field. |  |



