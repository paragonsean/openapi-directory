

# LabVirtualMachineProperties

Properties of a virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactDeploymentStatus** | [**ArtifactDeploymentStatusProperties**](ArtifactDeploymentStatusProperties.md) |  |  [optional] |
|**artifacts** | [**List&lt;ArtifactInstallProperties&gt;**](ArtifactInstallProperties.md) | The artifacts to be installed on the virtual machine. |  [optional] |
|**computeId** | **String** | The resource identifier (Microsoft.Compute) of the virtual machine. |  [optional] |
|**createdByUser** | **String** | The email address of creator of the virtual machine. |  [optional] |
|**createdByUserId** | **String** | The object identifier of the creator of the virtual machine. |  [optional] |
|**customImageId** | **String** | The custom image identifier of the virtual machine. |  [optional] |
|**disallowPublicIpAddress** | **Boolean** | Indicates whether the virtual machine is to be created without a public IP address. |  [optional] |
|**fqdn** | **String** | The fully-qualified domain name of the virtual machine. |  [optional] |
|**galleryImageReference** | [**GalleryImageReference**](GalleryImageReference.md) |  |  [optional] |
|**isAuthenticationWithSshKey** | **Boolean** | A value indicating whether this virtual machine uses an SSH key for authentication. |  [optional] |
|**labSubnetName** | **String** | The lab subnet name of the virtual machine. |  [optional] |
|**labVirtualNetworkId** | **String** | The lab virtual network identifier of the virtual machine. |  [optional] |
|**notes** | **String** | The notes of the virtual machine. |  [optional] |
|**osType** | **String** | The OS type of the virtual machine. |  [optional] |
|**ownerObjectId** | **String** | The object identifier of the owner of the virtual machine. |  [optional] |
|**password** | **String** | The password of the virtual machine administrator. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**size** | **String** | The size of the virtual machine. |  [optional] |
|**sshKey** | **String** | The SSH key of the virtual machine administrator. |  [optional] |
|**userName** | **String** | The user name of the virtual machine. |  [optional] |



