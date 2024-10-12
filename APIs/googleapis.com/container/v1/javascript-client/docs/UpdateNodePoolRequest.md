# KubernetesEngineApi.UpdateNodePoolRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterId** | **String** | Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**confidentialNodes** | [**ConfidentialNodes**](ConfidentialNodes.md) |  | [optional] 
**diskSizeGb** | **String** | Optional. The desired disk size for nodes in the node pool specified in GB. The smallest allowed disk size is 10GB. Initiates an upgrade operation that migrates the nodes in the node pool to the specified disk size. | [optional] 
**diskType** | **String** | Optional. The desired disk type (e.g. &#39;pd-standard&#39;, &#39;pd-ssd&#39; or &#39;pd-balanced&#39;) for nodes in the node pool. Initiates an upgrade operation that migrates the nodes in the node pool to the specified disk type. | [optional] 
**etag** | **String** | The current etag of the node pool. If an etag is provided and does not match the current etag of the node pool, update will be blocked and an ABORTED error will be returned. | [optional] 
**fastSocket** | [**FastSocket**](FastSocket.md) |  | [optional] 
**gcfsConfig** | [**GcfsConfig**](GcfsConfig.md) |  | [optional] 
**gvnic** | [**VirtualNIC**](VirtualNIC.md) |  | [optional] 
**imageType** | **String** | Required. The desired image type for the node pool. Please see https://cloud.google.com/kubernetes-engine/docs/concepts/node-images for available image types. | [optional] 
**kubeletConfig** | [**NodeKubeletConfig**](NodeKubeletConfig.md) |  | [optional] 
**labels** | [**NodeLabels**](NodeLabels.md) |  | [optional] 
**linuxNodeConfig** | [**LinuxNodeConfig**](LinuxNodeConfig.md) |  | [optional] 
**locations** | **[String]** | The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the node pool&#39;s nodes should be located. Changing the locations for a node pool will result in nodes being either created or removed from the node pool, depending on whether locations are being added or removed. | [optional] 
**loggingConfig** | [**NodePoolLoggingConfig**](NodePoolLoggingConfig.md) |  | [optional] 
**machineType** | **String** | Optional. The desired [Google Compute Engine machine type](https://cloud.google.com/compute/docs/machine-types) for nodes in the node pool. Initiates an upgrade operation that migrates the nodes in the node pool to the specified machine type. | [optional] 
**name** | **String** | The name (project, location, cluster, node pool) of the node pool to update. Specified in the format &#x60;projects/_*_/locations/_*_/clusters/_*_/nodePools/_*&#x60;. | [optional] 
**nodeNetworkConfig** | [**NodeNetworkConfig**](NodeNetworkConfig.md) |  | [optional] 
**nodePoolId** | **String** | Deprecated. The name of the node pool to upgrade. This field has been deprecated and replaced by the name field. | [optional] 
**nodeVersion** | **String** | Required. The Kubernetes version to change the nodes to (typically an upgrade). Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - \&quot;latest\&quot;: picks the highest valid Kubernetes version - \&quot;1.X\&quot;: picks the highest valid patch+gke.N patch in the 1.X version - \&quot;1.X.Y\&quot;: picks the highest valid gke.N patch in the 1.X.Y version - \&quot;1.X.Y-gke.N\&quot;: picks an explicit Kubernetes version - \&quot;-\&quot;: picks the Kubernetes master version | [optional] 
**projectId** | **String** | Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field. | [optional] 
**queuedProvisioning** | [**QueuedProvisioning**](QueuedProvisioning.md) |  | [optional] 
**resourceLabels** | [**ResourceLabels**](ResourceLabels.md) |  | [optional] 
**resourceManagerTags** | [**ResourceManagerTags**](ResourceManagerTags.md) |  | [optional] 
**tags** | [**NetworkTags**](NetworkTags.md) |  | [optional] 
**taints** | [**NodeTaints**](NodeTaints.md) |  | [optional] 
**upgradeSettings** | [**UpgradeSettings**](UpgradeSettings.md) |  | [optional] 
**windowsNodeConfig** | [**WindowsNodeConfig**](WindowsNodeConfig.md) |  | [optional] 
**workloadMetadataConfig** | [**WorkloadMetadataConfig**](WorkloadMetadataConfig.md) |  | [optional] 
**zone** | **String** | Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field. | [optional] 


