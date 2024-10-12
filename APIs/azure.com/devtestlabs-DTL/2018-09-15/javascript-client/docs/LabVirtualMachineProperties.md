# DevTestLabsClient.LabVirtualMachineProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowClaim** | **Boolean** | Indicates whether another user can take ownership of the virtual machine | [optional] 
**applicableSchedule** | [**ApplicableSchedule**](ApplicableSchedule.md) |  | [optional] 
**artifactDeploymentStatus** | [**ArtifactDeploymentStatusProperties**](ArtifactDeploymentStatusProperties.md) |  | [optional] 
**artifacts** | [**[ArtifactInstallProperties]**](ArtifactInstallProperties.md) | The artifacts to be installed on the virtual machine. | [optional] 
**computeId** | **String** | The resource identifier (Microsoft.Compute) of the virtual machine. | [optional] 
**computeVm** | [**ComputeVmProperties**](ComputeVmProperties.md) |  | [optional] 
**createdByUser** | **String** | The email address of creator of the virtual machine. | [optional] 
**createdByUserId** | **String** | The object identifier of the creator of the virtual machine. | [optional] 
**createdDate** | **Date** | The creation date of the virtual machine. | [optional] 
**customImageId** | **String** | The custom image identifier of the virtual machine. | [optional] 
**dataDiskParameters** | [**[DataDiskProperties]**](DataDiskProperties.md) | New or existing data disks to attach to the virtual machine after creation | [optional] 
**disallowPublicIpAddress** | **Boolean** | Indicates whether the virtual machine is to be created without a public IP address. | [optional] 
**environmentId** | **String** | The resource ID of the environment that contains this virtual machine, if any. | [optional] 
**expirationDate** | **Date** | The expiration date for VM. | [optional] 
**fqdn** | **String** | The fully-qualified domain name of the virtual machine. | [optional] 
**galleryImageReference** | [**GalleryImageReference**](GalleryImageReference.md) |  | [optional] 
**isAuthenticationWithSshKey** | **Boolean** | Indicates whether this virtual machine uses an SSH key for authentication. | [optional] 
**labSubnetName** | **String** | The lab subnet name of the virtual machine. | [optional] 
**labVirtualNetworkId** | **String** | The lab virtual network identifier of the virtual machine. | [optional] 
**lastKnownPowerState** | **String** | Last known compute power state captured in DTL | [optional] 
**networkInterface** | [**NetworkInterfaceProperties**](NetworkInterfaceProperties.md) |  | [optional] 
**notes** | **String** | The notes of the virtual machine. | [optional] 
**osType** | **String** | The OS type of the virtual machine. | [optional] 
**ownerObjectId** | **String** | The object identifier of the owner of the virtual machine. | [optional] 
**ownerUserPrincipalName** | **String** | The user principal name of the virtual machine owner. | [optional] 
**password** | **String** | The password of the virtual machine administrator. | [optional] 
**planId** | **String** | The id of the plan associated with the virtual machine image | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] [readonly] 
**scheduleParameters** | [**[ScheduleCreationParameter]**](ScheduleCreationParameter.md) | Virtual Machine schedules to be created | [optional] 
**size** | **String** | The size of the virtual machine. | [optional] 
**sshKey** | **String** | The SSH key of the virtual machine administrator. | [optional] 
**storageType** | **String** | Storage type to use for virtual machine (i.e. Standard, Premium). | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] [readonly] 
**userName** | **String** | The user name of the virtual machine. | [optional] 
**virtualMachineCreationSource** | **String** | Tells source of creation of lab virtual machine. Output property only. | [optional] 



## Enum: VirtualMachineCreationSourceEnum


* `FromCustomImage` (value: `"FromCustomImage"`)

* `FromGalleryImage` (value: `"FromGalleryImage"`)

* `FromSharedGalleryImage` (value: `"FromSharedGalleryImage"`)




