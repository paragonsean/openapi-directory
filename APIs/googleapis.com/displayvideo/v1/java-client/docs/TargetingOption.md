

# TargetingOption

Represents a single targeting option, which is a targetable concept in DV360.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageRangeDetails** | [**AgeRangeTargetingOptionDetails**](AgeRangeTargetingOptionDetails.md) |  |  [optional] |
|**appCategoryDetails** | [**AppCategoryTargetingOptionDetails**](AppCategoryTargetingOptionDetails.md) |  |  [optional] |
|**audioContentTypeDetails** | [**AudioContentTypeTargetingOptionDetails**](AudioContentTypeTargetingOptionDetails.md) |  |  [optional] |
|**authorizedSellerStatusDetails** | [**AuthorizedSellerStatusTargetingOptionDetails**](AuthorizedSellerStatusTargetingOptionDetails.md) |  |  [optional] |
|**browserDetails** | [**BrowserTargetingOptionDetails**](BrowserTargetingOptionDetails.md) |  |  [optional] |
|**businessChainDetails** | [**BusinessChainTargetingOptionDetails**](BusinessChainTargetingOptionDetails.md) |  |  [optional] |
|**carrierAndIspDetails** | [**CarrierAndIspTargetingOptionDetails**](CarrierAndIspTargetingOptionDetails.md) |  |  [optional] |
|**categoryDetails** | [**CategoryTargetingOptionDetails**](CategoryTargetingOptionDetails.md) |  |  [optional] |
|**contentDurationDetails** | [**ContentDurationTargetingOptionDetails**](ContentDurationTargetingOptionDetails.md) |  |  [optional] |
|**contentGenreDetails** | [**ContentGenreTargetingOptionDetails**](ContentGenreTargetingOptionDetails.md) |  |  [optional] |
|**contentInstreamPositionDetails** | [**ContentInstreamPositionTargetingOptionDetails**](ContentInstreamPositionTargetingOptionDetails.md) |  |  [optional] |
|**contentOutstreamPositionDetails** | [**ContentOutstreamPositionTargetingOptionDetails**](ContentOutstreamPositionTargetingOptionDetails.md) |  |  [optional] |
|**contentStreamTypeDetails** | [**ContentStreamTypeTargetingOptionDetails**](ContentStreamTypeTargetingOptionDetails.md) |  |  [optional] |
|**deviceMakeModelDetails** | [**DeviceMakeModelTargetingOptionDetails**](DeviceMakeModelTargetingOptionDetails.md) |  |  [optional] |
|**deviceTypeDetails** | [**DeviceTypeTargetingOptionDetails**](DeviceTypeTargetingOptionDetails.md) |  |  [optional] |
|**digitalContentLabelDetails** | [**DigitalContentLabelTargetingOptionDetails**](DigitalContentLabelTargetingOptionDetails.md) |  |  [optional] |
|**environmentDetails** | [**EnvironmentTargetingOptionDetails**](EnvironmentTargetingOptionDetails.md) |  |  [optional] |
|**exchangeDetails** | [**ExchangeTargetingOptionDetails**](ExchangeTargetingOptionDetails.md) |  |  [optional] |
|**genderDetails** | [**GenderTargetingOptionDetails**](GenderTargetingOptionDetails.md) |  |  [optional] |
|**geoRegionDetails** | [**GeoRegionTargetingOptionDetails**](GeoRegionTargetingOptionDetails.md) |  |  [optional] |
|**householdIncomeDetails** | [**HouseholdIncomeTargetingOptionDetails**](HouseholdIncomeTargetingOptionDetails.md) |  |  [optional] |
|**languageDetails** | [**LanguageTargetingOptionDetails**](LanguageTargetingOptionDetails.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name for this targeting option. |  [optional] [readonly] |
|**nativeContentPositionDetails** | [**NativeContentPositionTargetingOptionDetails**](NativeContentPositionTargetingOptionDetails.md) |  |  [optional] |
|**omidDetails** | [**OmidTargetingOptionDetails**](OmidTargetingOptionDetails.md) |  |  [optional] |
|**onScreenPositionDetails** | [**OnScreenPositionTargetingOptionDetails**](OnScreenPositionTargetingOptionDetails.md) |  |  [optional] |
|**operatingSystemDetails** | [**OperatingSystemTargetingOptionDetails**](OperatingSystemTargetingOptionDetails.md) |  |  [optional] |
|**parentalStatusDetails** | [**ParentalStatusTargetingOptionDetails**](ParentalStatusTargetingOptionDetails.md) |  |  [optional] |
|**poiDetails** | [**PoiTargetingOptionDetails**](PoiTargetingOptionDetails.md) |  |  [optional] |
|**sensitiveCategoryDetails** | [**SensitiveCategoryTargetingOptionDetails**](SensitiveCategoryTargetingOptionDetails.md) |  |  [optional] |
|**subExchangeDetails** | [**SubExchangeTargetingOptionDetails**](SubExchangeTargetingOptionDetails.md) |  |  [optional] |
|**targetingOptionId** | **String** | Output only. A unique identifier for this targeting option. The tuple {&#x60;targeting_type&#x60;, &#x60;targeting_option_id&#x60;} will be unique. |  [optional] [readonly] |
|**targetingType** | [**TargetingTypeEnum**](#TargetingTypeEnum) | Output only. The type of this targeting option. |  [optional] [readonly] |
|**userRewardedContentDetails** | [**UserRewardedContentTargetingOptionDetails**](UserRewardedContentTargetingOptionDetails.md) |  |  [optional] |
|**videoPlayerSizeDetails** | [**VideoPlayerSizeTargetingOptionDetails**](VideoPlayerSizeTargetingOptionDetails.md) |  |  [optional] |
|**viewabilityDetails** | [**ViewabilityTargetingOptionDetails**](ViewabilityTargetingOptionDetails.md) |  |  [optional] |



## Enum: TargetingTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TARGETING_TYPE_UNSPECIFIED&quot; |
| CHANNEL | &quot;TARGETING_TYPE_CHANNEL&quot; |
| APP_CATEGORY | &quot;TARGETING_TYPE_APP_CATEGORY&quot; |
| APP | &quot;TARGETING_TYPE_APP&quot; |
| URL | &quot;TARGETING_TYPE_URL&quot; |
| DAY_AND_TIME | &quot;TARGETING_TYPE_DAY_AND_TIME&quot; |
| AGE_RANGE | &quot;TARGETING_TYPE_AGE_RANGE&quot; |
| REGIONAL_LOCATION_LIST | &quot;TARGETING_TYPE_REGIONAL_LOCATION_LIST&quot; |
| PROXIMITY_LOCATION_LIST | &quot;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&quot; |
| GENDER | &quot;TARGETING_TYPE_GENDER&quot; |
| VIDEO_PLAYER_SIZE | &quot;TARGETING_TYPE_VIDEO_PLAYER_SIZE&quot; |
| USER_REWARDED_CONTENT | &quot;TARGETING_TYPE_USER_REWARDED_CONTENT&quot; |
| PARENTAL_STATUS | &quot;TARGETING_TYPE_PARENTAL_STATUS&quot; |
| CONTENT_INSTREAM_POSITION | &quot;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&quot; |
| CONTENT_OUTSTREAM_POSITION | &quot;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&quot; |
| DEVICE_TYPE | &quot;TARGETING_TYPE_DEVICE_TYPE&quot; |
| AUDIENCE_GROUP | &quot;TARGETING_TYPE_AUDIENCE_GROUP&quot; |
| BROWSER | &quot;TARGETING_TYPE_BROWSER&quot; |
| HOUSEHOLD_INCOME | &quot;TARGETING_TYPE_HOUSEHOLD_INCOME&quot; |
| ON_SCREEN_POSITION | &quot;TARGETING_TYPE_ON_SCREEN_POSITION&quot; |
| THIRD_PARTY_VERIFIER | &quot;TARGETING_TYPE_THIRD_PARTY_VERIFIER&quot; |
| DIGITAL_CONTENT_LABEL_EXCLUSION | &quot;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&quot; |
| SENSITIVE_CATEGORY_EXCLUSION | &quot;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&quot; |
| ENVIRONMENT | &quot;TARGETING_TYPE_ENVIRONMENT&quot; |
| CARRIER_AND_ISP | &quot;TARGETING_TYPE_CARRIER_AND_ISP&quot; |
| OPERATING_SYSTEM | &quot;TARGETING_TYPE_OPERATING_SYSTEM&quot; |
| DEVICE_MAKE_MODEL | &quot;TARGETING_TYPE_DEVICE_MAKE_MODEL&quot; |
| KEYWORD | &quot;TARGETING_TYPE_KEYWORD&quot; |
| NEGATIVE_KEYWORD_LIST | &quot;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&quot; |
| VIEWABILITY | &quot;TARGETING_TYPE_VIEWABILITY&quot; |
| CATEGORY | &quot;TARGETING_TYPE_CATEGORY&quot; |
| INVENTORY_SOURCE | &quot;TARGETING_TYPE_INVENTORY_SOURCE&quot; |
| LANGUAGE | &quot;TARGETING_TYPE_LANGUAGE&quot; |
| AUTHORIZED_SELLER_STATUS | &quot;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&quot; |
| GEO_REGION | &quot;TARGETING_TYPE_GEO_REGION&quot; |
| INVENTORY_SOURCE_GROUP | &quot;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&quot; |
| EXCHANGE | &quot;TARGETING_TYPE_EXCHANGE&quot; |
| SUB_EXCHANGE | &quot;TARGETING_TYPE_SUB_EXCHANGE&quot; |
| POI | &quot;TARGETING_TYPE_POI&quot; |
| BUSINESS_CHAIN | &quot;TARGETING_TYPE_BUSINESS_CHAIN&quot; |
| CONTENT_DURATION | &quot;TARGETING_TYPE_CONTENT_DURATION&quot; |
| CONTENT_STREAM_TYPE | &quot;TARGETING_TYPE_CONTENT_STREAM_TYPE&quot; |
| NATIVE_CONTENT_POSITION | &quot;TARGETING_TYPE_NATIVE_CONTENT_POSITION&quot; |
| OMID | &quot;TARGETING_TYPE_OMID&quot; |
| AUDIO_CONTENT_TYPE | &quot;TARGETING_TYPE_AUDIO_CONTENT_TYPE&quot; |
| CONTENT_GENRE | &quot;TARGETING_TYPE_CONTENT_GENRE&quot; |



