

# ConnectionRequestPartial

Connection Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. |  [optional] |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  [optional] |
|**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**lacpTimeout** | [**LacpTimeoutEnum**](#LacpTimeoutEnum) | This sets the LACP Timeout mode. Both ends of the connections need to be configured the same.  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Sets the mode of the connection. The mode can be:  - &#x60;lag_lacp&#x60;: connection is build as a LAG with LACP enabled - &#x60;lag_static&#x60;: connection is build as LAG with static configuration - &#x60;flex_ethernet&#x60;: connect is build as a FlexEthernet channel - &#x60;standalone&#x60;: only one port is allowed in this connection without any bundling.  |  [optional] |
|**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  |  [optional] |
|**roleAssignments** | **List&lt;String&gt;** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  |  [optional] |
|**speed** | **Integer** | Shows the total bandwidth of the connection in Mbit/s.  |  [optional] |



## Enum: LacpTimeoutEnum

| Name | Value |
|---- | -----|
| SLOW | &quot;slow&quot; |
| FAST | &quot;fast&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| LAG_LACP | &quot;lag_lacp&quot; |
| LAG_STATIC | &quot;lag_static&quot; |
| FLEX_ETHERNET | &quot;flex_ethernet&quot; |
| STANDALONE | &quot;standalone&quot; |



