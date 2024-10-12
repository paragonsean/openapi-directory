

# GoogleCloudRetailV2RuleDoNotAssociateAction

Prevents `query_term` from being associated with specified terms during search. Example: Don't associate \"gShoe\" and \"cheap\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doNotAssociateTerms** | **List&lt;String&gt;** | Cannot contain duplicates or the query term. Can specify up to 100 terms. |  [optional] |
|**queryTerms** | **List&lt;String&gt;** | Terms from the search query. Will not consider do_not_associate_terms for search if in search query. Can specify up to 100 terms. |  [optional] |
|**terms** | **List&lt;String&gt;** | Will be [deprecated &#x3D; true] post migration; |  [optional] |



