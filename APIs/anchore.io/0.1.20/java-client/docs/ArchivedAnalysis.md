

# ArchivedAnalysis


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyzedAt** | **OffsetDateTime** |  |  [optional] |
|**annotations** | **Object** | User provided annotations as key-value pairs |  [optional] |
|**archiveSizeBytes** | **Integer** | The size, in bytes, of the analysis archive file |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**imageDigest** | **String** | The image digest (digest of the manifest describing the image, per docker spec) |  [optional] |
|**imageDetail** | [**List&lt;TagEntry&gt;**](TagEntry.md) | List of tags associated with the image digest |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**parentDigest** | **String** | The digest of a parent manifest (for manifest-list images) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The archival status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ARCHIVING | &quot;archiving&quot; |
| ARCHIVED | &quot;archived&quot; |
| DELETING | &quot;deleting&quot; |
| DELETED | &quot;deleted&quot; |



