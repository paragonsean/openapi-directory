

# GoogleAdsSearchads360V0CommonLocationGroupInfo

A radius around a list of locations specified through a feed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feedItemSets** | **List&lt;String&gt;** | FeedItemSets whose FeedItems are targeted. If multiple IDs are specified, then all items that appear in at least one set are targeted. This field cannot be used with geo_target_constants. This is optional and can only be set in CREATE operations. |  [optional] |
|**geoTargetConstants** | **List&lt;String&gt;** | Geo target constant(s) restricting the scope of the geographic area within the feed. Currently only one geo target constant is allowed. |  [optional] |
|**radius** | **String** | Distance in units specifying the radius around targeted locations. This is required and must be set in CREATE operations. |  [optional] |
|**radiusUnits** | [**RadiusUnitsEnum**](#RadiusUnitsEnum) | Unit of the radius. Miles and meters are supported for geo target constants. Milli miles and meters are supported for feed item sets. This is required and must be set in CREATE operations. |  [optional] |



## Enum: RadiusUnitsEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| METERS | &quot;METERS&quot; |
| MILES | &quot;MILES&quot; |
| MILLI_MILES | &quot;MILLI_MILES&quot; |



