

# EnvironmentAssignedTargetingOptionDetails

Assigned environment targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_ENVIRONMENT`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Required. The serving environment. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; (e.g., \&quot;508010\&quot; for targeting the &#x60;ENVIRONMENT_WEB_OPTIMIZED&#x60; option). |  [optional] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| WEB_OPTIMIZED | &quot;ENVIRONMENT_WEB_OPTIMIZED&quot; |
| WEB_NOT_OPTIMIZED | &quot;ENVIRONMENT_WEB_NOT_OPTIMIZED&quot; |
| APP | &quot;ENVIRONMENT_APP&quot; |



