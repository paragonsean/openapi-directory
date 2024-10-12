

# RRSetRoutingPolicyLoadBalancerTarget

The configuration for an individual load balancer to health check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | The frontend IP address of the load balancer to health check. |  [optional] |
|**ipProtocol** | [**IpProtocolEnum**](#IpProtocolEnum) | The protocol of the load balancer to health check. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**loadBalancerType** | [**LoadBalancerTypeEnum**](#LoadBalancerTypeEnum) | The type of load balancer specified by this target. This value must match the configuration of the load balancer located at the LoadBalancerTarget&#39;s IP address, port, and region. Use the following: - *regionalL4ilb*: for a regional internal passthrough Network Load Balancer. - *regionalL7ilb*: for a regional internal Application Load Balancer. - *globalL7ilb*: for a global internal Application Load Balancer.  |  [optional] |
|**networkUrl** | **String** | The fully qualified URL of the network that the load balancer is attached to. This should be formatted like https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network} . |  [optional] |
|**port** | **String** | The configured port of the load balancer. |  [optional] |
|**project** | **String** | The project ID in which the load balancer is located. |  [optional] |
|**region** | **String** | The region in which the load balancer is located. |  [optional] |



## Enum: IpProtocolEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;undefined&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



## Enum: LoadBalancerTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| GLOBAL_L7ILB | &quot;globalL7ilb&quot; |
| REGIONAL_L4ILB | &quot;regionalL4ilb&quot; |
| REGIONAL_L7ILB | &quot;regionalL7ilb&quot; |



