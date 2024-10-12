# BungieNetApi.DestinyEntitiesItemsDestinyItemInstanceEnergy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energyCapacity** | **Number** | The total capacity of Energy that the item currently has, regardless of if it is currently being used. | [optional] 
**energyType** | **Number** | This is the enum version of the Energy Type value, for convenience. | [optional] 
**energyTypeHash** | **Number** | The type of energy for this item. Plugs that require Energy can only be inserted if they have the \&quot;Any\&quot; Energy Type or the matching energy type of this item. This is a reference to the DestinyEnergyTypeDefinition for the energy type, where you can find extended info about it. | [optional] 
**energyUnused** | **Number** | The amount of energy still available for inserting new plugs. | [optional] 
**energyUsed** | **Number** | The amount of Energy currently in use by inserted plugs. | [optional] 


