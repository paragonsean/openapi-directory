

# GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo

Details about why a particular URI failed to be crawled. Each FailureInfo contains one FailureReason per CorpusType.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureReasons** | [**List&lt;GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason&gt;**](GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason.md) | List of failure reasons by corpus type (e.g. desktop, mobile). |  [optional] |
|**uri** | **String** | URI that failed to be crawled. |  [optional] |



