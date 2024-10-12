

# GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse

Response message for SiteSearchEngineService.FetchDomainVerificationStatus method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token that can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**targetSites** | [**List&lt;GoogleCloudDiscoveryengineV1alphaTargetSite&gt;**](GoogleCloudDiscoveryengineV1alphaTargetSite.md) | List of TargetSites containing the site verification status. |  [optional] |
|**totalSize** | **Integer** | The total number of items matching the request. This will always be populated in the response. |  [optional] |



