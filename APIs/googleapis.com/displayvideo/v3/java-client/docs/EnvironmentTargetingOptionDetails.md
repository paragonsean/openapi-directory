

# EnvironmentTargetingOptionDetails

Represents a targetable environment. This will be populated in the environment_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_ENVIRONMENT`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Output only. The serving environment. |  [optional] [readonly] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| WEB_OPTIMIZED | &quot;ENVIRONMENT_WEB_OPTIMIZED&quot; |
| WEB_NOT_OPTIMIZED | &quot;ENVIRONMENT_WEB_NOT_OPTIMIZED&quot; |
| APP | &quot;ENVIRONMENT_APP&quot; |



