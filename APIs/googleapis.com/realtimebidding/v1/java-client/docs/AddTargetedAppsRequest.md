

# AddTargetedAppsRequest

A request to start targeting the provided app IDs in a specific pretargeting configuration. The pretargeting configuration itself specifies how these apps are targeted. in PretargetingConfig.appTargeting.mobileAppTargeting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appIds** | **List&lt;String&gt;** | A list of app IDs to target in the pretargeting configuration. These values will be added to the list of targeted app IDs in PretargetingConfig.appTargeting.mobileAppTargeting.values. |  [optional] |
|**targetingMode** | [**TargetingModeEnum**](#TargetingModeEnum) | Required. The targeting mode that should be applied to the list of app IDs. If there are existing targeted app IDs, must be equal to the existing PretargetingConfig.appTargeting.mobileAppTargeting.targetingMode or a 400 bad request error will be returned. |  [optional] |



## Enum: TargetingModeEnum

| Name | Value |
|---- | -----|
| TARGETING_MODE_UNSPECIFIED | &quot;TARGETING_MODE_UNSPECIFIED&quot; |
| INCLUSIVE | &quot;INCLUSIVE&quot; |
| EXCLUSIVE | &quot;EXCLUSIVE&quot; |



