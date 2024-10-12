# BatchService.PoolUpdatePropertiesParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | The list replaces any existing application package references on the pool. Changes to application package references affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged. If omitted, or if you specify an empty collection, any existing application packages references are removed from the pool. | 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | This list replaces any existing certificate references configured on the pool. If you specify an empty collection, any existing certificate references are removed from the pool. For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | This list replaces any existing metadata configured on the pool. If omitted, or if you specify an empty collection, any existing metadata is removed from the pool. | 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 


