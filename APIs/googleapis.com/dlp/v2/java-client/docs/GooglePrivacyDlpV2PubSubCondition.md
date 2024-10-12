

# GooglePrivacyDlpV2PubSubCondition

A condition consisting of a value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**minimumRiskScore** | [**MinimumRiskScoreEnum**](#MinimumRiskScoreEnum) | The minimum data risk score that triggers the condition. |  [optional] |
|**minimumSensitivityScore** | [**MinimumSensitivityScoreEnum**](#MinimumSensitivityScoreEnum) | The minimum sensitivity level that triggers the condition. |  [optional] |



## Enum: MinimumRiskScoreEnum

| Name | Value |
|---- | -----|
| PROFILE_SCORE_BUCKET_UNSPECIFIED | &quot;PROFILE_SCORE_BUCKET_UNSPECIFIED&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM_OR_HIGH | &quot;MEDIUM_OR_HIGH&quot; |



## Enum: MinimumSensitivityScoreEnum

| Name | Value |
|---- | -----|
| PROFILE_SCORE_BUCKET_UNSPECIFIED | &quot;PROFILE_SCORE_BUCKET_UNSPECIFIED&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM_OR_HIGH | &quot;MEDIUM_OR_HIGH&quot; |



