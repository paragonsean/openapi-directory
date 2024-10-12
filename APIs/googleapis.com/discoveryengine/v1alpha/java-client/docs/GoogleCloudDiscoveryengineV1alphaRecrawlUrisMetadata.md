

# GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata

Metadata related to the progress of the SiteSearchEngineService.RecrawlUris operation. This will be returned by the google.longrunning.Operation.metadata field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Operation create time. |  [optional] |
|**invalidUris** | **List&lt;String&gt;** | Unique URIs in the request that don&#39;t match any TargetSite in the DataStore, only match TargetSites that haven&#39;t been fully indexed, or match a TargetSite with type EXCLUDE. |  [optional] |
|**pendingCount** | **Integer** | Total number of URIs that have yet to be crawled. |  [optional] |
|**quotaExceededCount** | **Integer** | Total number of URIs that were rejected due to insufficient indexing resources. |  [optional] |
|**successCount** | **Integer** | Total number of URIs that have been crawled so far. |  [optional] |
|**updateTime** | **String** | Operation last update time. If the operation is done, this is also the finish time. |  [optional] |
|**validUrisCount** | **Integer** | Total number of unique URIs in the request that are not in invalid_uris. |  [optional] |



