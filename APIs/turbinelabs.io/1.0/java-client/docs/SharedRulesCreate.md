

# SharedRulesCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** |  |  [optional] |
|**cohortSeed** | [**CohortSeed**](CohortSeed.md) |  |  [optional] |
|**_default** | [**AllConstraints**](AllConstraints.md) |  |  |
|**properties** | [**List&lt;Metadatum&gt;**](Metadatum.md) |  |  [optional] |
|**responseData** | [**ResponseData**](ResponseData.md) | When a request is served by a Route that is part of this SharedRules group the response is annotated with the information specified within this ResponseData object. It&#39;s possible that multiple response data configurations will apply; if that&#39;s the case then the values from the applicable Route and ClusterConstarint takes precedence over those specified here.  |  [optional] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |
|**rules** | [**List&lt;Rule&gt;**](Rule.md) |  |  [optional] |
|**sharedRulesKey** | **String** |  |  [optional] |
|**zoneKey** | **String** |  |  |



