

# VmwareNodeConfig

Parameters that describe the configuration of all nodes within a given node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiskSizeGb** | **String** | VMware disk size to be used during creation. |  [optional] |
|**cpus** | **String** | The number of CPUs for each node in the node pool. |  [optional] |
|**enableLoadBalancer** | **Boolean** | Allow node pool traffic to be load balanced. Only works for clusters with MetalLB load balancers. |  [optional] |
|**image** | **String** | The OS image name in vCenter, only valid when using Windows. |  [optional] |
|**imageType** | **String** | Required. The OS image to be used for each node in a node pool. Currently &#x60;cos&#x60;, &#x60;ubuntu&#x60;, &#x60;ubuntu_containerd&#x60; and &#x60;windows&#x60; are supported. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version -- it&#39;s best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ |  [optional] |
|**memoryMb** | **String** | The megabytes of memory for each node in the node pool. |  [optional] |
|**replicas** | **String** | The number of nodes in the node pool. |  [optional] |
|**taints** | [**List&lt;NodeTaint&gt;**](NodeTaint.md) | The initial taints assigned to nodes of this node pool. |  [optional] |
|**vsphereConfig** | [**VmwareVsphereConfig**](VmwareVsphereConfig.md) |  |  [optional] |



