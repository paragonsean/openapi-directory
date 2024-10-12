

# CloudPool

A pool in the Azure Batch service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocationState** | [**AllocationStateEnum**](#AllocationStateEnum) | Whether the pool is resizing. |  [optional] |
|**allocationStateTransitionTime** | **OffsetDateTime** | The time at which the pool entered its current allocation state. |  [optional] |
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | The list of application packages to be installed on each compute node in the pool. |  [optional] |
|**autoScaleEvaluationInterval** | **String** | A time interval for the desired AutoScale evaluation period in the pool. |  [optional] |
|**autoScaleFormula** | **String** | A formula for the desired number of compute nodes in the pool. |  [optional] |
|**autoScaleRun** | [**AutoScaleRun**](AutoScaleRun.md) |  |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | The list of certificates to be installed on each compute node in the pool. |  [optional] |
|**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | The creation time of the pool. |  [optional] |
|**currentDedicated** | **Integer** | The number of compute nodes currently in the pool. |  [optional] |
|**displayName** | **String** | The display name for the pool. |  [optional] |
|**eTag** | **String** | The ETag of the pool. |  [optional] |
|**enableAutoScale** | **Boolean** | Whether the pool size should automatically adjust over time. If true, the AutoScaleFormula property must be set. If false, the TargetDedicated property must be set. |  [optional] |
|**enableInterNodeCommunication** | **Boolean** | Whether the pool permits direct communication between nodes. |  [optional] |
|**id** | **String** | A string that uniquely identifies the pool within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified time of the pool. |  [optional] |
|**maxTasksPerNode** | **Integer** | The maximum number of tasks that can run concurrently on a single compute node in the pool. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | A list of name-value pairs associated with the pool as metadata. |  [optional] |
|**resizeError** | [**ResizeError**](ResizeError.md) |  |  [optional] |
|**resizeTimeout** | **String** | The timeout for allocation of compute nodes to the pool. In a Get Pool operation, this is the timeout for the most recent resize operation. The default value is 10 minutes. |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the pool. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | The time at which the pool entered its current state. |  [optional] |
|**stats** | [**PoolStatistics**](PoolStatistics.md) |  |  [optional] |
|**targetDedicated** | **Integer** | The desired number of compute nodes in the pool. This property must have the default value if EnableAutoScale is true. It is required if EnableAutoScale is false. |  [optional] |
|**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  |  [optional] |
|**url** | **String** | The URL of the pool. |  [optional] |
|**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  |  [optional] |
|**vmSize** | **String** | The size of virtual machines in the pool. All virtual machines in a pool are the same size. |  [optional] |



## Enum: AllocationStateEnum

| Name | Value |
|---- | -----|
| STEADY | &quot;steady&quot; |
| RESIZING | &quot;resizing&quot; |
| STOPPING | &quot;stopping&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DELETING | &quot;deleting&quot; |
| UPGRADING | &quot;upgrading&quot; |



