

# ElectoralDistrict

Describes the geographic scope of a contest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | An identifier for this district, relative to its scope. For example, the 34th State Senate district would have id \&quot;34\&quot; and a scope of stateUpper. |  [optional] |
|**name** | **String** | The name of the district. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The geographic scope of this district. If unspecified the district&#39;s geography is not known. One of: national, statewide, congressional, stateUpper, stateLower, countywide, judicial, schoolBoard, cityWide, township, countyCouncil, cityCouncil, ward, special |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| STATEWIDE | &quot;statewide&quot; |
| CONGRESSIONAL | &quot;congressional&quot; |
| STATE_UPPER | &quot;stateUpper&quot; |
| STATE_LOWER | &quot;stateLower&quot; |
| COUNTYWIDE | &quot;countywide&quot; |
| JUDICIAL | &quot;judicial&quot; |
| SCHOOL_BOARD | &quot;schoolBoard&quot; |
| CITYWIDE | &quot;citywide&quot; |
| SPECIAL | &quot;special&quot; |
| COUNTY_COUNCIL | &quot;countyCouncil&quot; |
| TOWNSHIP | &quot;township&quot; |
| WARD | &quot;ward&quot; |
| CITY_COUNCIL | &quot;cityCouncil&quot; |
| NATIONAL | &quot;national&quot; |



