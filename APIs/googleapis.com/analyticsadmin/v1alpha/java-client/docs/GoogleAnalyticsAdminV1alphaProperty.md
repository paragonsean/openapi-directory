

# GoogleAnalyticsAdminV1alphaProperty

A resource message representing a Google Analytics GA4 property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | Immutable. The resource name of the parent account Format: accounts/{account_id} Example: \&quot;accounts/123\&quot; |  [optional] |
|**createTime** | **String** | Output only. Time when the entity was originally created. |  [optional] [readonly] |
|**currencyCode** | **String** | The currency type used in reports involving monetary values. Format: https://en.wikipedia.org/wiki/ISO_4217 Examples: \&quot;USD\&quot;, \&quot;EUR\&quot;, \&quot;JPY\&quot; |  [optional] |
|**deleteTime** | **String** | Output only. If set, the time at which this property was trashed. If not set, then this property is not currently in the trash can. |  [optional] [readonly] |
|**displayName** | **String** | Required. Human-readable display name for this property. The max allowed display name length is 100 UTF-16 code units. |  [optional] |
|**expireTime** | **String** | Output only. If set, the time at which this trashed property will be permanently deleted. If not set, then this property is not currently in the trash can and is not slated to be deleted. |  [optional] [readonly] |
|**industryCategory** | [**IndustryCategoryEnum**](#IndustryCategoryEnum) | Industry associated with this property Example: AUTOMOTIVE, FOOD_AND_DRINK |  [optional] |
|**name** | **String** | Output only. Resource name of this property. Format: properties/{property_id} Example: \&quot;properties/1000\&quot; |  [optional] [readonly] |
|**parent** | **String** | Immutable. Resource name of this property&#39;s logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/{account}, properties/{property} Example: \&quot;accounts/100\&quot;, \&quot;properties/101\&quot; |  [optional] |
|**propertyType** | [**PropertyTypeEnum**](#PropertyTypeEnum) | Immutable. The property type for this Property resource. When creating a property, if the type is \&quot;PROPERTY_TYPE_UNSPECIFIED\&quot;, then \&quot;ORDINARY_PROPERTY\&quot; will be implied. |  [optional] |
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | Output only. The Google Analytics service level that applies to this property. |  [optional] [readonly] |
|**timeZone** | **String** | Required. Reporting Time Zone, used as the day boundary for reports, regardless of where the data originates. If the time zone honors DST, Analytics will automatically adjust for the changes. NOTE: Changing the time zone only affects data going forward, and is not applied retroactively. Format: https://www.iana.org/time-zones Example: \&quot;America/Los_Angeles\&quot; |  [optional] |
|**updateTime** | **String** | Output only. Time when entity payload fields were last updated. |  [optional] [readonly] |



## Enum: IndustryCategoryEnum

| Name | Value |
|---- | -----|
| INDUSTRY_CATEGORY_UNSPECIFIED | &quot;INDUSTRY_CATEGORY_UNSPECIFIED&quot; |
| AUTOMOTIVE | &quot;AUTOMOTIVE&quot; |
| BUSINESS_AND_INDUSTRIAL_MARKETS | &quot;BUSINESS_AND_INDUSTRIAL_MARKETS&quot; |
| FINANCE | &quot;FINANCE&quot; |
| HEALTHCARE | &quot;HEALTHCARE&quot; |
| TECHNOLOGY | &quot;TECHNOLOGY&quot; |
| TRAVEL | &quot;TRAVEL&quot; |
| OTHER | &quot;OTHER&quot; |
| ARTS_AND_ENTERTAINMENT | &quot;ARTS_AND_ENTERTAINMENT&quot; |
| BEAUTY_AND_FITNESS | &quot;BEAUTY_AND_FITNESS&quot; |
| BOOKS_AND_LITERATURE | &quot;BOOKS_AND_LITERATURE&quot; |
| FOOD_AND_DRINK | &quot;FOOD_AND_DRINK&quot; |
| GAMES | &quot;GAMES&quot; |
| HOBBIES_AND_LEISURE | &quot;HOBBIES_AND_LEISURE&quot; |
| HOME_AND_GARDEN | &quot;HOME_AND_GARDEN&quot; |
| INTERNET_AND_TELECOM | &quot;INTERNET_AND_TELECOM&quot; |
| LAW_AND_GOVERNMENT | &quot;LAW_AND_GOVERNMENT&quot; |
| NEWS | &quot;NEWS&quot; |
| ONLINE_COMMUNITIES | &quot;ONLINE_COMMUNITIES&quot; |
| PEOPLE_AND_SOCIETY | &quot;PEOPLE_AND_SOCIETY&quot; |
| PETS_AND_ANIMALS | &quot;PETS_AND_ANIMALS&quot; |
| REAL_ESTATE | &quot;REAL_ESTATE&quot; |
| REFERENCE | &quot;REFERENCE&quot; |
| SCIENCE | &quot;SCIENCE&quot; |
| SPORTS | &quot;SPORTS&quot; |
| JOBS_AND_EDUCATION | &quot;JOBS_AND_EDUCATION&quot; |
| SHOPPING | &quot;SHOPPING&quot; |



## Enum: PropertyTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROPERTY_TYPE_UNSPECIFIED&quot; |
| ORDINARY | &quot;PROPERTY_TYPE_ORDINARY&quot; |
| SUBPROPERTY | &quot;PROPERTY_TYPE_SUBPROPERTY&quot; |
| ROLLUP | &quot;PROPERTY_TYPE_ROLLUP&quot; |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| SERVICE_LEVEL_UNSPECIFIED | &quot;SERVICE_LEVEL_UNSPECIFIED&quot; |
| GOOGLE_ANALYTICS_STANDARD | &quot;GOOGLE_ANALYTICS_STANDARD&quot; |
| GOOGLE_ANALYTICS_360 | &quot;GOOGLE_ANALYTICS_360&quot; |



