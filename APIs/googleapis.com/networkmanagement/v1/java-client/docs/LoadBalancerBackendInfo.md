

# LoadBalancerBackendInfo

For display only. Metadata associated with the load balancer backend.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendBucketUri** | **String** | URI of the backend bucket this backend targets (if applicable). |  [optional] |
|**backendServiceUri** | **String** | URI of the backend service this backend belongs to (if applicable). |  [optional] |
|**healthCheckFirewallsConfigState** | [**HealthCheckFirewallsConfigStateEnum**](#HealthCheckFirewallsConfigStateEnum) | Output only. Health check firewalls configuration state for the backend. This is a result of the static firewall analysis (verifying that health check traffic from required IP ranges to the backend is allowed or not). The backend might still be unhealthy even if these firewalls are configured. Please refer to the documentation for more information: https://cloud.google.com/load-balancing/docs/firewall-rules |  [optional] [readonly] |
|**healthCheckUri** | **String** | URI of the health check attached to this backend (if applicable). |  [optional] |
|**instanceGroupUri** | **String** | URI of the instance group this backend belongs to (if applicable). |  [optional] |
|**instanceUri** | **String** | URI of the backend instance (if applicable). Populated for instance group backends, and zonal NEG backends. |  [optional] |
|**name** | **String** | Display name of the backend. For example, it might be an instance name for the instance group backends, or an IP address and port for zonal network endpoint group backends. |  [optional] |
|**networkEndpointGroupUri** | **String** | URI of the network endpoint group this backend belongs to (if applicable). |  [optional] |
|**pscGoogleApiTarget** | **String** | PSC Google API target this PSC NEG backend targets (if applicable). |  [optional] |
|**pscServiceAttachmentUri** | **String** | URI of the PSC service attachment this PSC NEG backend targets (if applicable). |  [optional] |



## Enum: HealthCheckFirewallsConfigStateEnum

| Name | Value |
|---- | -----|
| HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED | &quot;HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED&quot; |
| FIREWALLS_CONFIGURED | &quot;FIREWALLS_CONFIGURED&quot; |
| FIREWALLS_PARTIALLY_CONFIGURED | &quot;FIREWALLS_PARTIALLY_CONFIGURED&quot; |
| FIREWALLS_NOT_CONFIGURED | &quot;FIREWALLS_NOT_CONFIGURED&quot; |
| FIREWALLS_UNSUPPORTED | &quot;FIREWALLS_UNSUPPORTED&quot; |



