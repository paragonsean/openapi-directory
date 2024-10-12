# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonLocationGroupInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedItemSets** | **[String]** | FeedItemSets whose FeedItems are targeted. If multiple IDs are specified, then all items that appear in at least one set are targeted. This field cannot be used with geo_target_constants. This is optional and can only be set in CREATE operations. | [optional] 
**geoTargetConstants** | **[String]** | Geo target constant(s) restricting the scope of the geographic area within the feed. Currently only one geo target constant is allowed. | [optional] 
**radius** | **String** | Distance in units specifying the radius around targeted locations. This is required and must be set in CREATE operations. | [optional] 
**radiusUnits** | **String** | Unit of the radius. Miles and meters are supported for geo target constants. Milli miles and meters are supported for feed item sets. This is required and must be set in CREATE operations. | [optional] 



## Enum: RadiusUnitsEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `METERS` (value: `"METERS"`)

* `MILES` (value: `"MILES"`)

* `MILLI_MILES` (value: `"MILLI_MILES"`)




