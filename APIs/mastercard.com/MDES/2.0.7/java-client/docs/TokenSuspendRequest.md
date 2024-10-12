

# TokenSuspendRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditInfo** | [**AuditInfo**](AuditInfo.md) |  |  |
|**commentText** | **String** | Comment related to suspension. |  [optional] |
|**reasonCode** | **String** | The reason for the action. Valid values:&lt;br /&gt;    \&quot;L\&quot; - Cardholder reported token device lost.&lt;br /&gt;    \&quot;S\&quot; - Cardholder reported token device stolen.&lt;br /&gt;    \&quot;T\&quot; - Issue or cardholder reported fraudulent token transactions.&lt;br /&gt;    \&quot;Z\&quot; - Other. |  |
|**tokenUniqueReference** | **String** | The TokenUniqueReference of the token. |  |



