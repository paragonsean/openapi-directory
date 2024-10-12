# ApigeeApi.GoogleCloudApigeeV1ArchiveDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | Output only. The time at which the Archive Deployment was created in milliseconds since the epoch. | [optional] [readonly] 
**gcsUri** | **String** | Input only. The Google Cloud Storage signed URL returned from GenerateUploadUrl and used to upload the Archive zip file. | [optional] 
**labels** | **{String: String}** | User-supplied key-value pairs used to organize ArchiveDeployments. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. | [optional] 
**name** | **String** | Name of the Archive Deployment in the following format: &#x60;organizations/{org}/environments/{env}/archiveDeployments/{id}&#x60;. | [optional] 
**operation** | **String** | Output only. A reference to the LRO that created this Archive Deployment in the following format: &#x60;organizations/{org}/operations/{id}&#x60; | [optional] [readonly] 
**updatedAt** | **String** | Output only. The time at which the Archive Deployment was updated in milliseconds since the epoch. | [optional] [readonly] 


