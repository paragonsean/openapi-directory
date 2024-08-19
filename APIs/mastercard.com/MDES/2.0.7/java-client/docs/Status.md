

# Status


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditInfo** | [**AuditInfo**](AuditInfo.md) |  |  [optional] |
|**commentId** | **String** | Identifier of the comment added.  Conditional field, only present when comment text was provided in the request. |  [optional] |
|**initiator** | **String** | Party that initiated the status update. Valid values:&lt;br /&gt;    \&quot;I\&quot; - Issuer.&lt;br /&gt;    \&quot;W\&quot; - Token Requestor (including Wallet Provider).&lt;br /&gt;    \&quot;C\&quot; - Cardholder.&lt;br /&gt;    \&quot;P\&quot; - Mobile PIN Validation service.&lt;br /&gt;    \&quot;M\&quot; - Mobile PIN Change Validation service. |  [optional] |
|**reasonCode** | **String** | Reason for the status update.  Valid values:&lt;br /&gt;    \&quot;A\&quot; ? Cardholder successfully authenticated using a mobile App prior to activation.&lt;br /&gt;    \&quot;C\&quot; ? Cardholder successfully authenticated with a customer service agent prior to activation. (For &#39;Token Activate&#39;).&lt;br /&gt;    \&quot;C\&quot; ? Account closed. (For &#39;Token Delete&#39;).&lt;br /&gt;    \&quot;F\&quot; ? Cardholder reported token device found or not stolen.&lt;br /&gt;    \&quot;L\&quot; ? Cardholder reported/confirmed token device lost.&lt;br /&gt;    \&quot;S\&quot; ? Cardholder reported/confirmed token device stolen.&lt;br /&gt;    \&quot;T\&quot; ? Issuer or cardholder reported fraudulent/then confirmed no fraudulent token transactions.&lt;br /&gt;    \&quot;Z\&quot; ? Other. |  [optional] |
|**statusCode** | **String** | The status of the Token. Valid values:&lt;br /&gt;    \&quot;U\&quot; - Unmapped. The token has not yet been linked to the Account PAN. The process of tokenization is ?In Progress?.&lt;br /&gt;    \&quot;A\&quot; - Active. The token is linked to the Account PAN and may initiate new transactions to be authorized.&lt;br /&gt;    \&quot;S\&quot; - Suspended. The token is linked to the Account PAN but may not perform transactions at the request of one or more suspenders.&lt;br /&gt;    \&quot;D\&quot; - Deleted. The token is logically deleted but is still linked to the Account PAN for the purposes of post-authorization transaction processing. |  [optional] |
|**statusDateTime** | **String** | Date and time the status was updated. String, ISO 8691 format - YYYY-MM-DDThh:mm:ssTZD . |  [optional] |
|**statusDescription** | **String** | Description of the current status. |  [optional] |



