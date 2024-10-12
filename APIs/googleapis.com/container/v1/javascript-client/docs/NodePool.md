# KubernetesEngineApi.NodePool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaling** | [**NodePoolAutoscaling**](NodePoolAutoscaling.md) |  | [optional] 
**bestEffortProvisioning** | [**BestEffortProvisioning**](BestEffortProvisioning.md) |  | [optional] 
**conditions** | [**[StatusCondition]**](StatusCondition.md) | Which conditions caused the current node pool state. | [optional] 
**config** | [**NodeConfig**](NodeConfig.md) |  | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of node pool fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**initialNodeCount** | **Number** | The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. | [optional] 
**instanceGroupUrls** | **[String]** | [Output only] The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources. | [optional] 
**locations** | **[String]** | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool&#39;s nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed. | [optional] 
**management** | [**NodeManagement**](NodeManagement.md) |  | [optional] 
**maxPodsConstraint** | [**MaxPodsConstraint**](MaxPodsConstraint.md) |  | [optional] 
**name** | **String** | The name of the node pool. | [optional] 
**networkConfig** | [**NodeNetworkConfig**](NodeNetworkConfig.md) |  | [optional] 
**placementPolicy** | [**PlacementPolicy**](PlacementPolicy.md) |  | [optional] 
**podIpv4CidrSize** | **Number** | [Output only] The pod CIDR block size per node in this node pool. | [optional] 
**queuedProvisioning** | [**QueuedProvisioning**](QueuedProvisioning.md) |  | [optional] 
**selfLink** | **String** | [Output only] Server-defined URL for the resource. | [optional] 
**status** | **String** | [Output only] The status of the nodes in this pool instance. | [optional] 
**statusMessage** | **String** | [Output only] Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available. | [optional] 
**updateInfo** | [**UpdateInfo**](UpdateInfo.md) |  | [optional] 
**upgradeSettings** | [**UpgradeSettings**](UpgradeSettings.md) |  | [optional] 
**version** | **String** | The version of Kubernetes running on this NodePool&#39;s nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version). | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `PROVISIONING` (value: `"PROVISIONING"`)

* `RUNNING` (value: `"RUNNING"`)

* `RUNNING_WITH_ERROR` (value: `"RUNNING_WITH_ERROR"`)

* `RECONCILING` (value: `"RECONCILING"`)

* `STOPPING` (value: `"STOPPING"`)

* `ERROR` (value: `"ERROR"`)




