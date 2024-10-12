

# LoadBalancerBackend

For display only. Metadata associated with a specific load balancer backend.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Name of a Compute Engine instance or network endpoint. |  [optional] |
|**healthCheckAllowingFirewallRules** | **List&lt;String&gt;** | A list of firewall rule URIs allowing probes from health check IP ranges. |  [optional] |
|**healthCheckBlockingFirewallRules** | **List&lt;String&gt;** | A list of firewall rule URIs blocking probes from health check IP ranges. |  [optional] |
|**healthCheckFirewallState** | [**HealthCheckFirewallStateEnum**](#HealthCheckFirewallStateEnum) | State of the health check firewall configuration. |  [optional] |
|**uri** | **String** | URI of a Compute Engine instance or network endpoint. |  [optional] |



## Enum: HealthCheckFirewallStateEnum

| Name | Value |
|---- | -----|
| HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED | &quot;HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED&quot; |
| CONFIGURED | &quot;CONFIGURED&quot; |
| MISCONFIGURED | &quot;MISCONFIGURED&quot; |



