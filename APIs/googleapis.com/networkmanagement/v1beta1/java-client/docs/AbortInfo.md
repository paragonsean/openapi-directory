

# AbortInfo

Details of the final state \"abort\" and associated resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cause** | [**CauseEnum**](#CauseEnum) | Causes that the analysis is aborted. |  [optional] |
|**ipAddress** | **String** | IP address that caused the abort. |  [optional] |
|**projectsMissingPermission** | **List&lt;String&gt;** | List of project IDs the user specified in the request but lacks access to. In this case, analysis is aborted with the PERMISSION_DENIED cause. |  [optional] |
|**resourceUri** | **String** | URI of the resource that caused the abort. |  [optional] |



## Enum: CauseEnum

| Name | Value |
|---- | -----|
| CAUSE_UNSPECIFIED | &quot;CAUSE_UNSPECIFIED&quot; |
| UNKNOWN_NETWORK | &quot;UNKNOWN_NETWORK&quot; |
| UNKNOWN_PROJECT | &quot;UNKNOWN_PROJECT&quot; |
| NO_EXTERNAL_IP | &quot;NO_EXTERNAL_IP&quot; |
| UNINTENDED_DESTINATION | &quot;UNINTENDED_DESTINATION&quot; |
| SOURCE_ENDPOINT_NOT_FOUND | &quot;SOURCE_ENDPOINT_NOT_FOUND&quot; |
| MISMATCHED_SOURCE_NETWORK | &quot;MISMATCHED_SOURCE_NETWORK&quot; |
| DESTINATION_ENDPOINT_NOT_FOUND | &quot;DESTINATION_ENDPOINT_NOT_FOUND&quot; |
| MISMATCHED_DESTINATION_NETWORK | &quot;MISMATCHED_DESTINATION_NETWORK&quot; |
| UNKNOWN_IP | &quot;UNKNOWN_IP&quot; |
| SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK | &quot;SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS | &quot;PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS&quot; |
| PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS | &quot;PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS&quot; |
| NO_SOURCE_LOCATION | &quot;NO_SOURCE_LOCATION&quot; |
| INVALID_ARGUMENT | &quot;INVALID_ARGUMENT&quot; |
| TRACE_TOO_LONG | &quot;TRACE_TOO_LONG&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| UNSUPPORTED | &quot;UNSUPPORTED&quot; |
| MISMATCHED_IP_VERSION | &quot;MISMATCHED_IP_VERSION&quot; |
| GKE_KONNECTIVITY_PROXY_UNSUPPORTED | &quot;GKE_KONNECTIVITY_PROXY_UNSUPPORTED&quot; |
| RESOURCE_CONFIG_NOT_FOUND | &quot;RESOURCE_CONFIG_NOT_FOUND&quot; |
| VM_INSTANCE_CONFIG_NOT_FOUND | &quot;VM_INSTANCE_CONFIG_NOT_FOUND&quot; |
| NETWORK_CONFIG_NOT_FOUND | &quot;NETWORK_CONFIG_NOT_FOUND&quot; |
| FIREWALL_CONFIG_NOT_FOUND | &quot;FIREWALL_CONFIG_NOT_FOUND&quot; |
| ROUTE_CONFIG_NOT_FOUND | &quot;ROUTE_CONFIG_NOT_FOUND&quot; |
| GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT | &quot;GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT&quot; |
| SOURCE_PSC_CLOUD_SQL_UNSUPPORTED | &quot;SOURCE_PSC_CLOUD_SQL_UNSUPPORTED&quot; |
| SOURCE_FORWARDING_RULE_UNSUPPORTED | &quot;SOURCE_FORWARDING_RULE_UNSUPPORTED&quot; |
| NON_ROUTABLE_IP_ADDRESS | &quot;NON_ROUTABLE_IP_ADDRESS&quot; |



