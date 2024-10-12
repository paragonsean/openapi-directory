

# LocationFilter

Input only. Geographic region of the search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Optional. The address name, such as \&quot;Mountain View\&quot; or \&quot;Bay Area\&quot;. |  [optional] |
|**distanceInMiles** | **Double** | Optional. The distance_in_miles is applied when the location being searched for is identified as a city or smaller. When the location being searched for is a state or larger, this field is ignored. |  [optional] |
|**latLng** | [**LatLng**](LatLng.md) |  |  [optional] |
|**regionCode** | **String** | Optional. CLDR region code of the country/region. This field may be used in two ways: 1) If telecommute preference is not set, this field is used address ambiguity of the user-input address. For example, \&quot;Liverpool\&quot; may refer to \&quot;Liverpool, NY, US\&quot; or \&quot;Liverpool, UK\&quot;. This region code biases the address resolution toward a specific country or territory. If this field is not set, address resolution is biased toward the United States by default. 2) If telecommute preference is set to TELECOMMUTE_ALLOWED, the telecommute location filter will be limited to the region specified in this field. If this field is not set, the telecommute job locations will not be limited. See https://unicode-org.github.io/cldr-staging/charts/latest/supplemental/territory_information.html for details. Example: \&quot;CH\&quot; for Switzerland. |  [optional] |
|**telecommutePreference** | [**TelecommutePreferenceEnum**](#TelecommutePreferenceEnum) | Optional. Allows the client to return jobs without a set location, specifically, telecommuting jobs (telecommuting is considered by the service as a special location). Job.posting_region indicates if a job permits telecommuting. If this field is set to TelecommutePreference.TELECOMMUTE_ALLOWED, telecommuting jobs are searched, and address and lat_lng are ignored. If not set or set to TelecommutePreference.TELECOMMUTE_EXCLUDED, the telecommute status of the jobs is ignored. Jobs that have PostingRegion.TELECOMMUTE and have additional Job.addresses may still be matched based on other location filters using address or latlng. This filter can be used by itself to search exclusively for telecommuting jobs, or it can be combined with another location filter to search for a combination of job locations, such as \&quot;Mountain View\&quot; or \&quot;telecommuting\&quot; jobs. However, when used in combination with other location filters, telecommuting jobs can be treated as less relevant than other jobs in the search response. |  [optional] |



## Enum: TelecommutePreferenceEnum

| Name | Value |
|---- | -----|
| PREFERENCE_UNSPECIFIED | &quot;TELECOMMUTE_PREFERENCE_UNSPECIFIED&quot; |
| EXCLUDED | &quot;TELECOMMUTE_EXCLUDED&quot; |
| ALLOWED | &quot;TELECOMMUTE_ALLOWED&quot; |
| JOBS_EXCLUDED | &quot;TELECOMMUTE_JOBS_EXCLUDED&quot; |



