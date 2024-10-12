

# EntitySearchResultListItem

Contains the individual search results for an entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | [**SearchResultConfidenceObject**](SearchResultConfidenceObject.md) |  |  [optional] |
|**documentMatchTypes** | **List&lt;String&gt;** | Array of descriptons of document field matches used to score this search. This is a summary for all the documents for the matched entity.  |  [optional] |
|**documentNameMismatches** | **List&lt;UUID&gt;** | If this entity has any level of name match then this is an array of document IDs for the entity where the document has an entity name and it doesn&#39;t match any entity names being sought.  |  [optional] |
|**entity** | [**EntityObject**](EntityObject.md) |  |  [optional] |
|**entityMatchTypes** | **List&lt;String&gt;** | Array of descriptons of entity field matches used to score this search.  |  [optional] |



