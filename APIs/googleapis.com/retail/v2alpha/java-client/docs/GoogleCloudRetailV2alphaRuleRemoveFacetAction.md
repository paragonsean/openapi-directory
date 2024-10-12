

# GoogleCloudRetailV2alphaRuleRemoveFacetAction

Removes an attribute/facet in the request if is present. * Rule Condition: Must specify non-empty Condition.query_terms (for search only) or Condition.page_categories (for browse only), but can't specify both. * Action Input: attribute name * Action Result: Will remove the attribute (as a facet) from the request if it is present. Example: Suppose the query is \"shoes\", the Condition.query_terms is \"shoes\" and the attribute name \"size\", then facet key \"size\" will be removed from the request (if it is present).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeNames** | **List&lt;String&gt;** | The attribute names (i.e. facet keys) to remove from the dynamic facets (if present in the request). There can&#39;t be more 3 attribute names. Each attribute name should be a valid attribute name, be non-empty and contain at most 80 characters. |  [optional] |



