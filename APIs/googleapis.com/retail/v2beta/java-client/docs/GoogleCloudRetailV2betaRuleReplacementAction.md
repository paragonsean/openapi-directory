

# GoogleCloudRetailV2betaRuleReplacementAction

Replaces a term in the query. Multiple replacement candidates can be specified. All `query_terms` will be replaced with the replacement term. Example: Replace \"gShoe\" with \"google shoe\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queryTerms** | **List&lt;String&gt;** | Terms from the search query. Will be replaced by replacement term. Can specify up to 100 terms. |  [optional] |
|**replacementTerm** | **String** | Term that will be used for replacement. |  [optional] |
|**term** | **String** | Will be [deprecated &#x3D; true] post migration; |  [optional] |



