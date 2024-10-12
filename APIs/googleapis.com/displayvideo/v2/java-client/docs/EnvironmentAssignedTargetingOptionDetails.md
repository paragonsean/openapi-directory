

# EnvironmentAssignedTargetingOptionDetails

Assigned environment targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_ENVIRONMENT`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Required. The serving environment. |  [optional] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| WEB_OPTIMIZED | &quot;ENVIRONMENT_WEB_OPTIMIZED&quot; |
| WEB_NOT_OPTIMIZED | &quot;ENVIRONMENT_WEB_NOT_OPTIMIZED&quot; |
| APP | &quot;ENVIRONMENT_APP&quot; |



