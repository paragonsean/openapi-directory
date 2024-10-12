

# GoogleCloudRetailV2alphaCondition

Metadata that is used to define a condition that triggers an action. A valid condition must specify at least one of 'query_terms' or 'products_filter'. If multiple fields are specified, the condition is met if all the fields are satisfied e.g. if a set of query terms and product_filter are set, then only items matching the product_filter for requests with a query matching the query terms wil get boosted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeTimeRange** | [**List&lt;GoogleCloudRetailV2alphaConditionTimeRange&gt;**](GoogleCloudRetailV2alphaConditionTimeRange.md) | Range of time(s) specifying when Condition is active. Condition true if any time range matches. |  [optional] |
|**pageCategories** | **List&lt;String&gt;** | Used to support browse uses cases. A list (up to 10 entries) of categories or departments. The format should be the same as UserEvent.page_categories; |  [optional] |
|**queryTerms** | [**List&lt;GoogleCloudRetailV2alphaConditionQueryTerm&gt;**](GoogleCloudRetailV2alphaConditionQueryTerm.md) | A list (up to 10 entries) of terms to match the query on. If not specified, match all queries. If many query terms are specified, the condition is matched if any of the terms is a match (i.e. using the OR operator). |  [optional] |



