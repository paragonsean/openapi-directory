# BungieNetApi.DestinyDefinitionsDestinyItemSourceBlockDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusive** | **Number** | If we found that this item is exclusive to a specific platform, this will be set to the BungieMembershipType enumeration that matches that platform. | [optional] 
**sourceHashes** | **[Number]** | The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition). | [optional] 
**sources** | [**[DestinyDefinitionsSourcesDestinyItemSourceDefinition]**](DestinyDefinitionsSourcesDestinyItemSourceDefinition.md) | A collection of details about the stats that were computed for the ways we found that the item could be spawned. | [optional] 
**vendorSources** | [**[DestinyDefinitionsDestinyItemVendorSourceReference]**](DestinyDefinitionsDestinyItemVendorSourceReference.md) | A denormalized reference back to vendors that potentially sell this item. | [optional] 


