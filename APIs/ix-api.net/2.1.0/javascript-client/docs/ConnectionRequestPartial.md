# IxApi.ConnectionRequestPartial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. | [optional] 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | [optional] 
**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  | [optional] 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**lacpTimeout** | **String** | This sets the LACP Timeout mode. Both ends of the connections need to be configured the same.  | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | [optional] 
**mode** | **String** | Sets the mode of the connection. The mode can be:  - &#x60;lag_lacp&#x60;: connection is build as a LAG with LACP enabled - &#x60;lag_static&#x60;: connection is build as LAG with static configuration - &#x60;flex_ethernet&#x60;: connect is build as a FlexEthernet channel - &#x60;standalone&#x60;: only one port is allowed in this connection without any bundling.  | [optional] 
**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  | [optional] [default to &#39;&#39;]
**roleAssignments** | **[String]** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  | [optional] 
**speed** | **Number** | Shows the total bandwidth of the connection in Mbit/s.  | [optional] 



## Enum: LacpTimeoutEnum


* `slow` (value: `"slow"`)

* `fast` (value: `"fast"`)





## Enum: ModeEnum


* `lag_lacp` (value: `"lag_lacp"`)

* `lag_static` (value: `"lag_static"`)

* `flex_ethernet` (value: `"flex_ethernet"`)

* `standalone` (value: `"standalone"`)




