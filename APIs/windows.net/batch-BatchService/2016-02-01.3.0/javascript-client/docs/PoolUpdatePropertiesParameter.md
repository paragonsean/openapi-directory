# BatchService.PoolUpdatePropertiesParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | A list of application packages to be installed on each compute node in the pool. If you specify an empty collection, any existing application packages references are removed from the pool. | 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | A list of certificates to be installed on each compute node in the pool. If you specify an empty collection, any existing certificate references are removed from the pool. | 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | A list of name-value pairs associated with the pool as metadata. If you specify an empty collection, any existing metadata is removed from the pool. | 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 


