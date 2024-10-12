

# AutoprovisioningNodePoolDefaults

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiskKmsKey** | **String** | The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption |  [optional] |
|**diskSizeGb** | **Integer** | Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB. |  [optional] |
|**diskType** | **String** | Type of the disk attached to each node (e.g. &#39;pd-standard&#39;, &#39;pd-ssd&#39; or &#39;pd-balanced&#39;) If unspecified, the default disk type is &#39;pd-standard&#39; |  [optional] |
|**imageType** | **String** | The image type to use for NAP created node. Please see https://cloud.google.com/kubernetes-engine/docs/concepts/node-images for available image types. |  [optional] |
|**insecureKubeletReadonlyPortEnabled** | **Boolean** | Enable or disable Kubelet read only port. |  [optional] |
|**management** | [**NodeManagement**](NodeManagement.md) |  |  [optional] |
|**minCpuPlatform** | **String** | Deprecated. Minimum CPU platform to be used for NAP created node pools. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: Intel Haswell or minCpuPlatform: Intel Sandy Bridge. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform). This field is deprecated, min_cpu_platform should be specified using &#x60;cloud.google.com/requested-min-cpu-platform&#x60; label selector on the pod. To unset the min cpu platform field pass \&quot;automatic\&quot; as field value. |  [optional] |
|**oauthScopes** | **List&lt;String&gt;** | Scopes that are used by NAP when creating node pools. |  [optional] |
|**serviceAccount** | **String** | The Google Cloud Platform Service Account to be used by the node VMs. |  [optional] |
|**shieldedInstanceConfig** | [**ShieldedInstanceConfig**](ShieldedInstanceConfig.md) |  |  [optional] |
|**upgradeSettings** | [**UpgradeSettings**](UpgradeSettings.md) |  |  [optional] |



