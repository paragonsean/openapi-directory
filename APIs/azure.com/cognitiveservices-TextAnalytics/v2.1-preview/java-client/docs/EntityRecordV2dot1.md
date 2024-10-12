

# EntityRecordV2dot1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bingId** | **String** | Bing unique identifier of the recognized entity. Use in conjunction with the Bing Entity Search API to fetch additional relevant information. |  [optional] |
|**matches** | [**List&lt;MatchRecordV2dot1&gt;**](MatchRecordV2dot1.md) | List of instances this entity appears in the text. |  [optional] |
|**name** | **String** | Entity formal name. |  [optional] |
|**subType** | **String** | Entity sub type from Named Entity Recognition model |  [optional] |
|**type** | **String** | Entity type from Named Entity Recognition model |  [optional] |
|**wikipediaId** | **String** | Wikipedia unique identifier of the recognized entity. |  [optional] |
|**wikipediaLanguage** | **String** | Wikipedia language for which the WikipediaId and WikipediaUrl refers to. |  [optional] |
|**wikipediaUrl** | **String** | URL for the entity&#39;s English Wikipedia page. |  [optional] [readonly] |



