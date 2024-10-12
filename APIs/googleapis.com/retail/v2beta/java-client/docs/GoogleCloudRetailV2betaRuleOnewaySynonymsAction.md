

# GoogleCloudRetailV2betaRuleOnewaySynonymsAction

Maps a set of terms to a set of synonyms. Set of synonyms will be treated as synonyms of each query term only. `query_terms` will not be treated as synonyms of each other. Example: \"sneakers\" will use a synonym of \"shoes\". \"shoes\" will not use a synonym of \"sneakers\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**onewayTerms** | **List&lt;String&gt;** | Will be [deprecated &#x3D; true] post migration; |  [optional] |
|**queryTerms** | **List&lt;String&gt;** | Terms from the search query. Will treat synonyms as their synonyms. Not themselves synonyms of the synonyms. Can specify up to 100 terms. |  [optional] |
|**synonyms** | **List&lt;String&gt;** | Defines a set of synonyms. Cannot contain duplicates. Can specify up to 100 synonyms. |  [optional] |



