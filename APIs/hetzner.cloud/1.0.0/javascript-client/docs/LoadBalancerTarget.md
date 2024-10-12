# HetznerCloudApi.LoadBalancerTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthStatus** | [**[LoadBalancerTargetHealthStatusInner]**](LoadBalancerTargetHealthStatusInner.md) | List of health statuses of the services on this target. Only present for target types \&quot;server\&quot; and \&quot;ip\&quot;. | [optional] 
**ip** | [**LoadBalancerTargetIP**](LoadBalancerTargetIP.md) |  | [optional] 
**labelSelector** | [**LoadBalancerTargetLabelSelector**](LoadBalancerTargetLabelSelector.md) |  | [optional] 
**server** | [**LoadBalancerTargetServer**](LoadBalancerTargetServer.md) |  | [optional] 
**targets** | [**[LoadBalancerTargetTarget]**](LoadBalancerTargetTarget.md) | List of resolved label selector target Servers. Only present for type \&quot;label_selector\&quot;. | [optional] 
**type** | **String** | Type of the resource | 
**usePrivateIp** | **Boolean** | Use the private network IP instead of the public IP. Default value is false. Only present for target types \&quot;server\&quot; and \&quot;label_selector\&quot;. | [optional] 



## Enum: TypeEnum


* `server` (value: `"server"`)

* `label_selector` (value: `"label_selector"`)

* `ip` (value: `"ip"`)




