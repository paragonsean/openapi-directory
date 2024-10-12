# VertexAiApi.GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataContentValidationStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalidRecordCount** | **String** | Number of records in this file we skipped due to validate errors. | [optional] 
**partialErrors** | [**[GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError]**](GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError.md) | The detail information of the partial failures encountered for those invalid records that couldn&#39;t be parsed. Up to 50 partial errors will be reported. | [optional] 
**sourceGcsUri** | **String** | Cloud Storage URI pointing to the original file in user&#39;s bucket. | [optional] 
**validRecordCount** | **String** | Number of records in this file that were successfully processed. | [optional] 


