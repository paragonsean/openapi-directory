# StorageTransferApi.TransferSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**awsS3CompatibleDataSource** | [**AwsS3CompatibleData**](AwsS3CompatibleData.md) |  | [optional] 
**awsS3DataSource** | [**AwsS3Data**](AwsS3Data.md) |  | [optional] 
**azureBlobStorageDataSource** | [**AzureBlobStorageData**](AzureBlobStorageData.md) |  | [optional] 
**gcsDataSink** | [**GcsData**](GcsData.md) |  | [optional] 
**gcsDataSource** | [**GcsData**](GcsData.md) |  | [optional] 
**gcsIntermediateDataLocation** | [**GcsData**](GcsData.md) |  | [optional] 
**hdfsDataSource** | [**HdfsData**](HdfsData.md) |  | [optional] 
**httpDataSource** | [**HttpData**](HttpData.md) |  | [optional] 
**objectConditions** | [**ObjectConditions**](ObjectConditions.md) |  | [optional] 
**posixDataSink** | [**PosixFilesystem**](PosixFilesystem.md) |  | [optional] 
**posixDataSource** | [**PosixFilesystem**](PosixFilesystem.md) |  | [optional] 
**sinkAgentPoolName** | **String** | Specifies the agent pool name associated with the posix data sink. When unspecified, the default name is used. | [optional] 
**sourceAgentPoolName** | **String** | Specifies the agent pool name associated with the posix data source. When unspecified, the default name is used. | [optional] 
**transferManifest** | [**TransferManifest**](TransferManifest.md) |  | [optional] 
**transferOptions** | [**TransferOptions**](TransferOptions.md) |  | [optional] 


