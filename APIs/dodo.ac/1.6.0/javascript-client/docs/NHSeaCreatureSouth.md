# Nookipedia.NHSeaCreatureSouth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityArray** | [**[NHBugNorthAvailabilityArrayInner]**](NHBugNorthAvailabilityArrayInner.md) | An array of objects, each object holding a months string and the time the critter is availabile during the specified month(s) in the southern hemisphere. Most critters will have just one object. A small number of critters have variable time availability in which case this array will have multiple objects. | [optional] 
**months** | **String** | The months the sea creature is available for in the Southern hemisphere. If all year, value will be &#x60;\&quot;All year\&quot;&#x60;. | [optional] 
**monthsArray** | **[Number]** | An array of integers representing the months the sea creature is available in the Southern hemisphere. | [optional] 
**timesByMonth** | [**NHSeaCreatureNorthTimesByMonth**](NHSeaCreatureNorthTimesByMonth.md) |  | [optional] 


