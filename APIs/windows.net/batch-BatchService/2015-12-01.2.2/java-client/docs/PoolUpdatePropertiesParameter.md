

# PoolUpdatePropertiesParameter

Parameters for a CloudPoolOperations.UpdateProperties request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | Sets a list of application packages to be installed on each compute node in the pool. If you specify an empty collection, any existing application packages references are removed from the pool. |  |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | Sets a list of certificates to be installed on each compute node in the pool. If you specify an empty collection, any existing certificate references are removed from the pool. |  |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Sets a list of name-value pairs associated with the pool as metadata. If you specify an empty collection, any existing metadata is removed from the pool. |  |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |



