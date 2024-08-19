# MdesCustomerService.TokenUnsuspendRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditInfo** | [**AuditInfo**](AuditInfo.md) |  | 
**commentText** | **String** | Comment related to unsuspension. | [optional] 
**reasonCode** | **String** | The reason for the action. Valid values:&lt;br /&gt;    \&quot;F\&quot; - Cardholder reported token device found or not stolen&lt;br /&gt;    \&quot;T\&quot; - Issuer or cardholder confirmed no fraudulent token transactions&lt;br /&gt;    \&quot;Z\&quot; - Other. | 
**tokenUniqueReference** | **String** | The TokenUniqueReference of the token. | 


