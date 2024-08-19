

# NetworkService

Polymorphic Network Services

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**id** | **String** |  |  |
|**ixfdbIxid** | **Integer** | id of ixfdb |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  |
|**metroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60; where the exchange lan network service is directly provided.  Same as &#x60;service_metro_area_network&#x60; on the related &#x60;ProductOffering&#x60;.  |  |
|**name** | **String** | Name of the multi-point to multi-point virtual circuit. |  |
|**networkFeatures** | **List&lt;String&gt;** |  |  |
|**nscRequiredContactRoles** | **List&lt;String&gt;** | The configuration will require at least one of each of the specified roles assigned to contacts.  The &#x60;RoleAssignment&#x60; is associated through the &#x60;role_assignments&#x60; list property of the network service configuration. |  [optional] [readonly] |
|**peeringdbIxid** | **Integer** | PeeringDB ixid |  [optional] |
|**productOffering** | **String** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**status** | [**List&lt;Status&gt;**](Status.md) |  |  [optional] |
|**subnetV4** | **String** | IPv4 subnet in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) CIDR notation.  |  |
|**subnetV6** | **String** | IPv6 subnet in hexadecimal colon separated CIDR notation.  |  |
|**type** | **String** |  |  |
|**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. |  |
|**capacity** | **Integer** | The capacity of the service in Mbps. When null, the maximum capacity will be used. |  [optional] |
|**chargedUntil** | **LocalDate** | Your obligation to pay for the service will end on this date. Typically &#x60;≥ decommission_at&#x60;.  This field is only used when the state is &#x60;DECOMMISSION_REQUESTED&#x60; or &#x60;DECOMMISSIONED&#x60;. |  [optional] |
|**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  |  [optional] |
|**decommissionAt** | **LocalDate** | The service will be decommissioned on this date.  This field is only used when the state is &#x60;DECOMMISSION_REQUESTED&#x60; or &#x60;DECOMMISSIONED&#x60;. |  [optional] |
|**joiningMemberAccount** | **String** | The account of the B-side member joining the virtual circuit.  |  |
|**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  |  [optional] |
|**memberJoiningRules** | **List&lt;String&gt;** |  |  |
|**_public** | **Boolean** | A public mp2mp network service can be joined by everyone on the exchange unless denied by a member-joining-rule.  Public network services are visible to other members of the IXP, however only &#x60;name&#x60;, &#x60;type&#x60;, &#x60;product_offering&#x60;, &#x60;consuming_account&#x60; and &#x60;managing_account&#x60; are made available.  Other required fields are redacted. |  [optional] |
|**cloudKey** | **String** |  |  |
|**diversity** | **Integer** | Same value as the corresponding &#x60;ProductOffering&#x60;.  The service can be delivered over multiple handovers from the exchange to the &#x60;service_provider&#x60;.  The &#x60;diversity&#x60; denotes the number of handovers between the exchange and the service provider. A value of two signals a redundant service.  Only one network service configuration for each &#x60;handover&#x60; and &#x60;cloud_vlan&#x60; can be created. |  |
|**providerRef** | **String** | For a cloud network service with the exchange first workflow, the &#x60;provider_ref&#x60; will be a reference to a resource of the cloud provider. (E.g. the UUID of a virtual circuit.)  The &#x60;provider_ref&#x60; is managed by the exchange and its meaning may vary between different cloud services.  |  |



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



