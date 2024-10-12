# CloudDnsApi.RRSetRoutingPolicyLoadBalancerTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipAddress** | **String** | The frontend IP address of the load balancer to health check. | [optional] 
**ipProtocol** | **String** | The protocol of the load balancer to health check. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#rRSetRoutingPolicyLoadBalancerTarget&#39;]
**loadBalancerType** | **String** | The type of load balancer specified by this target. This value must match the configuration of the load balancer located at the LoadBalancerTarget&#39;s IP address, port, and region. Use the following: - *regionalL4ilb*: for a regional internal passthrough Network Load Balancer. - *regionalL7ilb*: for a regional internal Application Load Balancer. - *globalL7ilb*: for a global internal Application Load Balancer.  | [optional] 
**networkUrl** | **String** | The fully qualified URL of the network that the load balancer is attached to. This should be formatted like https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network} . | [optional] 
**port** | **String** | The configured port of the load balancer. | [optional] 
**project** | **String** | The project ID in which the load balancer is located. | [optional] 
**region** | **String** | The region in which the load balancer is located. | [optional] 



## Enum: IpProtocolEnum


* `UNDEFINED` (value: `"UNDEFINED"`)

* `TCP` (value: `"TCP"`)

* `UDP` (value: `"UDP"`)





## Enum: LoadBalancerTypeEnum


* `NONE` (value: `"NONE"`)

* `GLOBAL_L7ILB` (value: `"GLOBAL_L7ILB"`)

* `REGIONAL_L4ILB` (value: `"REGIONAL_L4ILB"`)

* `REGIONAL_L7ILB` (value: `"REGIONAL_L7ILB"`)




