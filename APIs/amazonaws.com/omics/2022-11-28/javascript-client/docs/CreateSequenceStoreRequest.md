# AmazonOmics.CreateSequenceStoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | A name for the store. | 
**description** | **String** | A description for the store. | [optional] 
**sseConfig** | [**CreateAnnotationStoreRequestSseConfig**](CreateAnnotationStoreRequestSseConfig.md) |  | [optional] 
**tags** | **{String: String}** | Tags for the store. | [optional] 
**clientToken** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique token for each request. | [optional] 
**fallbackLocation** | **String** |  An S3 location that is used to store files that have failed a direct upload.  | [optional] 


