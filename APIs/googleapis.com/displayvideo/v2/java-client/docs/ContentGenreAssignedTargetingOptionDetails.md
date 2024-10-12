

# ContentGenreAssignedTargetingOptionDetails

Details for content genre assigned targeting option. This will be populated in the content_genre_details field when targeting_type is `TARGETING_TYPE_CONTENT_GENRE`. Explicitly targeting all options is not supported. Remove all content genre targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of the content genre. |  [optional] [readonly] |
|**negative** | **Boolean** | Indicates if this option is being negatively targeted. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60;. |  [optional] |



