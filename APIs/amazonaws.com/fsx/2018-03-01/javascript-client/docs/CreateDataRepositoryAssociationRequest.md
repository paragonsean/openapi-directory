# AmazonFsx.CreateDataRepositoryAssociationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileSystemId** | **String** | The globally unique ID of the file system, assigned by Amazon FSx. | 
**fileSystemPath** | **String** |  | [optional] 
**dataRepositoryPath** | **String** |  | 
**batchImportMetaDataOnCreate** | **Boolean** |  | [optional] 
**importedFileChunkSize** | **Number** |  | [optional] 
**s3** | [**CreateDataRepositoryAssociationRequestS3**](CreateDataRepositoryAssociationRequestS3.md) |  | [optional] 
**clientRequestToken** | **String** | (Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK. | [optional] 
**tags** | [**[Tag]**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. | [optional] 


