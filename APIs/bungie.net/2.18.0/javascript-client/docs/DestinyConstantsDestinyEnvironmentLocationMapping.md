# BungieNetApi.DestinyConstantsDestinyEnvironmentLocationMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationSource** | **String** | A hint that the UI uses to figure out how this location is activated by the player. | [optional] 
**activityHash** | **Number** | If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don&#39;t) | [optional] 
**itemHash** | **Number** | If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don&#39;t) | [optional] 
**locationHash** | **Number** | The location that is revealed on the director by this mapping. | [optional] 
**objectiveHash** | **Number** | If this is populated, this is an objective related to the location. | [optional] 


