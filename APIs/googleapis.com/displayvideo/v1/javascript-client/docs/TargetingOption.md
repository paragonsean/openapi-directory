# DisplayVideo360Api.TargetingOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageRangeDetails** | [**AgeRangeTargetingOptionDetails**](AgeRangeTargetingOptionDetails.md) |  | [optional] 
**appCategoryDetails** | [**AppCategoryTargetingOptionDetails**](AppCategoryTargetingOptionDetails.md) |  | [optional] 
**audioContentTypeDetails** | [**AudioContentTypeTargetingOptionDetails**](AudioContentTypeTargetingOptionDetails.md) |  | [optional] 
**authorizedSellerStatusDetails** | [**AuthorizedSellerStatusTargetingOptionDetails**](AuthorizedSellerStatusTargetingOptionDetails.md) |  | [optional] 
**browserDetails** | [**BrowserTargetingOptionDetails**](BrowserTargetingOptionDetails.md) |  | [optional] 
**businessChainDetails** | [**BusinessChainTargetingOptionDetails**](BusinessChainTargetingOptionDetails.md) |  | [optional] 
**carrierAndIspDetails** | [**CarrierAndIspTargetingOptionDetails**](CarrierAndIspTargetingOptionDetails.md) |  | [optional] 
**categoryDetails** | [**CategoryTargetingOptionDetails**](CategoryTargetingOptionDetails.md) |  | [optional] 
**contentDurationDetails** | [**ContentDurationTargetingOptionDetails**](ContentDurationTargetingOptionDetails.md) |  | [optional] 
**contentGenreDetails** | [**ContentGenreTargetingOptionDetails**](ContentGenreTargetingOptionDetails.md) |  | [optional] 
**contentInstreamPositionDetails** | [**ContentInstreamPositionTargetingOptionDetails**](ContentInstreamPositionTargetingOptionDetails.md) |  | [optional] 
**contentOutstreamPositionDetails** | [**ContentOutstreamPositionTargetingOptionDetails**](ContentOutstreamPositionTargetingOptionDetails.md) |  | [optional] 
**contentStreamTypeDetails** | [**ContentStreamTypeTargetingOptionDetails**](ContentStreamTypeTargetingOptionDetails.md) |  | [optional] 
**deviceMakeModelDetails** | [**DeviceMakeModelTargetingOptionDetails**](DeviceMakeModelTargetingOptionDetails.md) |  | [optional] 
**deviceTypeDetails** | [**DeviceTypeTargetingOptionDetails**](DeviceTypeTargetingOptionDetails.md) |  | [optional] 
**digitalContentLabelDetails** | [**DigitalContentLabelTargetingOptionDetails**](DigitalContentLabelTargetingOptionDetails.md) |  | [optional] 
**environmentDetails** | [**EnvironmentTargetingOptionDetails**](EnvironmentTargetingOptionDetails.md) |  | [optional] 
**exchangeDetails** | [**ExchangeTargetingOptionDetails**](ExchangeTargetingOptionDetails.md) |  | [optional] 
**genderDetails** | [**GenderTargetingOptionDetails**](GenderTargetingOptionDetails.md) |  | [optional] 
**geoRegionDetails** | [**GeoRegionTargetingOptionDetails**](GeoRegionTargetingOptionDetails.md) |  | [optional] 
**householdIncomeDetails** | [**HouseholdIncomeTargetingOptionDetails**](HouseholdIncomeTargetingOptionDetails.md) |  | [optional] 
**languageDetails** | [**LanguageTargetingOptionDetails**](LanguageTargetingOptionDetails.md) |  | [optional] 
**name** | **String** | Output only. The resource name for this targeting option. | [optional] [readonly] 
**nativeContentPositionDetails** | [**NativeContentPositionTargetingOptionDetails**](NativeContentPositionTargetingOptionDetails.md) |  | [optional] 
**omidDetails** | [**OmidTargetingOptionDetails**](OmidTargetingOptionDetails.md) |  | [optional] 
**onScreenPositionDetails** | [**OnScreenPositionTargetingOptionDetails**](OnScreenPositionTargetingOptionDetails.md) |  | [optional] 
**operatingSystemDetails** | [**OperatingSystemTargetingOptionDetails**](OperatingSystemTargetingOptionDetails.md) |  | [optional] 
**parentalStatusDetails** | [**ParentalStatusTargetingOptionDetails**](ParentalStatusTargetingOptionDetails.md) |  | [optional] 
**poiDetails** | [**PoiTargetingOptionDetails**](PoiTargetingOptionDetails.md) |  | [optional] 
**sensitiveCategoryDetails** | [**SensitiveCategoryTargetingOptionDetails**](SensitiveCategoryTargetingOptionDetails.md) |  | [optional] 
**subExchangeDetails** | [**SubExchangeTargetingOptionDetails**](SubExchangeTargetingOptionDetails.md) |  | [optional] 
**targetingOptionId** | **String** | Output only. A unique identifier for this targeting option. The tuple {&#x60;targeting_type&#x60;, &#x60;targeting_option_id&#x60;} will be unique. | [optional] [readonly] 
**targetingType** | **String** | Output only. The type of this targeting option. | [optional] [readonly] 
**userRewardedContentDetails** | [**UserRewardedContentTargetingOptionDetails**](UserRewardedContentTargetingOptionDetails.md) |  | [optional] 
**videoPlayerSizeDetails** | [**VideoPlayerSizeTargetingOptionDetails**](VideoPlayerSizeTargetingOptionDetails.md) |  | [optional] 
**viewabilityDetails** | [**ViewabilityTargetingOptionDetails**](ViewabilityTargetingOptionDetails.md) |  | [optional] 



## Enum: TargetingTypeEnum


* `UNSPECIFIED` (value: `"TARGETING_TYPE_UNSPECIFIED"`)

* `CHANNEL` (value: `"TARGETING_TYPE_CHANNEL"`)

* `APP_CATEGORY` (value: `"TARGETING_TYPE_APP_CATEGORY"`)

* `APP` (value: `"TARGETING_TYPE_APP"`)

* `URL` (value: `"TARGETING_TYPE_URL"`)

* `DAY_AND_TIME` (value: `"TARGETING_TYPE_DAY_AND_TIME"`)

* `AGE_RANGE` (value: `"TARGETING_TYPE_AGE_RANGE"`)

* `REGIONAL_LOCATION_LIST` (value: `"TARGETING_TYPE_REGIONAL_LOCATION_LIST"`)

* `PROXIMITY_LOCATION_LIST` (value: `"TARGETING_TYPE_PROXIMITY_LOCATION_LIST"`)

* `GENDER` (value: `"TARGETING_TYPE_GENDER"`)

* `VIDEO_PLAYER_SIZE` (value: `"TARGETING_TYPE_VIDEO_PLAYER_SIZE"`)

* `USER_REWARDED_CONTENT` (value: `"TARGETING_TYPE_USER_REWARDED_CONTENT"`)

* `PARENTAL_STATUS` (value: `"TARGETING_TYPE_PARENTAL_STATUS"`)

* `CONTENT_INSTREAM_POSITION` (value: `"TARGETING_TYPE_CONTENT_INSTREAM_POSITION"`)

* `CONTENT_OUTSTREAM_POSITION` (value: `"TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION"`)

* `DEVICE_TYPE` (value: `"TARGETING_TYPE_DEVICE_TYPE"`)

* `AUDIENCE_GROUP` (value: `"TARGETING_TYPE_AUDIENCE_GROUP"`)

* `BROWSER` (value: `"TARGETING_TYPE_BROWSER"`)

* `HOUSEHOLD_INCOME` (value: `"TARGETING_TYPE_HOUSEHOLD_INCOME"`)

* `ON_SCREEN_POSITION` (value: `"TARGETING_TYPE_ON_SCREEN_POSITION"`)

* `THIRD_PARTY_VERIFIER` (value: `"TARGETING_TYPE_THIRD_PARTY_VERIFIER"`)

* `DIGITAL_CONTENT_LABEL_EXCLUSION` (value: `"TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION"`)

* `SENSITIVE_CATEGORY_EXCLUSION` (value: `"TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION"`)

* `ENVIRONMENT` (value: `"TARGETING_TYPE_ENVIRONMENT"`)

* `CARRIER_AND_ISP` (value: `"TARGETING_TYPE_CARRIER_AND_ISP"`)

* `OPERATING_SYSTEM` (value: `"TARGETING_TYPE_OPERATING_SYSTEM"`)

* `DEVICE_MAKE_MODEL` (value: `"TARGETING_TYPE_DEVICE_MAKE_MODEL"`)

* `KEYWORD` (value: `"TARGETING_TYPE_KEYWORD"`)

* `NEGATIVE_KEYWORD_LIST` (value: `"TARGETING_TYPE_NEGATIVE_KEYWORD_LIST"`)

* `VIEWABILITY` (value: `"TARGETING_TYPE_VIEWABILITY"`)

* `CATEGORY` (value: `"TARGETING_TYPE_CATEGORY"`)

* `INVENTORY_SOURCE` (value: `"TARGETING_TYPE_INVENTORY_SOURCE"`)

* `LANGUAGE` (value: `"TARGETING_TYPE_LANGUAGE"`)

* `AUTHORIZED_SELLER_STATUS` (value: `"TARGETING_TYPE_AUTHORIZED_SELLER_STATUS"`)

* `GEO_REGION` (value: `"TARGETING_TYPE_GEO_REGION"`)

* `INVENTORY_SOURCE_GROUP` (value: `"TARGETING_TYPE_INVENTORY_SOURCE_GROUP"`)

* `EXCHANGE` (value: `"TARGETING_TYPE_EXCHANGE"`)

* `SUB_EXCHANGE` (value: `"TARGETING_TYPE_SUB_EXCHANGE"`)

* `POI` (value: `"TARGETING_TYPE_POI"`)

* `BUSINESS_CHAIN` (value: `"TARGETING_TYPE_BUSINESS_CHAIN"`)

* `CONTENT_DURATION` (value: `"TARGETING_TYPE_CONTENT_DURATION"`)

* `CONTENT_STREAM_TYPE` (value: `"TARGETING_TYPE_CONTENT_STREAM_TYPE"`)

* `NATIVE_CONTENT_POSITION` (value: `"TARGETING_TYPE_NATIVE_CONTENT_POSITION"`)

* `OMID` (value: `"TARGETING_TYPE_OMID"`)

* `AUDIO_CONTENT_TYPE` (value: `"TARGETING_TYPE_AUDIO_CONTENT_TYPE"`)

* `CONTENT_GENRE` (value: `"TARGETING_TYPE_CONTENT_GENRE"`)




