# TransportForLondonUnifiedApi.TflApiPresentationEntitiesStopPoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibilitySummary** | **String** |  | [optional] 
**additionalProperties** | [**[TflApiPresentationEntitiesAdditionalProperties]**](TflApiPresentationEntitiesAdditionalProperties.md) | A bag of additional key/value pairs with extra information about this place. | [optional] 
**children** | [**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md) |  | [optional] 
**childrenUrls** | **[String]** |  | [optional] 
**commonName** | **String** | A human readable name. | [optional] 
**distance** | **Number** | The distance of the place from its search point, if this is the result              of a geographical search, otherwise zero. | [optional] 
**fullName** | **String** |  | [optional] 
**hubNaptanCode** | **String** |  | [optional] 
**icsCode** | **String** |  | [optional] 
**id** | **String** | A unique identifier. | [optional] 
**indicator** | **String** | The indicator of the stop point e.g. \&quot;Stop K\&quot; | [optional] 
**individualStopId** | **String** |  | [optional] 
**lat** | **Number** | WGS84 latitude of the location. | [optional] 
**lineGroup** | [**[TflApiPresentationEntitiesLineGroup]**](TflApiPresentationEntitiesLineGroup.md) |  | [optional] 
**lineModeGroups** | [**[TflApiPresentationEntitiesLineModeGroup]**](TflApiPresentationEntitiesLineModeGroup.md) |  | [optional] 
**lines** | [**[TflApiPresentationEntitiesIdentifier]**](TflApiPresentationEntitiesIdentifier.md) |  | [optional] 
**lon** | **Number** | WGS84 longitude of the location. | [optional] 
**modes** | **[String]** |  | [optional] 
**naptanId** | **String** |  | [optional] 
**naptanMode** | **String** |  | [optional] 
**placeType** | **String** | The type of Place. See /Place/Meta/placeTypes for possible values. | [optional] 
**platformName** | **String** |  | [optional] 
**smsCode** | **String** |  | [optional] 
**stationNaptan** | **String** |  | [optional] 
**status** | **Boolean** |  | [optional] 
**stopLetter** | **String** | The stop letter, if it could be cleansed from the Indicator e.g. \&quot;K\&quot; | [optional] 
**stopType** | **String** |  | [optional] 
**url** | **String** | The unique location of this resource. | [optional] 


