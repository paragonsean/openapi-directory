

# UpdateDataRepositoryAssociationResponseAssociation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associationId** | [**String**](String.md) |  |  [optional] |
|**resourceARN** | **String** | The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. |  [optional] |
|**fileSystemId** | **String** | The globally unique ID of the file system, assigned by Amazon FSx. |  [optional] |
|**lifecycle** | [**DataRepositoryLifecycle**](DataRepositoryLifecycle.md) |  |  [optional] |
|**failureDetails** | [**DataRepositoryFailureDetails**](DataRepositoryFailureDetails.md) |  |  [optional] |
|**fileSystemPath** | [**String**](String.md) |  |  [optional] |
|**dataRepositoryPath** | [**String**](String.md) |  |  [optional] |
|**batchImportMetaDataOnCreate** | [**Boolean**](Boolean.md) |  |  [optional] |
|**importedFileChunkSize** | [**Integer**](Integer.md) |  |  [optional] |
|**S3** | [**DataRepositoryAssociationS3**](DataRepositoryAssociationS3.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. |  [optional] |
|**creationTime** | **OffsetDateTime** | The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time. |  [optional] |
|**fileCacheId** | [**String**](String.md) |  |  [optional] |
|**fileCachePath** | [**String**](String.md) |  |  [optional] |
|**dataRepositorySubdirectories** | [**List**](List.md) |  |  [optional] |
|**NFS** | [**DataRepositoryAssociationNFS**](DataRepositoryAssociationNFS.md) |  |  [optional] |



