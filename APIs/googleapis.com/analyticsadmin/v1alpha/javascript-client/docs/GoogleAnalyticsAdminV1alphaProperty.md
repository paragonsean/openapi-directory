# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Immutable. The resource name of the parent account Format: accounts/{account_id} Example: \&quot;accounts/123\&quot; | [optional] 
**createTime** | **String** | Output only. Time when the entity was originally created. | [optional] [readonly] 
**currencyCode** | **String** | The currency type used in reports involving monetary values. Format: https://en.wikipedia.org/wiki/ISO_4217 Examples: \&quot;USD\&quot;, \&quot;EUR\&quot;, \&quot;JPY\&quot; | [optional] 
**deleteTime** | **String** | Output only. If set, the time at which this property was trashed. If not set, then this property is not currently in the trash can. | [optional] [readonly] 
**displayName** | **String** | Required. Human-readable display name for this property. The max allowed display name length is 100 UTF-16 code units. | [optional] 
**expireTime** | **String** | Output only. If set, the time at which this trashed property will be permanently deleted. If not set, then this property is not currently in the trash can and is not slated to be deleted. | [optional] [readonly] 
**industryCategory** | **String** | Industry associated with this property Example: AUTOMOTIVE, FOOD_AND_DRINK | [optional] 
**name** | **String** | Output only. Resource name of this property. Format: properties/{property_id} Example: \&quot;properties/1000\&quot; | [optional] [readonly] 
**parent** | **String** | Immutable. Resource name of this property&#39;s logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/{account}, properties/{property} Example: \&quot;accounts/100\&quot;, \&quot;properties/101\&quot; | [optional] 
**propertyType** | **String** | Immutable. The property type for this Property resource. When creating a property, if the type is \&quot;PROPERTY_TYPE_UNSPECIFIED\&quot;, then \&quot;ORDINARY_PROPERTY\&quot; will be implied. | [optional] 
**serviceLevel** | **String** | Output only. The Google Analytics service level that applies to this property. | [optional] [readonly] 
**timeZone** | **String** | Required. Reporting Time Zone, used as the day boundary for reports, regardless of where the data originates. If the time zone honors DST, Analytics will automatically adjust for the changes. NOTE: Changing the time zone only affects data going forward, and is not applied retroactively. Format: https://www.iana.org/time-zones Example: \&quot;America/Los_Angeles\&quot; | [optional] 
**updateTime** | **String** | Output only. Time when entity payload fields were last updated. | [optional] [readonly] 



## Enum: IndustryCategoryEnum


* `INDUSTRY_CATEGORY_UNSPECIFIED` (value: `"INDUSTRY_CATEGORY_UNSPECIFIED"`)

* `AUTOMOTIVE` (value: `"AUTOMOTIVE"`)

* `BUSINESS_AND_INDUSTRIAL_MARKETS` (value: `"BUSINESS_AND_INDUSTRIAL_MARKETS"`)

* `FINANCE` (value: `"FINANCE"`)

* `HEALTHCARE` (value: `"HEALTHCARE"`)

* `TECHNOLOGY` (value: `"TECHNOLOGY"`)

* `TRAVEL` (value: `"TRAVEL"`)

* `OTHER` (value: `"OTHER"`)

* `ARTS_AND_ENTERTAINMENT` (value: `"ARTS_AND_ENTERTAINMENT"`)

* `BEAUTY_AND_FITNESS` (value: `"BEAUTY_AND_FITNESS"`)

* `BOOKS_AND_LITERATURE` (value: `"BOOKS_AND_LITERATURE"`)

* `FOOD_AND_DRINK` (value: `"FOOD_AND_DRINK"`)

* `GAMES` (value: `"GAMES"`)

* `HOBBIES_AND_LEISURE` (value: `"HOBBIES_AND_LEISURE"`)

* `HOME_AND_GARDEN` (value: `"HOME_AND_GARDEN"`)

* `INTERNET_AND_TELECOM` (value: `"INTERNET_AND_TELECOM"`)

* `LAW_AND_GOVERNMENT` (value: `"LAW_AND_GOVERNMENT"`)

* `NEWS` (value: `"NEWS"`)

* `ONLINE_COMMUNITIES` (value: `"ONLINE_COMMUNITIES"`)

* `PEOPLE_AND_SOCIETY` (value: `"PEOPLE_AND_SOCIETY"`)

* `PETS_AND_ANIMALS` (value: `"PETS_AND_ANIMALS"`)

* `REAL_ESTATE` (value: `"REAL_ESTATE"`)

* `REFERENCE` (value: `"REFERENCE"`)

* `SCIENCE` (value: `"SCIENCE"`)

* `SPORTS` (value: `"SPORTS"`)

* `JOBS_AND_EDUCATION` (value: `"JOBS_AND_EDUCATION"`)

* `SHOPPING` (value: `"SHOPPING"`)





## Enum: PropertyTypeEnum


* `UNSPECIFIED` (value: `"PROPERTY_TYPE_UNSPECIFIED"`)

* `ORDINARY` (value: `"PROPERTY_TYPE_ORDINARY"`)

* `SUBPROPERTY` (value: `"PROPERTY_TYPE_SUBPROPERTY"`)

* `ROLLUP` (value: `"PROPERTY_TYPE_ROLLUP"`)





## Enum: ServiceLevelEnum


* `SERVICE_LEVEL_UNSPECIFIED` (value: `"SERVICE_LEVEL_UNSPECIFIED"`)

* `GOOGLE_ANALYTICS_STANDARD` (value: `"GOOGLE_ANALYTICS_STANDARD"`)

* `GOOGLE_ANALYTICS_360` (value: `"GOOGLE_ANALYTICS_360"`)




