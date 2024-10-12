# KubernetesEngineApi.UsableSubnetworkSecondaryRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipCidrRange** | **String** | The range of IP addresses belonging to this subnetwork secondary range. | [optional] 
**rangeName** | **String** | The name associated with this subnetwork secondary range, used when adding an alias IP range to a VM instance. | [optional] 
**status** | **String** | This field is to determine the status of the secondary range programmably. | [optional] 



## Enum: StatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `UNUSED` (value: `"UNUSED"`)

* `IN_USE_SERVICE` (value: `"IN_USE_SERVICE"`)

* `IN_USE_SHAREABLE_POD` (value: `"IN_USE_SHAREABLE_POD"`)

* `IN_USE_MANAGED_POD` (value: `"IN_USE_MANAGED_POD"`)




