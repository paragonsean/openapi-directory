

# NetworkServiceConfig

Polymorphic Network Service Config

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asns** | **List&lt;Long&gt;** |  |  |
|**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. |  |
|**capacity** | **Integer** | The capacity of the service in Mbps. If set to Null, the maximum capacity will be used, i.e. the virtual circuit is not rate-limited.  An exchange may choose to constrain the available capacity range of a &#x60;ProductOffering&#x60;.  That means, the service can consume up to the total bandwidth of the &#x60;Connection&#x60;.  Typically the service is charged based on the capacity. |  [optional] |
|**chargedUntil** | **LocalDate** | Your obligation to pay for the service will end on this date. Typically &#x60;≥ decommission_at&#x60;.  This field is only used when the state is &#x60;DECOMMISSION_REQUESTED&#x60; or &#x60;DECOMMISSIONED&#x60;. |  [optional] |
|**connection** | **String** | The id of the connection to use for this &#x60;NetworkServiceConfig&#x60;. |  |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  |
|**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  |  [optional] |
|**decommissionAt** | **LocalDate** | The service will be decommissioned on this date.  This field is only used when the state is &#x60;DECOMMISSION_REQUESTED&#x60; or &#x60;DECOMMISSIONED&#x60;. |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**id** | **String** |  |  |
|**ips** | **List&lt;String&gt;** | A list of ip-address IDs.  Allocation of IP Addresses might be deferred depending on the IXP implementation. No assumption should be made. |  [optional] [readonly] |
|**listed** | **Boolean** | The customer wants to be featured on the member list |  |
|**macs** | **List&lt;String&gt;** |  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  |
|**networkFeatureConfigs** | **List&lt;String&gt;** | A list of ids of &#x60;NetworkFeatureConfig&#x60;s.  |  [optional] [readonly] |
|**networkService** | **String** | The id of the configured network service. |  |
|**productOffering** | **String** | The product offering must match the type &#x60;exchange_lan&#x60; and must refer to the related network service through the &#x60;exchange_lan_network_service&#x60; property. |  |
|**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  |  [optional] |
|**roleAssignments** | **List&lt;String&gt;** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**status** | [**List&lt;Status&gt;**](Status.md) |  |  [optional] |
|**type** | **String** |  |  |
|**vlanConfig** | [**VlanConfig**](VlanConfig.md) |  |  |
|**role** | [**RoleEnum**](#RoleEnum) | A &#x60;leaf&#x60; can only reach roots and is isolated from other leafs. A &#x60;root&#x60; can reach any other point in the virtual circuit including other roots. |  [optional] |
|**cloudVlan** | **Integer** | If the &#x60;provider_vlans&#x60; property of the &#x60;ProductOffering&#x60; is &#x60;multi&#x60;, a numeric value refers to a specific vlan on the service provider side.  Otherwise, if set to &#x60;null&#x60;, it refers to all unmatched vlan ids on the service provider side. (All vlan ids from the service provider side are presented as tags within any vlans specified in &#x60;vlan_config&#x60;.)  If the &#x60;provider_vlans&#x60; property of the &#x60;ProductOffering&#x60; is &#x60;single&#x60;, the &#x60;cloud_vlan&#x60; MUST be &#x60;null&#x60; or MUST NOT be provided. |  |
|**handover** | **Integer** | The handover enumerates the connection and is required for checking diversity constraints.  It must be within &#x60;1 &lt;&#x3D; x &lt;&#x3D; network_service.diversity&#x60;.  |  |



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



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ROOT | &quot;root&quot; |
| LEAF | &quot;leaf&quot; |



