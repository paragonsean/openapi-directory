# AnchoreEngineApiServer.ArchivedAnalysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzedAt** | **Date** |  | [optional] 
**annotations** | **Object** | User provided annotations as key-value pairs | [optional] 
**archiveSizeBytes** | **Number** | The size, in bytes, of the analysis archive file | [optional] 
**createdAt** | **Date** |  | [optional] 
**imageDigest** | **String** | The image digest (digest of the manifest describing the image, per docker spec) | [optional] 
**imageDetail** | [**[TagEntry]**](TagEntry.md) | List of tags associated with the image digest | [optional] 
**lastUpdated** | **Date** |  | [optional] 
**parentDigest** | **String** | The digest of a parent manifest (for manifest-list images) | [optional] 
**status** | **String** | The archival status | [optional] 



## Enum: StatusEnum


* `archiving` (value: `"archiving"`)

* `archived` (value: `"archived"`)

* `deleting` (value: `"deleting"`)

* `deleted` (value: `"deleted"`)




