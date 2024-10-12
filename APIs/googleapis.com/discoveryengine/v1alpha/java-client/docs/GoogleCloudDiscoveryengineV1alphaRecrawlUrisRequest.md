

# GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest

Request message for SiteSearchEngineService.RecrawlUris method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uris** | **List&lt;String&gt;** | Required. List of URIs to crawl. At most 10K URIs are supported, otherwise an INVALID_ARGUMENT error is thrown. Each URI should match at least one TargetSite in &#x60;site_search_engine&#x60;. |  [optional] |



