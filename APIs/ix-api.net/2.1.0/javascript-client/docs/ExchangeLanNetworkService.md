# IxApi.ExchangeLanNetworkService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**id** | **String** |  | 
**ixfdbIxid** | **Number** | id of ixfdb | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | 
**metroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60; where the exchange lan network service is directly provided.  Same as &#x60;service_metro_area_network&#x60; on the related &#x60;ProductOffering&#x60;.  | 
**name** | **String** | Exchange-dependent service name, will be shown on the invoice. | 
**networkFeatures** | **[String]** |  | 
**nscRequiredContactRoles** | **[String]** | The configuration will require at least one of each of the specified roles assigned to contacts.  The &#x60;RoleAssignment&#x60; is associated through the &#x60;role_assignments&#x60; list property of the network service configuration. | [optional] [readonly] 
**peeringdbIxid** | **Number** | PeeringDB ixid | [optional] 
**productOffering** | **String** | *deprecation notice* | [optional] 
**state** | **String** |  | 
**status** | [**[Status]**](Status.md) |  | [optional] 
**subnetV4** | **String** | IPv4 subnet in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) CIDR notation.  | 
**subnetV6** | **String** | IPv6 subnet in hexadecimal colon separated CIDR notation.  | 
**type** | **String** |  | 



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




