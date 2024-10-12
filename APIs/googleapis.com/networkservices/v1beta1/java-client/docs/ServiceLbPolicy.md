

# ServiceLbPolicy

ServiceLbPolicy holds global load balancing and traffic distribution configuration that can be applied to a BackendService.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCapacityDrain** | [**ServiceLbPolicyAutoCapacityDrain**](ServiceLbPolicyAutoCapacityDrain.md) |  |  [optional] |
|**createTime** | **String** | Output only. The timestamp when this resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**failoverConfig** | [**ServiceLbPolicyFailoverConfig**](ServiceLbPolicyFailoverConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the ServiceLbPolicy resource. |  [optional] |
|**loadBalancingAlgorithm** | [**LoadBalancingAlgorithmEnum**](#LoadBalancingAlgorithmEnum) | Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION. |  [optional] |
|**name** | **String** | Required. Name of the ServiceLbPolicy resource. It matches pattern &#x60;projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}&#x60;. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when this resource was last updated. |  [optional] [readonly] |



## Enum: LoadBalancingAlgorithmEnum

| Name | Value |
|---- | -----|
| LOAD_BALANCING_ALGORITHM_UNSPECIFIED | &quot;LOAD_BALANCING_ALGORITHM_UNSPECIFIED&quot; |
| SPRAY_TO_WORLD | &quot;SPRAY_TO_WORLD&quot; |
| SPRAY_TO_REGION | &quot;SPRAY_TO_REGION&quot; |
| WATERFALL_BY_REGION | &quot;WATERFALL_BY_REGION&quot; |
| WATERFALL_BY_ZONE | &quot;WATERFALL_BY_ZONE&quot; |



