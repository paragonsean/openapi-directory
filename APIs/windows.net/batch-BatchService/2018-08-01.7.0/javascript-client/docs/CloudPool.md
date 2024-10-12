# BatchService.CloudPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationState** | **String** |  | [optional] 
**allocationStateTransitionTime** | **Date** |  | [optional] 
**applicationLicenses** | **[String]** | The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail. | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) |  | [optional] 
**autoScaleEvaluationInterval** | **String** | This property is set only if the pool automatically scales, i.e. enableAutoScale is true. | [optional] 
**autoScaleFormula** | **String** | This property is set only if the pool automatically scales, i.e. enableAutoScale is true. | [optional] 
**autoScaleRun** | [**AutoScaleRun**](AutoScaleRun.md) |  | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**currentDedicatedNodes** | **Number** |  | [optional] 
**currentLowPriorityNodes** | **Number** | Low-priority compute nodes which have been preempted are included in this count. | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**eTag** | **String** | This is an opaque string. You can use it to detect whether the pool has changed between requests. In particular, you can be pass the ETag when updating a pool to specify that your changes should take effect only if nobody else has modified the pool in the meantime. | [optional] 
**enableAutoScale** | **Boolean** | If false, at least one of targetDedicateNodes and targetLowPriorityNodes must be specified. If true, the autoScaleFormula property is required and the pool automatically resizes according to the formula. The default value is false. | [optional] 
**enableInterNodeCommunication** | **Boolean** | This imposes restrictions on which nodes can be assigned to the pool. Specifying this value can reduce the chance of the requested number of nodes to be allocated in the pool. | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an account that differ only by case). | [optional] 
**lastModified** | **Date** | This is the last time at which the pool level data, such as the targetDedicatedNodes or enableAutoscale settings, changed. It does not factor in node-level changes such as a compute node changing state. | [optional] 
**maxTasksPerNode** | **Number** |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) |  | [optional] 
**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**resizeErrors** | [**[ResizeError]**](ResizeError.md) | This property is set only if one or more errors occurred during the last pool resize, and only when the pool allocationState is Steady. | [optional] 
**resizeTimeout** | **String** | This is the timeout for the most recent resize operation. (The initial sizing when the pool is created counts as a resize.) The default value is 15 minutes. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**state** | **String** |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**stats** | [**PoolStatistics**](PoolStatistics.md) |  | [optional] 
**targetDedicatedNodes** | **Number** |  | [optional] 
**targetLowPriorityNodes** | **Number** |  | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**url** | **String** |  | [optional] 
**userAccounts** | [**[UserAccount]**](UserAccount.md) |  | [optional] 
**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines in pools, see Choose a VM size for compute nodes in an Azure Batch pool (https://docs.microsoft.com/azure/batch/batch-pool-vm-sizes). | [optional] 



## Enum: AllocationStateEnum


* `steady` (value: `"steady"`)

* `resizing` (value: `"resizing"`)

* `stopping` (value: `"stopping"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `upgrading` (value: `"upgrading"`)




