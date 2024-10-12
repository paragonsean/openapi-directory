# LinodeApi.GetLKEClusterNode200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The Node&#39;s ID.  | [optional] [readonly] 
**instanceId** | **Number** | The Linode&#39;s ID. If no Linode is currently provisioned for this Node, this is &#x60;null&#x60;.  | [optional] 
**status** | **String** | The creation status of this Node. This status is distinct from this Node&#39;s readiness as a Kubernetes Node Object as determined by the command &#x60;kubectl get nodes&#x60;.  &#x60;not_ready&#x60; indicates that the Linode is still being created.  &#x60;ready&#x60; indicates that the Linode has successfully been created and is running Kubernetes software.  | [optional] 



## Enum: StatusEnum


* `ready` (value: `"ready"`)

* `not_ready` (value: `"not_ready"`)




