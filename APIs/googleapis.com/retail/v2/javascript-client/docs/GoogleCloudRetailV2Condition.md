# VertexAiSearchForRetailApi.GoogleCloudRetailV2Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeTimeRange** | [**[GoogleCloudRetailV2ConditionTimeRange]**](GoogleCloudRetailV2ConditionTimeRange.md) | Range of time(s) specifying when Condition is active. Condition true if any time range matches. | [optional] 
**pageCategories** | **[String]** | Used to support browse uses cases. A list (up to 10 entries) of categories or departments. The format should be the same as UserEvent.page_categories; | [optional] 
**queryTerms** | [**[GoogleCloudRetailV2ConditionQueryTerm]**](GoogleCloudRetailV2ConditionQueryTerm.md) | A list (up to 10 entries) of terms to match the query on. If not specified, match all queries. If many query terms are specified, the condition is matched if any of the terms is a match (i.e. using the OR operator). | [optional] 


