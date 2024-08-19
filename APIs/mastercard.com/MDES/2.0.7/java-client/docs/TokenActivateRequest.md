

# TokenActivateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountPan** | **Integer** | The Account PAN of the token to be activated. Conditional field, must be present when PaymentAppInstanceId is present, must not be present when TokenUniqueReference is present. |  [optional] |
|**auditInfo** | [**AuditInfo**](AuditInfo.md) |  |  |
|**commentText** | **Integer** | Comment related to activating this token. |  [optional] |
|**paymentAppInstanceId** | **Integer** | Identifier of the Payment App instance within a device that will be provisioned with a token. &lt;br&gt;&lt;br&gt;_Note:_ This may contain the identifier of the Secure Element or a mobile device for some programs. Conditional field, must be present when AccountPan is present. Must not be present when TokenUniqueReference is present. |  [optional] |
|**reasonCode** | **String** | Reason for the activation. Valid values:&lt;br /&gt;    \&quot;A\&quot; &#x3D; Cardholder successfully authenticated prior to activation.&lt;br /&gt;    \&quot;C\&quot; &#x3D; Cardholder successfully authenticated with a customer service agent prior to activation. |  |
|**tokenUniqueReference** | **String** | TokenUniqueReference for the token to be activated. Conditional field, present when AccountPan and PaymentAppInstanceId are not present. |  [optional] |



