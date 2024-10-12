# BatchService.CloudPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationState** | **String** | Gets or sets whether the pool is resizing. | [optional] 
**allocationStateTransitionTime** | **Date** | Gets or sets the time at which the pool entered its current allocation state. | [optional] 
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | Gets or sets the list of application packages to be installed on each compute node in the pool. | [optional] 
**autoScaleEvaluationInterval** | **String** | Gets or sets a time interval for the desired AutoScale evaluation period in the pool. | [optional] 
**autoScaleFormula** | **String** | Gets or sets a formula for the desired number of compute nodes in the pool. | [optional] 
**autoScaleRun** | [**AutoScaleRun**](AutoScaleRun.md) |  | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | Gets or sets the list of certificates to be installed on each compute node in the pool. | [optional] 
**creationTime** | **Date** | Gets or sets the creation time of the pool. | [optional] 
**currentDedicated** | **Number** | Gets or sets the number of compute nodes currently in the pool. | [optional] 
**currentOSVersion** | **String** | Gets or sets the Azure Guest OS Version currently installed on the virtual machines in the pool. This may differ from TargetOSVersion if the pool state is Upgrading. | [optional] 
**displayName** | **String** | Gets or sets the display name for the pool. | [optional] 
**eTag** | **String** | Gets or sets the ETag of the pool. | [optional] 
**enableAutoScale** | **Boolean** | Gets or sets whether the pool size should automatically adjust over time. If true, the AutoScaleFormula property must be set. If false, the TargetDedicated property must be set. | [optional] 
**enableInterNodeCommunication** | **Boolean** | Gets or sets whether the pool permits direct communication between nodes. | [optional] 
**id** | **String** | Gets or sets a string that uniquely identifies the pool within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | [optional] 
**lastModified** | **Date** | Gets or sets the last modified time of the pool. | [optional] 
**maxTasksPerNode** | **Number** | Gets or sets the maximum number of tasks that can run concurrently on a single compute node in the pool. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the pool as metadata. | [optional] 
**osFamily** | **String** | Gets or sets the Azure Guest OS family to be installed on the virtual machines in the pool. | [optional] 
**resizeError** | [**ResizeError**](ResizeError.md) |  | [optional] 
**resizeTimeout** | **String** | Gets or sets the timeout for allocation of compute nodes to the pool. In a Get Pool operation, this is the timeout for the most recent resize operation. The default value is 10 minutes. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**state** | **String** | Gets or sets the current state of the pool. | [optional] 
**stateTransitionTime** | **Date** | Gets or sets the time at which the pool entered its current state. | [optional] 
**stats** | [**PoolStatistics**](PoolStatistics.md) |  | [optional] 
**targetDedicated** | **Number** | Gets or sets the desired number of compute nodes in the pool. This property must have the default value if EnableAutoScale is true. It is required if EnableAutoScale is false. | [optional] 
**targetOSVersion** | **String** | Gets or sets the Azure Guest OS version to be installed on the virtual machines in the pool. The default value is * which specifies the latest operating system version for the specified family. | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**url** | **String** | Gets or sets the URL of the pool. | [optional] 
**vmSize** | **String** | Gets or sets the size of virtual machines in the pool.  All VMs in a pool are the same size. | [optional] 



## Enum: AllocationStateEnum


* `steady` (value: `"steady"`)

* `resizing` (value: `"resizing"`)

* `stopping` (value: `"stopping"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `upgrading` (value: `"upgrading"`)




