# ServiceNetworkingApi.ValidateConsumerConfigResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existingSubnetworkCandidates** | [**[Subnetwork]**](Subnetwork.md) | List of subnetwork candidates from the request which exist with the &#x60;ip_cidr_range&#x60;, &#x60;secondary_ip_cider_ranges&#x60;, and &#x60;outside_allocation&#x60; fields set. | [optional] 
**isValid** | **Boolean** | Indicates whether all the requested validations passed. | [optional] 
**validationError** | **String** | The first validation which failed. | [optional] 



## Enum: ValidationErrorEnum


* `VALIDATION_ERROR_UNSPECIFIED` (value: `"VALIDATION_ERROR_UNSPECIFIED"`)

* `VALIDATION_NOT_REQUESTED` (value: `"VALIDATION_NOT_REQUESTED"`)

* `SERVICE_NETWORKING_NOT_ENABLED` (value: `"SERVICE_NETWORKING_NOT_ENABLED"`)

* `NETWORK_NOT_FOUND` (value: `"NETWORK_NOT_FOUND"`)

* `NETWORK_NOT_PEERED` (value: `"NETWORK_NOT_PEERED"`)

* `NETWORK_PEERING_DELETED` (value: `"NETWORK_PEERING_DELETED"`)

* `NETWORK_NOT_IN_CONSUMERS_PROJECT` (value: `"NETWORK_NOT_IN_CONSUMERS_PROJECT"`)

* `NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT` (value: `"NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT"`)

* `HOST_PROJECT_NOT_FOUND` (value: `"HOST_PROJECT_NOT_FOUND"`)

* `CONSUMER_PROJECT_NOT_SERVICE_PROJECT` (value: `"CONSUMER_PROJECT_NOT_SERVICE_PROJECT"`)

* `RANGES_EXHAUSTED` (value: `"RANGES_EXHAUSTED"`)

* `RANGES_NOT_RESERVED` (value: `"RANGES_NOT_RESERVED"`)

* `RANGES_DELETED_LATER` (value: `"RANGES_DELETED_LATER"`)

* `COMPUTE_API_NOT_ENABLED` (value: `"COMPUTE_API_NOT_ENABLED"`)

* `USE_PERMISSION_NOT_FOUND` (value: `"USE_PERMISSION_NOT_FOUND"`)




