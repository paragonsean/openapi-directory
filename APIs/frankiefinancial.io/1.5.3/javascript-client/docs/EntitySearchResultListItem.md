# FrankieFinancialApi.EntitySearchResultListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | [**SearchResultConfidenceObject**](SearchResultConfidenceObject.md) |  | [optional] 
**documentMatchTypes** | **[String]** | Array of descriptons of document field matches used to score this search. This is a summary for all the documents for the matched entity.  | [optional] 
**documentNameMismatches** | **[String]** | If this entity has any level of name match then this is an array of document IDs for the entity where the document has an entity name and it doesn&#39;t match any entity names being sought.  | [optional] 
**entity** | [**EntityObject**](EntityObject.md) |  | [optional] 
**entityMatchTypes** | **[String]** | Array of descriptons of entity field matches used to score this search.  | [optional] 


