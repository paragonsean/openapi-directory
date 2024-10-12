# NetworkManagementApi.LoadBalancerBackend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Name of a Compute Engine instance or network endpoint. | [optional] 
**healthCheckAllowingFirewallRules** | **[String]** | A list of firewall rule URIs allowing probes from health check IP ranges. | [optional] 
**healthCheckBlockingFirewallRules** | **[String]** | A list of firewall rule URIs blocking probes from health check IP ranges. | [optional] 
**healthCheckFirewallState** | **String** | State of the health check firewall configuration. | [optional] 
**uri** | **String** | URI of a Compute Engine instance or network endpoint. | [optional] 



## Enum: HealthCheckFirewallStateEnum


* `HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED` (value: `"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED"`)

* `CONFIGURED` (value: `"CONFIGURED"`)

* `MISCONFIGURED` (value: `"MISCONFIGURED"`)




