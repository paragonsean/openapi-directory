

# LoadBalancerInfo

For display only. Metadata associated with a load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendType** | [**BackendTypeEnum**](#BackendTypeEnum) | Type of load balancer&#39;s backend configuration. |  [optional] |
|**backendUri** | **String** | Backend configuration URI. |  [optional] |
|**backends** | [**List&lt;LoadBalancerBackend&gt;**](LoadBalancerBackend.md) | Information for the loadbalancer backends. |  [optional] |
|**healthCheckUri** | **String** | URI of the health check for the load balancer. Deprecated and no longer populated as different load balancer backends might have different health checks. |  [optional] |
|**loadBalancerType** | [**LoadBalancerTypeEnum**](#LoadBalancerTypeEnum) | Type of the load balancer. |  [optional] |



## Enum: BackendTypeEnum

| Name | Value |
|---- | -----|
| BACKEND_TYPE_UNSPECIFIED | &quot;BACKEND_TYPE_UNSPECIFIED&quot; |
| BACKEND_SERVICE | &quot;BACKEND_SERVICE&quot; |
| TARGET_POOL | &quot;TARGET_POOL&quot; |
| TARGET_INSTANCE | &quot;TARGET_INSTANCE&quot; |



## Enum: LoadBalancerTypeEnum

| Name | Value |
|---- | -----|
| LOAD_BALANCER_TYPE_UNSPECIFIED | &quot;LOAD_BALANCER_TYPE_UNSPECIFIED&quot; |
| INTERNAL_TCP_UDP | &quot;INTERNAL_TCP_UDP&quot; |
| NETWORK_TCP_UDP | &quot;NETWORK_TCP_UDP&quot; |
| HTTP_PROXY | &quot;HTTP_PROXY&quot; |
| TCP_PROXY | &quot;TCP_PROXY&quot; |
| SSL_PROXY | &quot;SSL_PROXY&quot; |



