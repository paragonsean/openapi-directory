

# GeoRegionTargetingOptionDetails

Represents a targetable geographic region. This will be populated in the geo_region_details field when targeting_type is `TARGETING_TYPE_GEO_REGION`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of the geographic region (e.g., \&quot;Ontario, Canada\&quot;). |  [optional] [readonly] |
|**geoRegionType** | [**GeoRegionTypeEnum**](#GeoRegionTypeEnum) | Output only. The type of geographic region targeting. |  [optional] [readonly] |



## Enum: GeoRegionTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;GEO_REGION_TYPE_UNKNOWN&quot; |
| OTHER | &quot;GEO_REGION_TYPE_OTHER&quot; |
| COUNTRY | &quot;GEO_REGION_TYPE_COUNTRY&quot; |
| REGION | &quot;GEO_REGION_TYPE_REGION&quot; |
| TERRITORY | &quot;GEO_REGION_TYPE_TERRITORY&quot; |
| PROVINCE | &quot;GEO_REGION_TYPE_PROVINCE&quot; |
| STATE | &quot;GEO_REGION_TYPE_STATE&quot; |
| PREFECTURE | &quot;GEO_REGION_TYPE_PREFECTURE&quot; |
| GOVERNORATE | &quot;GEO_REGION_TYPE_GOVERNORATE&quot; |
| CANTON | &quot;GEO_REGION_TYPE_CANTON&quot; |
| UNION_TERRITORY | &quot;GEO_REGION_TYPE_UNION_TERRITORY&quot; |
| AUTONOMOUS_COMMUNITY | &quot;GEO_REGION_TYPE_AUTONOMOUS_COMMUNITY&quot; |
| DMA_REGION | &quot;GEO_REGION_TYPE_DMA_REGION&quot; |
| METRO | &quot;GEO_REGION_TYPE_METRO&quot; |
| CONGRESSIONAL_DISTRICT | &quot;GEO_REGION_TYPE_CONGRESSIONAL_DISTRICT&quot; |
| COUNTY | &quot;GEO_REGION_TYPE_COUNTY&quot; |
| MUNICIPALITY | &quot;GEO_REGION_TYPE_MUNICIPALITY&quot; |
| CITY | &quot;GEO_REGION_TYPE_CITY&quot; |
| POSTAL_CODE | &quot;GEO_REGION_TYPE_POSTAL_CODE&quot; |
| DEPARTMENT | &quot;GEO_REGION_TYPE_DEPARTMENT&quot; |
| AIRPORT | &quot;GEO_REGION_TYPE_AIRPORT&quot; |
| TV_REGION | &quot;GEO_REGION_TYPE_TV_REGION&quot; |
| OKRUG | &quot;GEO_REGION_TYPE_OKRUG&quot; |
| BOROUGH | &quot;GEO_REGION_TYPE_BOROUGH&quot; |
| CITY_REGION | &quot;GEO_REGION_TYPE_CITY_REGION&quot; |
| ARRONDISSEMENT | &quot;GEO_REGION_TYPE_ARRONDISSEMENT&quot; |
| NEIGHBORHOOD | &quot;GEO_REGION_TYPE_NEIGHBORHOOD&quot; |
| UNIVERSITY | &quot;GEO_REGION_TYPE_UNIVERSITY&quot; |
| DISTRICT | &quot;GEO_REGION_TYPE_DISTRICT&quot; |



