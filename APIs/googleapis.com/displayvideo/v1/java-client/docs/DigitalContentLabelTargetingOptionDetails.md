

# DigitalContentLabelTargetingOptionDetails

Represents a targetable digital content label rating tier. This will be populated in the digital_content_label_details field of the TargetingOption when targeting_type is `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentRatingTier** | [**ContentRatingTierEnum**](#ContentRatingTierEnum) | Output only. An enum for the content label brand safety tiers. |  [optional] [readonly] |



## Enum: ContentRatingTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_RATING_TIER_UNSPECIFIED&quot; |
| UNRATED | &quot;CONTENT_RATING_TIER_UNRATED&quot; |
| GENERAL | &quot;CONTENT_RATING_TIER_GENERAL&quot; |
| PARENTAL_GUIDANCE | &quot;CONTENT_RATING_TIER_PARENTAL_GUIDANCE&quot; |
| TEENS | &quot;CONTENT_RATING_TIER_TEENS&quot; |
| MATURE | &quot;CONTENT_RATING_TIER_MATURE&quot; |



