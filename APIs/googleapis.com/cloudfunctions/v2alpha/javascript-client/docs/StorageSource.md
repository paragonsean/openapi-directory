# CloudFunctionsApi.StorageSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | Google Cloud Storage bucket containing the source (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). | [optional] 
**generation** | **String** | Google Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used. | [optional] 
**object** | **String** | Google Cloud Storage object containing the source. This object must be a gzipped archive file (&#x60;.tar.gz&#x60;) containing source to build. | [optional] 


