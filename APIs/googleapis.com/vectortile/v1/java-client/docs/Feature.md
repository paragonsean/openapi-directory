

# Feature

A feature representing a single geographic entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The localized name of this feature. Currently only returned for roads. |  [optional] |
|**geometry** | [**Geometry**](Geometry.md) |  |  [optional] |
|**placeId** | **String** | Place ID of this feature, suitable for use in Places API details requests. |  [optional] |
|**relations** | [**List&lt;Relation&gt;**](Relation.md) | Relations to other features. |  [optional] |
|**segmentInfo** | [**SegmentInfo**](SegmentInfo.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this feature. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FEATURE_TYPE_UNSPECIFIED | &quot;FEATURE_TYPE_UNSPECIFIED&quot; |
| STRUCTURE | &quot;STRUCTURE&quot; |
| BAR | &quot;BAR&quot; |
| BANK | &quot;BANK&quot; |
| LODGING | &quot;LODGING&quot; |
| CAFE | &quot;CAFE&quot; |
| RESTAURANT | &quot;RESTAURANT&quot; |
| EVENT_VENUE | &quot;EVENT_VENUE&quot; |
| TOURIST_DESTINATION | &quot;TOURIST_DESTINATION&quot; |
| SHOPPING | &quot;SHOPPING&quot; |
| SCHOOL | &quot;SCHOOL&quot; |
| SEGMENT | &quot;SEGMENT&quot; |
| ROAD | &quot;ROAD&quot; |
| LOCAL_ROAD | &quot;LOCAL_ROAD&quot; |
| ARTERIAL_ROAD | &quot;ARTERIAL_ROAD&quot; |
| HIGHWAY | &quot;HIGHWAY&quot; |
| CONTROLLED_ACCESS_HIGHWAY | &quot;CONTROLLED_ACCESS_HIGHWAY&quot; |
| FOOTPATH | &quot;FOOTPATH&quot; |
| RAIL | &quot;RAIL&quot; |
| FERRY | &quot;FERRY&quot; |
| REGION | &quot;REGION&quot; |
| PARK | &quot;PARK&quot; |
| BEACH | &quot;BEACH&quot; |
| FOREST | &quot;FOREST&quot; |
| POLITICAL | &quot;POLITICAL&quot; |
| ADMINISTRATIVE_AREA1 | &quot;ADMINISTRATIVE_AREA1&quot; |
| LOCALITY | &quot;LOCALITY&quot; |
| SUBLOCALITY | &quot;SUBLOCALITY&quot; |
| WATER | &quot;WATER&quot; |



