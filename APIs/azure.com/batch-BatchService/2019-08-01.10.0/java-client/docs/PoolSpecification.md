

# PoolSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationLicenses** | **List&lt;String&gt;** | The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, Pool creation will fail. The permitted licenses available on the Pool are &#39;maya&#39;, &#39;vray&#39;, &#39;3dsmax&#39;, &#39;arnold&#39;. An additional charge applies for each application license added to the Pool. |  [optional] |
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Package references on any given Pool. |  [optional] |
|**autoScaleEvaluationInterval** | **String** | The default value is 15 minutes. The minimum and maximum value are 5 minutes and 168 hours respectively. If you specify a value less than 5 minutes or greater than 168 hours, the Batch service rejects the request with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |
|**autoScaleFormula** | **String** | This property must not be specified if enableAutoScale is set to false. It is required if enableAutoScale is set to true. The formula is checked for validity before the Pool is created. If the formula is not valid, the Batch service rejects the request with detailed error information. |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | For Windows Nodes, the Batch service installs the Certificates to the specified Certificate store and location. For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory. |  [optional] |
|**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  |  [optional] |
|**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |  [optional] |
|**enableAutoScale** | **Boolean** | If false, at least one of targetDedicateNodes and targetLowPriorityNodes must be specified. If true, the autoScaleFormula element is required. The Pool automatically resizes according to the formula. The default value is false. |  [optional] |
|**enableInterNodeCommunication** | **Boolean** | Enabling inter-node communication limits the maximum size of the Pool due to deployment restrictions on the Compute Nodes of the Pool. This may result in the Pool not reaching its desired size. The default value is false. |  [optional] |
|**maxTasksPerNode** | **Integer** | The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the Pool or 256. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |  [optional] |
|**mountConfiguration** | [**List&lt;MountConfiguration&gt;**](MountConfiguration.md) | This supports Azure Files, NFS, CIFS/SMB, and Blobfuse. |  [optional] |
|**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  |  [optional] |
|**resizeTimeout** | **String** | This timeout applies only to manual scaling; it has no effect when enableAutoScale is set to true. The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service rejects the request with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |
|**targetDedicatedNodes** | **Integer** | This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both. |  [optional] |
|**targetLowPriorityNodes** | **Integer** | This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both. |  [optional] |
|**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  |  [optional] |
|**userAccounts** | [**List&lt;UserAccount&gt;**](UserAccount.md) |  |  [optional] |
|**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  |  [optional] |
|**vmSize** | **String** | For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (https://docs.microsoft.com/azure/batch/batch-pool-vm-sizes). |  |



