

# Connection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. |  |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  |
|**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**id** | **String** |  |  |
|**lacpTimeout** | [**LacpTimeoutEnum**](#LacpTimeoutEnum) | This sets the LACP Timeout mode. Both ends of the connections need to be configured the same.  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  |
|**mode** | [**ModeEnum**](#ModeEnum) | Sets the mode of the connection. The mode can be:  - &#x60;lag_lacp&#x60;: connection is build as a LAG with LACP enabled - &#x60;lag_static&#x60;: connection is build as LAG with static configuration - &#x60;flex_ethernet&#x60;: connect is build as a FlexEthernet channel - &#x60;standalone&#x60;: only one port is allowed in this connection without any bundling.  |  |
|**name** | **String** |  |  |
|**outerVlanEthertypes** | [**List&lt;OuterVlanEthertypesEnum&gt;**](#List&lt;OuterVlanEthertypesEnum&gt;) | The ethertype of the outer tag in hexadecimal notation.  |  |
|**ports** | **List&lt;String&gt;** | References to the port belonging to this connection. Typically all ports within one connection are distributed over the same device.  |  [optional] |
|**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  |  [optional] |
|**roleAssignments** | **List&lt;String&gt;** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  |  |
|**speed** | **Integer** | Shows the total bandwidth of the connection in Mbit/s.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**status** | [**List&lt;Status&gt;**](Status.md) |  |  [optional] |
|**vlanTypes** | [**List&lt;VlanTypesEnum&gt;**](#List&lt;VlanTypesEnum&gt;) | A list of vlan config types you can configure using this connection. |  |



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



## Enum: List&lt;OuterVlanEthertypesEnum&gt;

| Name | Value |
|---- | -----|
| _0X8100 | &quot;0x8100&quot; |
| _0X88A8 | &quot;0x88a8&quot; |
| _0X9100 | &quot;0x9100&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| ALLOCATED | &quot;allocated&quot; |
| TESTING | &quot;testing&quot; |
| PRODUCTION | &quot;production&quot; |
| PRODUCTION_CHANGE_PENDING | &quot;production_change_pending&quot; |
| DECOMMISSION_REQUESTED | &quot;decommission_requested&quot; |
| DECOMMISSIONED | &quot;decommissioned&quot; |
| ARCHIVED | &quot;archived&quot; |
| ERROR | &quot;error&quot; |
| OPERATOR | &quot;operator&quot; |
| SCHEDULED | &quot;scheduled&quot; |



## Enum: List&lt;VlanTypesEnum&gt;

| Name | Value |
|---- | -----|
| PORT | &quot;port&quot; |
| DOT1Q | &quot;dot1q&quot; |
| QINQ | &quot;qinq&quot; |



