

# DoubleVerify

Details of DoubleVerify settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appStarRating** | [**DoubleVerifyAppStarRating**](DoubleVerifyAppStarRating.md) |  |  [optional] |
|**avoidedAgeRatings** | [**List&lt;AvoidedAgeRatingsEnum&gt;**](#List&lt;AvoidedAgeRatingsEnum&gt;) | Avoid bidding on apps with the age rating. |  [optional] |
|**brandSafetyCategories** | [**DoubleVerifyBrandSafetyCategories**](DoubleVerifyBrandSafetyCategories.md) |  |  [optional] |
|**customSegmentId** | **String** | The custom segment ID provided by DoubleVerify. The ID must start with \&quot;51\&quot; and consist of eight digits. Custom segment ID cannot be specified along with any of the following fields: * brand_safety_categories * avoided_age_ratings * app_star_rating * fraud_invalid_traffic |  [optional] |
|**displayViewability** | [**DoubleVerifyDisplayViewability**](DoubleVerifyDisplayViewability.md) |  |  [optional] |
|**fraudInvalidTraffic** | [**DoubleVerifyFraudInvalidTraffic**](DoubleVerifyFraudInvalidTraffic.md) |  |  [optional] |
|**videoViewability** | [**DoubleVerifyVideoViewability**](DoubleVerifyVideoViewability.md) |  |  [optional] |



## Enum: List&lt;AvoidedAgeRatingsEnum&gt;

| Name | Value |
|---- | -----|
| AGE_RATING_UNSPECIFIED | &quot;AGE_RATING_UNSPECIFIED&quot; |
| APP_AGE_RATE_UNKNOWN | &quot;APP_AGE_RATE_UNKNOWN&quot; |
| APP_AGE_RATE_4_PLUS | &quot;APP_AGE_RATE_4_PLUS&quot; |
| APP_AGE_RATE_9_PLUS | &quot;APP_AGE_RATE_9_PLUS&quot; |
| APP_AGE_RATE_12_PLUS | &quot;APP_AGE_RATE_12_PLUS&quot; |
| APP_AGE_RATE_17_PLUS | &quot;APP_AGE_RATE_17_PLUS&quot; |
| APP_AGE_RATE_18_PLUS | &quot;APP_AGE_RATE_18_PLUS&quot; |



