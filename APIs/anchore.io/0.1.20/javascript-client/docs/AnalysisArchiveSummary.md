# AnchoreEngineApiServer.AnalysisArchiveSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastUpdated** | **Date** | The timestamp of the most recent archived image | [optional] 
**totalDataBytes** | **Number** | The total sum of all the bytes stored to the backing storage. Accounts for anchore-applied compression, but not compression by the underlying storage system. | [optional] 
**totalImageCount** | **Number** | The number of unique images (digests) in the archive | [optional] 
**totalTagCount** | **Number** | The number of tag records (registry/repo:tag pull strings) in the archive. This may include repeated tags but will always have a unique tag-&gt;digest mapping per record. | [optional] 


