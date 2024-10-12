# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1SystemTimestamps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Creation timestamp of the resource within the given system. | [optional] 
**expireTime** | **String** | Output only. Expiration timestamp of the resource within the given system. Currently only applicable to BigQuery resources. | [optional] [readonly] 
**updateTime** | **String** | Timestamp of the last modification of the resource or its metadata within a given system. Note: Depending on the source system, not every modification updates this timestamp. For example, BigQuery timestamps every metadata modification but not data or permission changes. | [optional] 


