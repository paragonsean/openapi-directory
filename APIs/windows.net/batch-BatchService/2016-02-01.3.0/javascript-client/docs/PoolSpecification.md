# BatchService.PoolSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | The list of application packages to be installed on each compute node in the pool. | [optional] 
**autoScaleEvaluationInterval** | **String** | A time interval for the desired AutoScale evaluation period in the pool. | [optional] 
**autoScaleFormula** | **String** | The formula for the desired number of compute nodes in the pool. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | A list of certificates to be installed on each compute node in the pool. | [optional] 
**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  | [optional] 
**displayName** | **String** | The display name for the pool. | [optional] 
**enableAutoScale** | **Boolean** | Whether the pool size should automatically adjust over time. | [optional] 
**enableInterNodeCommunication** | **Boolean** | Whether the pool permits direct communication between nodes. | [optional] 
**maxTasksPerNode** | **Number** | The maximum number of tasks that can run concurrently on a single compute node in the pool. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | A list of name-value pairs associated with the pool as metadata. | [optional] 
**resizeTimeout** | **String** | The timeout for allocation of compute nodes to the pool. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**targetDedicated** | **Number** | The desired number of compute nodes in the pool. | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  | [optional] 
**vmSize** | **String** | The size of the virtual machines in the pool. All virtual machines in a pool are the same size. | [optional] 


