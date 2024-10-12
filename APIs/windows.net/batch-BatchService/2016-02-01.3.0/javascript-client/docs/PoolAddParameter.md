# BatchService.PoolAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | The list of application packages to be installed on each compute node in the pool. | [optional] 
**autoScaleEvaluationInterval** | **String** | A time interval for the desired autoscale evaluation period in the pool. | [optional] 
**autoScaleFormula** | **String** | A formula for the desired number of compute nodes in the pool. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | The list of certificates to be installed on each compute node in the pool. | [optional] 
**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  | [optional] 
**displayName** | **String** | The display name for the pool. | [optional] 
**enableAutoScale** | **Boolean** | Whether the pool size should automatically adjust over time. If true, the AutoScaleFormula property must be set. If false, the TargetDedicated property must be set. | [optional] 
**enableInterNodeCommunication** | **Boolean** | Whether the pool permits direct communication between nodes. | [optional] 
**id** | **String** | A string that uniquely identifies the pool within the account. The id can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. | 
**maxTasksPerNode** | **Number** | The maximum number of tasks that can run concurrently on a single compute node in the pool. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | A list of name-value pairs associated with the pool as metadata. | [optional] 
**resizeTimeout** | **String** | The timeout for allocation of compute nodes to the pool. In a Get Pool operation, this is the timeout for the most recent resize operation. The default value is 10 minutes. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**targetDedicated** | **Number** | The desired number of compute nodes in the pool. This property must have the default value if EnableAutoScale is true. It is required if EnableAutoScale is false. | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  | [optional] 
**vmSize** | **String** | The size of virtual machines in the pool. All virtual machines in a pool are the same size. | 


