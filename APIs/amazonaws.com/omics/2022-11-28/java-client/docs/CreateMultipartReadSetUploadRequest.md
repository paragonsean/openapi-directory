

# CreateMultipartReadSetUploadRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** |  An idempotency token that can be used to avoid triggering multiple multipart uploads.  |  [optional] |
|**sourceFileType** | [**SourceFileTypeEnum**](#SourceFileTypeEnum) |  The type of file being uploaded.  |  |
|**subjectId** | **String** |  The source&#39;s subject ID.  |  |
|**sampleId** | **String** |  The source&#39;s sample ID.  |  |
|**generatedFrom** | **String** |  Where the source originated.  |  [optional] |
|**referenceArn** | **String** |  The ARN of the reference.  |  |
|**name** | **String** |  The name of the read set.  |  |
|**description** | **String** |  The description of the read set.  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** |  Any tags to add to the read set.  |  [optional] |



## Enum: SourceFileTypeEnum

| Name | Value |
|---- | -----|
| FASTQ | &quot;FASTQ&quot; |
| BAM | &quot;BAM&quot; |
| CRAM | &quot;CRAM&quot; |



