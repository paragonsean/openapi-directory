

# AutoprovisioningNodePoolDefaults

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiskKmsKey** | **String** |  The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption |  [optional] |
|**diskSizeGb** | **Integer** | Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB. |  [optional] |
|**diskType** | **String** | Type of the disk attached to each node (e.g. &#39;pd-standard&#39;, &#39;pd-ssd&#39; or &#39;pd-balanced&#39;) If unspecified, the default disk type is &#39;pd-standard&#39; |  [optional] |
|**imageType** | **String** | The image type to use for NAP created node. Please see https://cloud.google.com/kubernetes-engine/docs/concepts/node-images for available image types. |  [optional] |
|**insecureKubeletReadonlyPortEnabled** | **Boolean** | Enable or disable Kubelet read only port. |  [optional] |
|**management** | [**NodeManagement**](NodeManagement.md) |  |  [optional] |
|**minCpuPlatform** | **String** | Deprecated. Minimum CPU platform to be used for NAP created node pools. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: Intel Haswell or minCpuPlatform: Intel Sandy Bridge. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform). This field is deprecated, min_cpu_platform should be specified using &#x60;cloud.google.com/requested-min-cpu-platform&#x60; label selector on the pod. To unset the min cpu platform field pass \&quot;automatic\&quot; as field value. |  [optional] |
|**oauthScopes** | **List&lt;String&gt;** | The set of Google API scopes to be made available on all of the node VMs under the \&quot;default\&quot; service account. The following scopes are recommended, but not required, and by default are not included: * &#x60;https://www.googleapis.com/auth/compute&#x60; is required for mounting persistent storage on your nodes. * &#x60;https://www.googleapis.com/auth/devstorage.read_only&#x60; is required for communicating with **gcr.io** (the [Google Container Registry](https://cloud.google.com/container-registry/)). If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added. |  [optional] |
|**serviceAccount** | **String** | The Google Cloud Platform Service Account to be used by the node VMs. Specify the email address of the Service Account; otherwise, if no Service Account is specified, the \&quot;default\&quot; service account is used. |  [optional] |
|**shieldedInstanceConfig** | [**ShieldedInstanceConfig**](ShieldedInstanceConfig.md) |  |  [optional] |
|**upgradeSettings** | [**UpgradeSettings**](UpgradeSettings.md) |  |  [optional] |



