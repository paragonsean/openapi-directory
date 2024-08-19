# Nookipedia.NHFishNorth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityArray** | [**[NHBugNorthAvailabilityArrayInner]**](NHBugNorthAvailabilityArrayInner.md) | An array of objects, each object holding a months string and the time the critter is availabile during the specified month(s) in the northern hemisphere. Most critters will have just one object. A small number of critters have variable time availability in which case this array will have multiple objects. | [optional] 
**months** | **String** | The months the fish is available for in the Northern hemisphere. If all year, value will be &#x60;\&quot;All year\&quot;&#x60;. | [optional] 
**monthsArray** | **[Number]** | An array of integers representing the months the fish is available in the Northern hemisphere. | [optional] 
**timesByMonth** | [**NHFishNorthTimesByMonth**](NHFishNorthTimesByMonth.md) |  | [optional] 


