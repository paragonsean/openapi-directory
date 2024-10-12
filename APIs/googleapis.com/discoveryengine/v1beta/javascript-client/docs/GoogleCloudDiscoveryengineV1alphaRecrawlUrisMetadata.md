# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Operation create time. | [optional] 
**invalidUris** | **[String]** | Unique URIs in the request that don&#39;t match any TargetSite in the DataStore, only match TargetSites that haven&#39;t been fully indexed, or match a TargetSite with type EXCLUDE. | [optional] 
**pendingCount** | **Number** | Total number of URIs that have yet to be crawled. | [optional] 
**quotaExceededCount** | **Number** | Total number of URIs that were rejected due to insufficient indexing resources. | [optional] 
**successCount** | **Number** | Total number of URIs that have been crawled so far. | [optional] 
**updateTime** | **String** | Operation last update time. If the operation is done, this is also the finish time. | [optional] 
**validUrisCount** | **Number** | Total number of unique URIs in the request that are not in invalid_uris. | [optional] 


