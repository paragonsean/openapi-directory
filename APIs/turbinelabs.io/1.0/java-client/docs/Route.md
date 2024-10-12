

# Route


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** |  |  |
|**cohortSeed** | [**CohortSeed**](CohortSeed.md) |  |  [optional] |
|**domainKey** | **String** |  |  |
|**path** | **String** |  |  |
|**responseData** | [**ResponseData**](ResponseData.md) | When a request is served by this Route annotate the response with the information specified within this ResponseData object. It&#39;s possible that multiple response data configurations will apply; if that&#39;s the case then the values from Route take precedence over those from a SharedRules object.  |  [optional] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |
|**routeKey** | **String** |  |  |
|**rules** | [**List&lt;Rule&gt;**](Rule.md) |  |  [optional] |
|**sharedRulesKey** | **String** |  |  |
|**zoneKey** | **String** |  |  |



