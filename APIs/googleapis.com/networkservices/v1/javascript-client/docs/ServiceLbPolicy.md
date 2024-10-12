# NetworkServicesApi.ServiceLbPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoCapacityDrain** | [**ServiceLbPolicyAutoCapacityDrain**](ServiceLbPolicyAutoCapacityDrain.md) |  | [optional] 
**createTime** | **String** | Output only. The timestamp when this resource was created. | [optional] [readonly] 
**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. | [optional] 
**failoverConfig** | [**ServiceLbPolicyFailoverConfig**](ServiceLbPolicyFailoverConfig.md) |  | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the ServiceLbPolicy resource. | [optional] 
**loadBalancingAlgorithm** | **String** | Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION. | [optional] 
**name** | **String** | Required. Name of the ServiceLbPolicy resource. It matches pattern &#x60;projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}&#x60;. | [optional] 
**updateTime** | **String** | Output only. The timestamp when this resource was last updated. | [optional] [readonly] 



## Enum: LoadBalancingAlgorithmEnum


* `LOAD_BALANCING_ALGORITHM_UNSPECIFIED` (value: `"LOAD_BALANCING_ALGORITHM_UNSPECIFIED"`)

* `SPRAY_TO_WORLD` (value: `"SPRAY_TO_WORLD"`)

* `SPRAY_TO_REGION` (value: `"SPRAY_TO_REGION"`)

* `WATERFALL_BY_REGION` (value: `"WATERFALL_BY_REGION"`)

* `WATERFALL_BY_ZONE` (value: `"WATERFALL_BY_ZONE"`)




