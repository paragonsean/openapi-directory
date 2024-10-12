

# UserRewardedContentAssignedTargetingOptionDetails

User rewarded content targeting option details. This will be populated in the user_rewarded_content_details field when targeting_type is `TARGETING_TYPE_USER_REWARDED_CONTENT`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60;. |  [optional] |
|**userRewardedContent** | [**UserRewardedContentEnum**](#UserRewardedContentEnum) | Output only. User rewarded content status for video ads. |  [optional] [readonly] |



## Enum: UserRewardedContentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;USER_REWARDED_CONTENT_UNSPECIFIED&quot; |
| USER_REWARDED | &quot;USER_REWARDED_CONTENT_USER_REWARDED&quot; |
| NOT_USER_REWARDED | &quot;USER_REWARDED_CONTENT_NOT_USER_REWARDED&quot; |



