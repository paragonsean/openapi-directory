

# ExchangeLanNetworkService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**id** | **String** |  |  |
|**ixfdbIxid** | **Integer** | id of ixfdb |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  |
|**metroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60; where the exchange lan network service is directly provided.  Same as &#x60;service_metro_area_network&#x60; on the related &#x60;ProductOffering&#x60;.  |  |
|**name** | **String** | Exchange-dependent service name, will be shown on the invoice. |  |
|**networkFeatures** | **List&lt;String&gt;** |  |  |
|**nscRequiredContactRoles** | **List&lt;String&gt;** | The configuration will require at least one of each of the specified roles assigned to contacts.  The &#x60;RoleAssignment&#x60; is associated through the &#x60;role_assignments&#x60; list property of the network service configuration. |  [optional] [readonly] |
|**peeringdbIxid** | **Integer** | PeeringDB ixid |  [optional] |
|**productOffering** | **String** | *deprecation notice* |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**status** | [**List&lt;Status&gt;**](Status.md) |  |  [optional] |
|**subnetV4** | **String** | IPv4 subnet in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) CIDR notation.  |  |
|**subnetV6** | **String** | IPv6 subnet in hexadecimal colon separated CIDR notation.  |  |
|**type** | **String** |  |  |



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



