

# CreateDataRepositoryAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemId** | **String** | The globally unique ID of the file system, assigned by Amazon FSx. |  |
|**fileSystemPath** | [**String**](String.md) |  |  [optional] |
|**dataRepositoryPath** | [**String**](String.md) |  |  |
|**batchImportMetaDataOnCreate** | [**Boolean**](Boolean.md) |  |  [optional] |
|**importedFileChunkSize** | [**Integer**](Integer.md) |  |  [optional] |
|**S3** | [**CreateDataRepositoryAssociationRequestS3**](CreateDataRepositoryAssociationRequestS3.md) |  |  [optional] |
|**clientRequestToken** | **String** | (Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. |  [optional] |



