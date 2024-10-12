# CampaignManager360Api.ListPopulationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floodlightActivityId** | **String** | Floodlight activity ID associated with this rule. This field can be left blank. | [optional] 
**floodlightActivityName** | **String** | Name of floodlight activity associated with this rule. This is a read-only, auto-generated field. | [optional] 
**listPopulationClauses** | [**[ListPopulationClause]**](ListPopulationClause.md) | Clauses that make up this list population rule. Clauses are joined by ANDs, and the clauses themselves are made up of list population terms which are joined by ORs. | [optional] 


