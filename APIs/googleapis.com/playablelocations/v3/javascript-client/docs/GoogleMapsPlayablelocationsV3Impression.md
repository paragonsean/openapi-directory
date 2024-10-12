# PlayableLocationsApi.GoogleMapsPlayablelocationsV3Impression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gameObjectType** | **Number** | An arbitrary, developer-defined type identifier for each type of game object used in your game. Since players interact with differ types of game objects in different ways, this field allows you to segregate impression data by type for analysis. You should assign a unique &#x60;game_object_type&#x60; ID to represent a distinct type of game object in your game. For example, 1&#x3D;monster location, 2&#x3D;powerup location. | [optional] 
**impressionType** | **String** | Required. The type of impression event. | [optional] 
**locationName** | **String** | Required. The name of the playable location. | [optional] 



## Enum: ImpressionTypeEnum


* `IMPRESSION_TYPE_UNSPECIFIED` (value: `"IMPRESSION_TYPE_UNSPECIFIED"`)

* `PRESENTED` (value: `"PRESENTED"`)

* `INTERACTED` (value: `"INTERACTED"`)




