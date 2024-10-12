# DisplayVideo360Api.DoubleVerify

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appStarRating** | [**DoubleVerifyAppStarRating**](DoubleVerifyAppStarRating.md) |  | [optional] 
**avoidedAgeRatings** | **[String]** | Avoid bidding on apps with the age rating. | [optional] 
**brandSafetyCategories** | [**DoubleVerifyBrandSafetyCategories**](DoubleVerifyBrandSafetyCategories.md) |  | [optional] 
**customSegmentId** | **String** | The custom segment ID provided by DoubleVerify. The ID must start with \&quot;51\&quot; and consist of eight digits. Custom segment ID cannot be specified along with any of the following fields: * brand_safety_categories * avoided_age_ratings * app_star_rating * fraud_invalid_traffic | [optional] 
**displayViewability** | [**DoubleVerifyDisplayViewability**](DoubleVerifyDisplayViewability.md) |  | [optional] 
**fraudInvalidTraffic** | [**DoubleVerifyFraudInvalidTraffic**](DoubleVerifyFraudInvalidTraffic.md) |  | [optional] 
**videoViewability** | [**DoubleVerifyVideoViewability**](DoubleVerifyVideoViewability.md) |  | [optional] 



## Enum: [AvoidedAgeRatingsEnum]


* `AGE_RATING_UNSPECIFIED` (value: `"AGE_RATING_UNSPECIFIED"`)

* `APP_AGE_RATE_UNKNOWN` (value: `"APP_AGE_RATE_UNKNOWN"`)

* `APP_AGE_RATE_4_PLUS` (value: `"APP_AGE_RATE_4_PLUS"`)

* `APP_AGE_RATE_9_PLUS` (value: `"APP_AGE_RATE_9_PLUS"`)

* `APP_AGE_RATE_12_PLUS` (value: `"APP_AGE_RATE_12_PLUS"`)

* `APP_AGE_RATE_17_PLUS` (value: `"APP_AGE_RATE_17_PLUS"`)

* `APP_AGE_RATE_18_PLUS` (value: `"APP_AGE_RATE_18_PLUS"`)




