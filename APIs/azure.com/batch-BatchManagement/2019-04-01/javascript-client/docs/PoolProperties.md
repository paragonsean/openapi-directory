# BatchManagement.PoolProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationState** | **String** |  | [optional] [readonly] 
**allocationStateTransitionTime** | **Date** |  | [optional] [readonly] 
**applicationLicenses** | **[String]** | The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail. | [optional] 
**applicationPackages** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | Changes to application package references affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged. There is a maximum of 10 application package references on any given pool. | [optional] 
**autoScaleRun** | [**AutoScaleRun**](AutoScaleRun.md) |  | [optional] 
**certificates** | [**[CertificateReference]**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**creationTime** | **Date** |  | [optional] [readonly] 
**currentDedicatedNodes** | **Number** |  | [optional] [readonly] 
**currentLowPriorityNodes** | **Number** |  | [optional] [readonly] 
**deploymentConfiguration** | [**DeploymentConfiguration**](DeploymentConfiguration.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**interNodeCommunication** | **String** | This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to &#39;Disabled&#39;. | [optional] 
**lastModified** | **Date** | This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state. | [optional] [readonly] 
**maxTasksPerNode** | **Number** | The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**provisioningState** | **String** |  | [optional] [readonly] 
**provisioningStateTransitionTime** | **Date** |  | [optional] [readonly] 
**resizeOperationStatus** | [**ResizeOperationStatus**](ResizeOperationStatus.md) |  | [optional] 
**scaleSettings** | [**ScaleSettings**](ScaleSettings.md) |  | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**userAccounts** | [**[UserAccount]**](UserAccount.md) |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (https://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). | [optional] 



## Enum: AllocationStateEnum


* `Steady` (value: `"Steady"`)

* `Resizing` (value: `"Resizing"`)

* `Stopping` (value: `"Stopping"`)





## Enum: InterNodeCommunicationEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Deleting` (value: `"Deleting"`)




