# DevTestLabsClient.LabProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**LabAnnouncementProperties**](LabAnnouncementProperties.md) |  | [optional] 
**artifactsStorageAccount** | **String** | The lab&#39;s artifact storage account. | [optional] [readonly] 
**createdDate** | **Date** | The creation date of the lab. | [optional] [readonly] 
**defaultPremiumStorageAccount** | **String** | The lab&#39;s default premium storage account. | [optional] [readonly] 
**defaultStorageAccount** | **String** | The lab&#39;s default storage account. | [optional] [readonly] 
**environmentPermission** | **String** | The access rights to be granted to the user when provisioning an environment | [optional] 
**extendedProperties** | **{String: String}** | Extended properties of the lab used for experimental features | [optional] 
**labStorageType** | **String** | Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. | [optional] 
**loadBalancerId** | **String** | The load balancer used to for lab VMs that use shared IP address. | [optional] [readonly] 
**mandatoryArtifactsResourceIdsLinux** | **[String]** | The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user. | [optional] 
**mandatoryArtifactsResourceIdsWindows** | **[String]** | The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user. | [optional] 
**networkSecurityGroupId** | **String** | The Network Security Group attached to the lab VMs Network interfaces to restrict open ports. | [optional] [readonly] 
**premiumDataDiskStorageAccount** | **String** | The lab&#39;s premium data disk storage account. | [optional] [readonly] 
**premiumDataDisks** | **String** | The setting to enable usage of premium data disks.  When its value is &#39;Enabled&#39;, creation of standard or premium data disks is allowed.  When its value is &#39;Disabled&#39;, only creation of standard data disks is allowed. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] [readonly] 
**publicIpId** | **String** | The public IP address for the lab&#39;s load balancer. | [optional] [readonly] 
**support** | [**LabSupportProperties**](LabSupportProperties.md) |  | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] [readonly] 
**vaultName** | **String** | The lab&#39;s Key vault. | [optional] [readonly] 
**vmCreationResourceGroup** | **String** | The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null. | [optional] [readonly] 



## Enum: EnvironmentPermissionEnum


* `Reader` (value: `"Reader"`)

* `Contributor` (value: `"Contributor"`)





## Enum: LabStorageTypeEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `StandardSSD` (value: `"StandardSSD"`)





## Enum: PremiumDataDisksEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




