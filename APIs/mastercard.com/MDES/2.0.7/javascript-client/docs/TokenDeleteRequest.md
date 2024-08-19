# MdesCustomerService.TokenDeleteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditInfo** | [**AuditInfo**](AuditInfo.md) |  | 
**commentText** | **String** | Comment related to deletion. | [optional] 
**reasonCode** | **String** | The reason for the action. Valid values:&lt;br /&gt;    \&quot;L\&quot; - Cardholder confirmed token device lost&lt;br /&gt;    \&quot;S\&quot; - Cardholder confirmed token device stolen&lt;br /&gt;    \&quot;F\&quot; - Issuer or cardholder confirmed fraudulent token transactions (Deprecated)&lt;br /&gt;    \&quot;T\&quot; - Issuer or cardholder confirmed fraudulent token transactions&lt;br /&gt;    \&quot;C\&quot; - Account closed&lt;br /&gt;    \&quot;Z\&quot; - Other | 
**tokenUniqueReference** | **String** | The TokenUniqueReference of the token. | 


