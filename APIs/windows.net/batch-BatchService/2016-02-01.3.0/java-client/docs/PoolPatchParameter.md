

# PoolPatchParameter

Parameters for a CloudPoolOperations.Patch request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPackageReferences** | [**List&lt;ApplicationPackageReference&gt;**](ApplicationPackageReference.md) | A list of application packages to be installed on each compute node in the pool. If omitted, any existing application package references are left unchanged. |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | A list of certificates to be installed on each compute node in the pool. If omitted, any existing certificate references are left unchanged. |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | A list of name-value pairs associated with the pool as metadata. If omitted, any existing metadata is left unchanged. |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |



