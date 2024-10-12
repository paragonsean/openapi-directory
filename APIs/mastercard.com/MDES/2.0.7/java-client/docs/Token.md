

# Token


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountPanSequenceNumber** | **String** | The Account PAN Sequence Number associated with a specific token, as provided to MDES previously by the issuer. It may be used to distinguish between multiple cardholders for a single Account PAN, to represent an issuance number of a specific card, or to distinguish between different card products, such as debit or credit, that share the same Account PAN. Conditional field, present when successfully assigned. Supported values - 00 to 99. |  [optional] |
|**activationCodeExpirationDateTime** | **String** | Date and time when an Activation Code will expire. Conditional field, not present for CoF tokens, and only present when an Activation Code has been generated and activation has not yet occurred. The date and time may be in the future or past. string in ISO 8601 format ? YYYY-MM-DDThh:mm:ssTZD . |  [optional] |
|**correlationId** | **String** | Value linking pre-digitization messages generated during provisioning. Conditional field, not present for CoF tokens. |  [optional] |
|**currentStatusCode** | **String** | Current status of the Token. Valid values:&lt;br&gt; \&quot;U\&quot; - Unmapped. The token has not yet been linked to the Account PAN. The process of tokenization is ?In Progress.&#39;&lt;br&gt; \&quot;A\&quot; - Active. The token is linked to the Account PAN and may initiate new transactions to be authorized.&lt;br&gt; \&quot;S\&quot; - Suspended. The token is linked to the Account PAN but may not perform transactions at the request of one or more suspenders.&lt;br&gt; \&quot;D\&quot; - Deleted. The token is logically deleted but is still linked to the Account PAN for the purposes of post-authorization transaction processing. |  [optional] |
|**currentStatusDateTime** | **String** | Date and time the status was updated.  string, ISO 8601 format ? YYYY-MM-DDThh:mm:ssTZD . |  [optional] |
|**currentStatusDescription** | **String** | Description of the current status. |  [optional] |
|**device** | [**Device**](Device.md) |  |  [optional] |
|**digitizationRequestDateTime** | **String** | Date and time of the initial request for digitization of the Account PAN for this token. Conditional field, not present for CoF tokens. string, in ISO 8601 format ? YYYY-MM-DDThh:mm:ssTZD . |  [optional] |
|**expirationDate** | **String** | Expiration date of token. Conditional field, present once the token has been designated for the digitization. Four digit string. Format \&quot;mmyy\&quot;. |  [optional] |
|**finalTokenizationDecision** | **String** | Final decision related to the digitization of the Account PAN for this token. Valid values:&lt;br /&gt;    \&quot;D\&quot; - Digitization was declined&lt;br /&gt;    \&quot;A\&quot; - Digitization was approved&lt;br /&gt;    \&quot;R\&quot; - Digitization was approved but required authentication prior to activation.&lt;br /&gt;Conditional field, not present for CoF tokens.&lt;br&gt;&lt;br&gt;_Note:_this information is currently subject to archival processes and will be present for only 1 year following digitization. |  [optional] |
|**lastCommentId** | **String** | Identifier of the last comment associated with the token. |  [optional] |
|**paymentAppInstanceId** | **String** | Identifier of the Payment App instance within a device that will be provisioned with a token.&lt;br&gt;&lt;br&gt;_Note:_ This may contain the identifier of the Secure Element or a mobile device for some programs. Optional, not present for CoF tokens, and only present when supplied by the Payment App Provider. |  [optional] |
|**primaryAccountNumberUniqueReference** | **String** | Unique reference to the Account PAN originally digitized. Conditional field, present when successfully assigned. |  [optional] |
|**provisioningStatusCode** | **String** | Current provisioning status of the token. Valid values:&lt;br /&gt;    \&quot;P\&quot; - Token being prepared&lt;br /&gt;    \&quot;T\&quot; - Awaiting cardholder acceptance of Terms and Conditions&lt;br /&gt;    \&quot;D\&quot; - Token being delivered to Wallet Provider or Device&lt;br /&gt;    \&quot;A\&quot; - Awaiting Activation&lt;br /&gt;    \&quot;S\&quot; - Provisioning successful&lt;br /&gt;    \&quot;F\&quot; - Provisioning failed.&lt;br /&gt;&lt;br&gt;&lt;br&gt;_Note:_ The order of the statuses above does not indicate any order of status transitions. Conditional field, not present for CoF tokens. |  [optional] |
|**provisioningStatusDescription** | **String** | Description of the provisioning status. Conditional field, not present for CoF tokens. |  [optional] |
|**storageTechnology** | **String** | The architecture or technology used for token storage. Valid values:&lt;br /&gt;    \&quot;D\&quot; - Device memory&lt;br /&gt;    \&quot;P\&quot; - Device memory protected by Trusted Platform Module (TPM)&lt;br /&gt;    \&quot;H\&quot; - Server&lt;br /&gt;    \&quot;E\&quot; - Trusted Execution Environment (TEE)&lt;br /&gt;    \&quot;S\&quot; - Secure Element (SE)&lt;br /&gt;    \&quot;V\&quot; - Virtual Execution Environment (VEE). |  [optional] |
|**suspenders** | [**Suspenders**](Suspenders.md) |  |  [optional] |
|**tokenActivatedDateTime** | **String** | Date and time that the token was activated. Conditional field, present only once the Token has been activated. string in ISO 8601 format ? YYYY-MM-DDThh:mm:ssTZD . |  [optional] |
|**tokenAssuranceLevel** | **String** | Indicates the level of Identification and Verification performed to validate the Cardholder and the Cardholder&#39;s account at the time the Token was issued (or at any subsquent time post-issuance).  Only present when a token has a Token Assurance Level assigned.  Supported values are 0 (Not Authenticated) and non-zero (Authenticated). |  [optional] |
|**tokenDeletedFromConsumerApp** | **String** | Indicates whether or not a token has been deleted from the consumer app by the token requestor.&lt;br&gt;&lt;br&gt;_Note:_ This is a \&quot;soft delete\&quot; that does not affect the actual Token Status. The token may still be active in the system. Supported values - true, false. |  [optional] |
|**tokenRequestorConsumerFacingEntityName** | **String** | The Token Service Provider name to be displayed to the consumer (consumer-facing name). |  [optional] |
|**tokenRequestorId** | **String** | Per EMV Co, the entity uniquely recognized by Mastercard as the Token Service Provider. |  [optional] |
|**tokenRequestorName** | **String** | The legal name of the token requestor. There can be more than one Token Requestor Id per Token Requester Name (legal name). So it is important to use both parameters to uniquely identify a token requestor. |  [optional] |
|**tokenSuffix** | **String** | Last 4 digits of token in a 4 character string. Conditional field, present once the token has been designated for the digitization. |  [optional] |
|**tokenType** | **String** | Type of token. Valid values:&lt;br /&gt;    \&quot;S\&quot; - Embedded Secure Element Token&lt;br /&gt;    \&quot;C\&quot; - Mastercard Cloud-Based Payments token.&lt;br /&gt;   F &#x3D; Static token (deprecated) |  [optional] |
|**tokenUniqueReference** | **String** | Unique reference to the token. Conditional field, present when successfully assigned. |  [optional] |
|**walletId** | **String** | Identifier of the Wallet Provider who requested the digitization or tokenization. Conditional field, not present for CoF tokens, and only present when supplied by the Payment App Provider. |  [optional] |



