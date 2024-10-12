

# GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason

Details about why crawling failed for a particular CorpusType, e.g., DESKTOP and MOBILE crawling may fail for different reasons.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corpusType** | [**CorpusTypeEnum**](#CorpusTypeEnum) | DESKTOP, MOBILE, or CORPUS_TYPE_UNSPECIFIED. |  [optional] |
|**errorMessage** | **String** | Reason why the URI was not crawled. |  [optional] |



## Enum: CorpusTypeEnum

| Name | Value |
|---- | -----|
| CORPUS_TYPE_UNSPECIFIED | &quot;CORPUS_TYPE_UNSPECIFIED&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| MOBILE | &quot;MOBILE&quot; |



