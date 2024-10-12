# NetworkManagementApi.LoadBalancerInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendType** | **String** | Type of load balancer&#39;s backend configuration. | [optional] 
**backendUri** | **String** | Backend configuration URI. | [optional] 
**backends** | [**[LoadBalancerBackend]**](LoadBalancerBackend.md) | Information for the loadbalancer backends. | [optional] 
**healthCheckUri** | **String** | URI of the health check for the load balancer. Deprecated and no longer populated as different load balancer backends might have different health checks. | [optional] 
**loadBalancerType** | **String** | Type of the load balancer. | [optional] 



## Enum: BackendTypeEnum


* `BACKEND_TYPE_UNSPECIFIED` (value: `"BACKEND_TYPE_UNSPECIFIED"`)

* `BACKEND_SERVICE` (value: `"BACKEND_SERVICE"`)

* `TARGET_POOL` (value: `"TARGET_POOL"`)

* `TARGET_INSTANCE` (value: `"TARGET_INSTANCE"`)





## Enum: LoadBalancerTypeEnum


* `LOAD_BALANCER_TYPE_UNSPECIFIED` (value: `"LOAD_BALANCER_TYPE_UNSPECIFIED"`)

* `INTERNAL_TCP_UDP` (value: `"INTERNAL_TCP_UDP"`)

* `NETWORK_TCP_UDP` (value: `"NETWORK_TCP_UDP"`)

* `HTTP_PROXY` (value: `"HTTP_PROXY"`)

* `TCP_PROXY` (value: `"TCP_PROXY"`)

* `SSL_PROXY` (value: `"SSL_PROXY"`)




