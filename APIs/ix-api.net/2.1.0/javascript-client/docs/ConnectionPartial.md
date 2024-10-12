# IxApi.ConnectionPartial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. | [optional] 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | [optional] 
**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  | [optional] 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**id** | **String** |  | [optional] 
**lacpTimeout** | **String** | This sets the LACP Timeout mode. Both ends of the connections need to be configured the same.  | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | [optional] 
**mode** | **String** | Sets the mode of the connection. The mode can be:  - &#x60;lag_lacp&#x60;: connection is build as a LAG with LACP enabled - &#x60;lag_static&#x60;: connection is build as LAG with static configuration - &#x60;flex_ethernet&#x60;: connect is build as a FlexEthernet channel - &#x60;standalone&#x60;: only one port is allowed in this connection without any bundling.  | [optional] 
**name** | **String** |  | [optional] 
**outerVlanEthertypes** | **[String]** | The ethertype of the outer tag in hexadecimal notation.  | [optional] 
**ports** | **[String]** | References to the port belonging to this connection. Typically all ports within one connection are distributed over the same device.  | [optional] 
**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  | [optional] [default to &#39;&#39;]
**roleAssignments** | **[String]** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  | [optional] 
**speed** | **Number** | Shows the total bandwidth of the connection in Mbit/s.  | [optional] 
**state** | **String** |  | [optional] 
**status** | [**[Status]**](Status.md) |  | [optional] 
**vlanTypes** | **[String]** | A list of vlan config types you can configure using this connection. | [optional] 



## Enum: LacpTimeoutEnum


* `slow` (value: `"slow"`)

* `fast` (value: `"fast"`)





## Enum: ModeEnum


* `lag_lacp` (value: `"lag_lacp"`)

* `lag_static` (value: `"lag_static"`)

* `flex_ethernet` (value: `"flex_ethernet"`)

* `standalone` (value: `"standalone"`)





## Enum: [OuterVlanEthertypesEnum]


* `0x8100` (value: `"0x8100"`)

* `0x88a8` (value: `"0x88a8"`)

* `0x9100` (value: `"0x9100"`)





## Enum: StateEnum


* `requested` (value: `"requested"`)

* `allocated` (value: `"allocated"`)

* `testing` (value: `"testing"`)

* `production` (value: `"production"`)

* `production_change_pending` (value: `"production_change_pending"`)

* `decommission_requested` (value: `"decommission_requested"`)

* `decommissioned` (value: `"decommissioned"`)

* `archived` (value: `"archived"`)

* `error` (value: `"error"`)

* `operator` (value: `"operator"`)

* `scheduled` (value: `"scheduled"`)





## Enum: [VlanTypesEnum]


* `port` (value: `"port"`)

* `dot1q` (value: `"dot1q"`)

* `qinq` (value: `"qinq"`)




