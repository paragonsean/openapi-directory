# BatchService.CloudPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationState** | **String** | steady - The pool is not resizing. There are no changes to the number of nodes in the pool in progress. A pool enters this state when it is created and when no operations are being performed on the pool to change the number of dedicated nodes. resizing - The pool is resizing; that is, compute nodes are being added to or removed from the pool. stopping - The pool was resizing, but the user has requested that the resize be stopped, but the stop request has not yet been completed. | [optional] 
**allocationStateTransitionTime** | **Date** |  | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) |  | [optional] 
**autoScaleEvaluationInterval** | **String** | This property is set only if the pool automatically scales, i.e. enableAutoScale is true. | [optional] 
**autoScaleFormula** | **String** | This property is set only if the pool automatically scales, i.e. enableAutoScale is true. | [optional] 
**autoScaleRun** | [**AutoScaleRun**](AutoScaleRun.md) |  | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**currentDedicated** | **Number** |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the pool has changed between requests. In particular, you can be pass the ETag when updating a pool to specify that your changes should take effect only if nobody else has modified the pool in the meantime. | [optional] 
**enableAutoScale** | **Boolean** | If true, the autoScaleFormula property must be set. If false, the targetDedicated property must be set. | [optional] 
**enableInterNodeCommunication** | **Boolean** | This imposes restrictions on which nodes can be assigned to the pool. Specifying this value can reduce the chance of the requested number of nodes to be allocated in the pool. | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. It is common to use a GUID for the id. | [optional] 
**lastModified** | **Date** | This is the last time at which the pool level data, such as the targetDedicated or enableAutoscale settings, changed. It does not factor in node-level changes such as a compute node changing state. | [optional] 
**maxTasksPerNode** | **Number** |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) |  | [optional] 
**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**resizeError** | [**ResizeError**](ResizeError.md) |  | [optional] 
**resizeTimeout** | **String** | This is the timeout for the most recent resize operation. (The initial sizing when the pool is created counts as a resize.) The default value is 15 minutes. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**state** | **String** | active - The pool is available to run tasks subject to the availability of compute nodes. deleting - The user has requested that the pool be deleted, but the delete operation has not yet completed. upgrading - The user has requested that the operating system of the pool&#39;s nodes be upgraded, but the upgrade operation has not yet completed (that is, some nodes in the pool have not yet been upgraded). While upgrading, the pool may be able to run tasks (with reduced capacity) but this is not guaranteed. | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**PoolStatistics**](PoolStatistics.md) |  | [optional] 
**targetDedicated** | **Number** | This property is not set if enableAutoScale is true. It is required if enableAutoScale is false. | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**url** | **String** |  | [optional] 
**userAccounts** | [**[UserAccount]**](UserAccount.md) |  | [optional] 
**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). | [optional] 



## Enum: AllocationStateEnum


* `steady` (value: `"steady"`)

* `resizing` (value: `"resizing"`)

* `stopping` (value: `"stopping"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `upgrading` (value: `"upgrading"`)




