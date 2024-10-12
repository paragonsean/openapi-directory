

# AssignedTargetingOption

A single assigned targeting option, which defines the state of a targeting option for an entity with targeting settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageRangeDetails** | [**AgeRangeAssignedTargetingOptionDetails**](AgeRangeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**appCategoryDetails** | [**AppCategoryAssignedTargetingOptionDetails**](AppCategoryAssignedTargetingOptionDetails.md) |  |  [optional] |
|**appDetails** | [**AppAssignedTargetingOptionDetails**](AppAssignedTargetingOptionDetails.md) |  |  [optional] |
|**assignedTargetingOptionId** | **String** | Output only. The unique ID of the assigned targeting option. The ID is only unique within a given resource and targeting type. It may be reused in other contexts. |  [optional] [readonly] |
|**assignedTargetingOptionIdAlias** | **String** | Output only. An alias for the assigned_targeting_option_id. This value can be used in place of &#x60;assignedTargetingOptionId&#x60; when retrieving or deleting existing targeting. This field will only be supported for all assigned targeting options of the following targeting types: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; This field is also supported for line item assigned targeting options of the following targeting types: * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; |  [optional] [readonly] |
|**audienceGroupDetails** | [**AudienceGroupAssignedTargetingOptionDetails**](AudienceGroupAssignedTargetingOptionDetails.md) |  |  [optional] |
|**audioContentTypeDetails** | [**AudioContentTypeAssignedTargetingOptionDetails**](AudioContentTypeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**authorizedSellerStatusDetails** | [**AuthorizedSellerStatusAssignedTargetingOptionDetails**](AuthorizedSellerStatusAssignedTargetingOptionDetails.md) |  |  [optional] |
|**browserDetails** | [**BrowserAssignedTargetingOptionDetails**](BrowserAssignedTargetingOptionDetails.md) |  |  [optional] |
|**businessChainDetails** | [**BusinessChainAssignedTargetingOptionDetails**](BusinessChainAssignedTargetingOptionDetails.md) |  |  [optional] |
|**carrierAndIspDetails** | [**CarrierAndIspAssignedTargetingOptionDetails**](CarrierAndIspAssignedTargetingOptionDetails.md) |  |  [optional] |
|**categoryDetails** | [**CategoryAssignedTargetingOptionDetails**](CategoryAssignedTargetingOptionDetails.md) |  |  [optional] |
|**channelDetails** | [**ChannelAssignedTargetingOptionDetails**](ChannelAssignedTargetingOptionDetails.md) |  |  [optional] |
|**contentDurationDetails** | [**ContentDurationAssignedTargetingOptionDetails**](ContentDurationAssignedTargetingOptionDetails.md) |  |  [optional] |
|**contentGenreDetails** | [**ContentGenreAssignedTargetingOptionDetails**](ContentGenreAssignedTargetingOptionDetails.md) |  |  [optional] |
|**contentInstreamPositionDetails** | [**ContentInstreamPositionAssignedTargetingOptionDetails**](ContentInstreamPositionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**contentOutstreamPositionDetails** | [**ContentOutstreamPositionAssignedTargetingOptionDetails**](ContentOutstreamPositionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**contentStreamTypeDetails** | [**ContentStreamTypeAssignedTargetingOptionDetails**](ContentStreamTypeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**dayAndTimeDetails** | [**DayAndTimeAssignedTargetingOptionDetails**](DayAndTimeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**deviceMakeModelDetails** | [**DeviceMakeModelAssignedTargetingOptionDetails**](DeviceMakeModelAssignedTargetingOptionDetails.md) |  |  [optional] |
|**deviceTypeDetails** | [**DeviceTypeAssignedTargetingOptionDetails**](DeviceTypeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**digitalContentLabelExclusionDetails** | [**DigitalContentLabelAssignedTargetingOptionDetails**](DigitalContentLabelAssignedTargetingOptionDetails.md) |  |  [optional] |
|**environmentDetails** | [**EnvironmentAssignedTargetingOptionDetails**](EnvironmentAssignedTargetingOptionDetails.md) |  |  [optional] |
|**exchangeDetails** | [**ExchangeAssignedTargetingOptionDetails**](ExchangeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**genderDetails** | [**GenderAssignedTargetingOptionDetails**](GenderAssignedTargetingOptionDetails.md) |  |  [optional] |
|**geoRegionDetails** | [**GeoRegionAssignedTargetingOptionDetails**](GeoRegionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**householdIncomeDetails** | [**HouseholdIncomeAssignedTargetingOptionDetails**](HouseholdIncomeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**inheritance** | [**InheritanceEnum**](#InheritanceEnum) | Output only. The inheritance status of the assigned targeting option. |  [optional] [readonly] |
|**inventorySourceDetails** | [**InventorySourceAssignedTargetingOptionDetails**](InventorySourceAssignedTargetingOptionDetails.md) |  |  [optional] |
|**inventorySourceGroupDetails** | [**InventorySourceGroupAssignedTargetingOptionDetails**](InventorySourceGroupAssignedTargetingOptionDetails.md) |  |  [optional] |
|**keywordDetails** | [**KeywordAssignedTargetingOptionDetails**](KeywordAssignedTargetingOptionDetails.md) |  |  [optional] |
|**languageDetails** | [**LanguageAssignedTargetingOptionDetails**](LanguageAssignedTargetingOptionDetails.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name for this assigned targeting option. |  [optional] [readonly] |
|**nativeContentPositionDetails** | [**NativeContentPositionAssignedTargetingOptionDetails**](NativeContentPositionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**negativeKeywordListDetails** | [**NegativeKeywordListAssignedTargetingOptionDetails**](NegativeKeywordListAssignedTargetingOptionDetails.md) |  |  [optional] |
|**omidDetails** | [**OmidAssignedTargetingOptionDetails**](OmidAssignedTargetingOptionDetails.md) |  |  [optional] |
|**onScreenPositionDetails** | [**OnScreenPositionAssignedTargetingOptionDetails**](OnScreenPositionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**operatingSystemDetails** | [**OperatingSystemAssignedTargetingOptionDetails**](OperatingSystemAssignedTargetingOptionDetails.md) |  |  [optional] |
|**parentalStatusDetails** | [**ParentalStatusAssignedTargetingOptionDetails**](ParentalStatusAssignedTargetingOptionDetails.md) |  |  [optional] |
|**poiDetails** | [**PoiAssignedTargetingOptionDetails**](PoiAssignedTargetingOptionDetails.md) |  |  [optional] |
|**proximityLocationListDetails** | [**ProximityLocationListAssignedTargetingOptionDetails**](ProximityLocationListAssignedTargetingOptionDetails.md) |  |  [optional] |
|**regionalLocationListDetails** | [**RegionalLocationListAssignedTargetingOptionDetails**](RegionalLocationListAssignedTargetingOptionDetails.md) |  |  [optional] |
|**sensitiveCategoryExclusionDetails** | [**SensitiveCategoryAssignedTargetingOptionDetails**](SensitiveCategoryAssignedTargetingOptionDetails.md) |  |  [optional] |
|**sessionPositionDetails** | [**SessionPositionAssignedTargetingOptionDetails**](SessionPositionAssignedTargetingOptionDetails.md) |  |  [optional] |
|**subExchangeDetails** | [**SubExchangeAssignedTargetingOptionDetails**](SubExchangeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**targetingType** | [**TargetingTypeEnum**](#TargetingTypeEnum) | Output only. Identifies the type of this assigned targeting option. |  [optional] [readonly] |
|**thirdPartyVerifierDetails** | [**ThirdPartyVerifierAssignedTargetingOptionDetails**](ThirdPartyVerifierAssignedTargetingOptionDetails.md) |  |  [optional] |
|**urlDetails** | [**UrlAssignedTargetingOptionDetails**](UrlAssignedTargetingOptionDetails.md) |  |  [optional] |
|**userRewardedContentDetails** | [**UserRewardedContentAssignedTargetingOptionDetails**](UserRewardedContentAssignedTargetingOptionDetails.md) |  |  [optional] |
|**videoPlayerSizeDetails** | [**VideoPlayerSizeAssignedTargetingOptionDetails**](VideoPlayerSizeAssignedTargetingOptionDetails.md) |  |  [optional] |
|**viewabilityDetails** | [**ViewabilityAssignedTargetingOptionDetails**](ViewabilityAssignedTargetingOptionDetails.md) |  |  [optional] |
|**youtubeChannelDetails** | [**YoutubeChannelAssignedTargetingOptionDetails**](YoutubeChannelAssignedTargetingOptionDetails.md) |  |  [optional] |
|**youtubeVideoDetails** | [**YoutubeVideoAssignedTargetingOptionDetails**](YoutubeVideoAssignedTargetingOptionDetails.md) |  |  [optional] |



## Enum: InheritanceEnum

| Name | Value |
|---- | -----|
| INHERITANCE_UNSPECIFIED | &quot;INHERITANCE_UNSPECIFIED&quot; |
| NOT_INHERITED | &quot;NOT_INHERITED&quot; |
| INHERITED_FROM_PARTNER | &quot;INHERITED_FROM_PARTNER&quot; |
| INHERITED_FROM_ADVERTISER | &quot;INHERITED_FROM_ADVERTISER&quot; |



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
| YOUTUBE_VIDEO | &quot;TARGETING_TYPE_YOUTUBE_VIDEO&quot; |
| YOUTUBE_CHANNEL | &quot;TARGETING_TYPE_YOUTUBE_CHANNEL&quot; |
| SESSION_POSITION | &quot;TARGETING_TYPE_SESSION_POSITION&quot; |



