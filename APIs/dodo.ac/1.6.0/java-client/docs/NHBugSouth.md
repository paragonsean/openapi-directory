

# NHBugSouth

When you can catch the bug in the Southern hemisphere.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityArray** | [**List&lt;NHBugNorthAvailabilityArrayInner&gt;**](NHBugNorthAvailabilityArrayInner.md) | An array of objects, each object holding a months string and the time the critter is availabile during the specified month(s) in the southern hemisphere. Most critters will have just one object. A small number of critters have variable time availability in which case this array will have multiple objects. |  [optional] |
|**months** | **String** | The months the bug is available for in the Southern hemisphere. If all year, value will be &#x60;\&quot;All year\&quot;&#x60;. |  [optional] |
|**monthsArray** | **List&lt;Integer&gt;** | An array of integers representing the months the bug is available in the Southern hemisphere. |  [optional] |
|**timesByMonth** | [**NHBugSouthTimesByMonth**](NHBugSouthTimesByMonth.md) |  |  [optional] |



