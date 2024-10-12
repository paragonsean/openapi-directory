

# LKENodeStatus

Status information for a Node which is a member of a Kubernetes cluster. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Node&#39;s ID.  |  [optional] |
|**instanceId** | **String** | The Linode&#39;s ID. When no Linode is currently provisioned for this Node, this will be null.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The Node&#39;s status as it pertains to being a Kubernetes node.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| NOT_READY | &quot;not_ready&quot; |



