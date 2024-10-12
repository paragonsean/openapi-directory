

# AnalysisArchiveSummary

A summarization of the analysis archive, including size, counts, etc. This archive stores image analysis only, never the actual image content or layers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdated** | **OffsetDateTime** | The timestamp of the most recent archived image |  [optional] |
|**totalDataBytes** | **Integer** | The total sum of all the bytes stored to the backing storage. Accounts for anchore-applied compression, but not compression by the underlying storage system. |  [optional] |
|**totalImageCount** | **Integer** | The number of unique images (digests) in the archive |  [optional] |
|**totalTagCount** | **Integer** | The number of tag records (registry/repo:tag pull strings) in the archive. This may include repeated tags but will always have a unique tag-&gt;digest mapping per record. |  [optional] |



