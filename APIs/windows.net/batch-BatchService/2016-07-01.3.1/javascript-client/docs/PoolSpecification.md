# BatchService.PoolSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | This property is currently not supported on auto pools created with the virtualMachineConfiguration (IaaS) property. | [optional] 
**autoScaleEvaluationInterval** | **String** | The default value is 15 minutes. The minimum and maximum value are 5 minutes and 168 hours respectively. If you specify a value less than 5 minutes or greater than 168 hours, the Batch service rejects the request with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 
**autoScaleFormula** | **String** | This property must not be specified if enableAutoScale is set to false. It is required if enableAutoScale is set to true. The formula is checked for validity before the pool is created. If the formula is not valid, the Batch service rejects the request with detailed error information. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of remoteuser, a certs directory is created in the user&#39;s home directory (e.g., /home/&lt;user-name&gt;/certs) where certificates are placed. | [optional] 
**cloudServiceConfiguration** | [**CloudServiceConfiguration**](CloudServiceConfiguration.md) |  | [optional] 
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**enableAutoScale** | **Boolean** | If false, the targetDedicated element is required. If true, the autoScaleFormula element is required. The pool automatically resizes according to the formula. The default value is false. | [optional] 
**enableInterNodeCommunication** | **Boolean** | Enabling inter-node communication limits the maximum size of the pool due to deployment restrictions on the nodes of the pool. This may result in the pool not reaching its desired size. The default value is false. | [optional] 
**maxTasksPerNode** | **Number** | The default value is 1. The maximum value of this setting depends on the size of the compute nodes in the pool (the vmSize setting). | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**resizeTimeout** | **String** | This timeout applies only to manual scaling; it has no effect when enableAutoScale is set to true. The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service rejects the request with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**targetDedicated** | **Number** | This property must not be specified if enableAutoScale is set to true. It is required if enableAutoScale is set to false. | [optional] 
**taskSchedulingPolicy** | [**TaskSchedulingPolicy**](TaskSchedulingPolicy.md) |  | [optional] 
**virtualMachineConfiguration** | [**VirtualMachineConfiguration**](VirtualMachineConfiguration.md) |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). | 


