# BatchService.PoolPatchParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageReferences** | [**[ApplicationPackageReference]**](ApplicationPackageReference.md) | Sets a list of application packages to be installed on each compute node in the pool. If omitted, any existing application package references are left unchanged. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | Sets a list of certificates to be installed on each compute node in the pool. If omitted, any existing certificate references are left unchanged. | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | Sets a list of name-value pairs associated with the pool as metadata. If omitted, any existing metadata is left unchanged. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 


