# FrankieFinancialApi.OwnershipQueryResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatedEntities** | [**{String: EntityObject}**](EntityObject.md) | List of all entities (both individuals and organisations) associated with this ownership result. These objects will be referenced by entityId in the shareholdings and officers lists in the following ownership details.  | [optional] 
**blockingEntityIds** | **[String]** | List of entity IDs (that should be in the associatedEntities list) who blocked the ultimate beneficial ownership tree traversal. These are likely to be entities that cannot be checked automatically (such as trusts) or who have no UBO&#39;s of their own, such as public companies.  The presence of data in this array also signifies that the full UBO list is not complete.  | [optional] 
**entityId** | **String** | The entityId of the organisation for which this result was created. The details will be in the ownershipDetails map with this ID as the key.  | [optional] 
**ownershipDetails** | [**{String: OwnershipDetailsObject}**](OwnershipDetailsObject.md) | A map of entityId to ownershipDetailsObjects with at least one entry being for the root organisation that the overall result relates to. Any remaining entries will be for further results for organisational owners referenced in the root ownershipDetailsObject and so on.  | [optional] 


