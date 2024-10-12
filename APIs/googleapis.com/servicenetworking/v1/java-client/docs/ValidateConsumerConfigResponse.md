

# ValidateConsumerConfigResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**existingSubnetworkCandidates** | [**List&lt;Subnetwork&gt;**](Subnetwork.md) | List of subnetwork candidates from the request which exist with the &#x60;ip_cidr_range&#x60;, &#x60;secondary_ip_cider_ranges&#x60;, and &#x60;outside_allocation&#x60; fields set. |  [optional] |
|**isValid** | **Boolean** | Indicates whether all the requested validations passed. |  [optional] |
|**validationError** | [**ValidationErrorEnum**](#ValidationErrorEnum) | The first validation which failed. |  [optional] |



## Enum: ValidationErrorEnum

| Name | Value |
|---- | -----|
| VALIDATION_ERROR_UNSPECIFIED | &quot;VALIDATION_ERROR_UNSPECIFIED&quot; |
| VALIDATION_NOT_REQUESTED | &quot;VALIDATION_NOT_REQUESTED&quot; |
| SERVICE_NETWORKING_NOT_ENABLED | &quot;SERVICE_NETWORKING_NOT_ENABLED&quot; |
| NETWORK_NOT_FOUND | &quot;NETWORK_NOT_FOUND&quot; |
| NETWORK_NOT_PEERED | &quot;NETWORK_NOT_PEERED&quot; |
| NETWORK_PEERING_DELETED | &quot;NETWORK_PEERING_DELETED&quot; |
| NETWORK_NOT_IN_CONSUMERS_PROJECT | &quot;NETWORK_NOT_IN_CONSUMERS_PROJECT&quot; |
| NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT | &quot;NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT&quot; |
| HOST_PROJECT_NOT_FOUND | &quot;HOST_PROJECT_NOT_FOUND&quot; |
| CONSUMER_PROJECT_NOT_SERVICE_PROJECT | &quot;CONSUMER_PROJECT_NOT_SERVICE_PROJECT&quot; |
| RANGES_EXHAUSTED | &quot;RANGES_EXHAUSTED&quot; |
| RANGES_NOT_RESERVED | &quot;RANGES_NOT_RESERVED&quot; |
| RANGES_DELETED_LATER | &quot;RANGES_DELETED_LATER&quot; |
| COMPUTE_API_NOT_ENABLED | &quot;COMPUTE_API_NOT_ENABLED&quot; |
| USE_PERMISSION_NOT_FOUND | &quot;USE_PERMISSION_NOT_FOUND&quot; |



