

# PoolSpecification

Specification for creating a new pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | Gets or sets the list of application packages to be installed on each compute node in the pool. |  [optional] |
|**autoScaleEvaluationInterval** | **String** | Gets or sets a time interval for the desired AutoScale evaluation period in the pool. |  [optional] |
|**autoScaleFormula** | **String** | Gets or sets the formula for the desired number of compute nodes in the pool. |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | Gets or sets a list of certificates to be installed on each compute node in the pool. |  [optional] |
|**displayName** | **String** | Gets or sets the display name for the pool. |  [optional] |
|**enableAutoScale** | **Boolean** | Gets or sets whether the pool size should automatically adjust over time. |  [optional] |
|**enableInterNodeCommunication** | **Boolean** | Gets or sets whether the pool permits direct communication between nodes. |  [optional] |
|**maxTasksPerNode** | **Integer** | Gets or sets the maximum number of tasks that can run concurrently on a single compute node in the pool. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the pool as metadata. |  [optional] |
|**osFamily** | **String** | Gets or sets the Azure Guest OS family to be installed on the virtual machines in the pool. |  [optional] |
|**resizeTimeout** | **String** | Gets or sets the timeout for allocation of compute nodes to the pool. |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |
|**targetDedicated** | **Integer** | Gets or sets the desired number of compute nodes in the pool. |  [optional] |
|**targetOSVersion** | **String** | Gets or sets the Azure Guest OS version to be installed on the virtual machines in the pool. |  [optional] |
|**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  |  [optional] |
|**vmSize** | **String** | Gets or sets the size of the virtual machines in the pool. All VMs in a pool are the same size. |  [optional] |



