

# InstanceGroupConfig

The config settings for Compute Engine resources in an instance group, such as a master or worker group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accelerators** | [**List&lt;AcceleratorConfig&gt;**](AcceleratorConfig.md) | Optional. The Compute Engine accelerator configuration for these instances. |  [optional] |
|**diskConfig** | [**DiskConfig**](DiskConfig.md) |  |  [optional] |
|**imageUri** | **String** | Optional. The Compute Engine image resource used for cluster instances.The URI can represent an image or image family.Image examples: https://www.googleapis.com/compute/v1/projects/[project_id]/global/images/[image-id] projects/[project_id]/global/images/[image-id] image-idImage family examples. Dataproc will use the most recent image from the family: https://www.googleapis.com/compute/v1/projects/[project_id]/global/images/family/[custom-image-family-name] projects/[project_id]/global/images/family/[custom-image-family-name]If the URI is unspecified, it will be inferred from SoftwareConfig.image_version or the system default. |  [optional] |
|**instanceFlexibilityPolicy** | [**InstanceFlexibilityPolicy**](InstanceFlexibilityPolicy.md) |  |  [optional] |
|**instanceNames** | **List&lt;String&gt;** | Output only. The list of instance names. Dataproc derives the names from cluster_name, num_instances, and the instance group. |  [optional] [readonly] |
|**instanceReferences** | [**List&lt;InstanceReference&gt;**](InstanceReference.md) | Output only. List of references to Compute Engine instances. |  [optional] [readonly] |
|**isPreemptible** | **Boolean** | Output only. Specifies that this instance group contains preemptible instances. |  [optional] [readonly] |
|**machineTypeUri** | **String** | Optional. The Compute Engine machine type used for cluster instances.A full URL, partial URI, or short name are valid. Examples: https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]/machineTypes/n1-standard-2 projects/[project_id]/zones/[zone]/machineTypes/n1-standard-2 n1-standard-2Auto Zone Exception: If you are using the Dataproc Auto Zone Placement (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement) feature, you must use the short name of the machine type resource, for example, n1-standard-2. |  [optional] |
|**managedGroupConfig** | [**ManagedGroupConfig**](ManagedGroupConfig.md) |  |  [optional] |
|**minCpuPlatform** | **String** | Optional. Specifies the minimum cpu platform for the Instance Group. See Dataproc -&gt; Minimum CPU Platform (https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu). |  [optional] |
|**minNumInstances** | **Integer** | Optional. The minimum number of primary worker instances to create. If min_num_instances is set, cluster creation will succeed if the number of primary workers created is at least equal to the min_num_instances number.Example: Cluster creation request with num_instances &#x3D; 5 and min_num_instances &#x3D; 3: If 4 VMs are created and 1 instance fails, the failed VM is deleted. The cluster is resized to 4 instances and placed in a RUNNING state. If 2 instances are created and 3 instances fail, the cluster in placed in an ERROR state. The failed VMs are not deleted. |  [optional] |
|**numInstances** | **Integer** | Optional. The number of VM instances in the instance group. For HA cluster master_config groups, must be set to 3. For standard cluster master_config groups, must be set to 1. |  [optional] |
|**preemptibility** | [**PreemptibilityEnum**](#PreemptibilityEnum) | Optional. Specifies the preemptibility of the instance group.The default value for master and worker groups is NON_PREEMPTIBLE. This default cannot be changed.The default value for secondary instances is PREEMPTIBLE. |  [optional] |
|**startupConfig** | [**StartupConfig**](StartupConfig.md) |  |  [optional] |



## Enum: PreemptibilityEnum

| Name | Value |
|---- | -----|
| PREEMPTIBILITY_UNSPECIFIED | &quot;PREEMPTIBILITY_UNSPECIFIED&quot; |
| NON_PREEMPTIBLE | &quot;NON_PREEMPTIBLE&quot; |
| PREEMPTIBLE | &quot;PREEMPTIBLE&quot; |
| SPOT | &quot;SPOT&quot; |



