# FrankieFinancialApi.OrganisationCheckResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityCategories** | **{String: [String]}** | A map of the entity categories that were selected for checks and an array of the entity IDs for each. The results for each entity ID will be in either the entityCheckResults or entityCheckErrors maps. Entities may appear in more than one category.  | [optional] 
**entityCheckErrors** | [**{String: ErrorObject}**](ErrorObject.md) | A map of outright errors (failure to generate any kind of result). These objects will be referenced by entity ID in the entity category map.  | [optional] 
**entityCheckResults** | [**{String: CheckEntityCheckResultObject}**](CheckEntityCheckResultObject.md) | List of all entities check results (both individuals and organisations) other than outright errors. These objects will be referenced by entity ID in the entity category map.  | [optional] 
**entityId** | **String** | The entityId of the organisation for which this result was created.  | [optional] 
**groupId** | **String** | The unique ID for grouping all new KYC/AML checks in this result. This is only for Frankie internal use.  | [optional] 


