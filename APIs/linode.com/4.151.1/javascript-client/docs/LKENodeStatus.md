# LinodeApi.LKENodeStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The Node&#39;s ID.  | [optional] 
**instanceId** | **String** | The Linode&#39;s ID. When no Linode is currently provisioned for this Node, this will be null.  | [optional] 
**status** | **String** | The Node&#39;s status as it pertains to being a Kubernetes node.  | [optional] 



## Enum: StatusEnum


* `ready` (value: `"ready"`)

* `not_ready` (value: `"not_ready"`)




