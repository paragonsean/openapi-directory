# RealTimeBiddingApi.AddTargetedAppsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appIds** | **[String]** | A list of app IDs to target in the pretargeting configuration. These values will be added to the list of targeted app IDs in PretargetingConfig.appTargeting.mobileAppTargeting.values. | [optional] 
**targetingMode** | **String** | Required. The targeting mode that should be applied to the list of app IDs. If there are existing targeted app IDs, must be equal to the existing PretargetingConfig.appTargeting.mobileAppTargeting.targetingMode or a 400 bad request error will be returned. | [optional] 



## Enum: TargetingModeEnum


* `TARGETING_MODE_UNSPECIFIED` (value: `"TARGETING_MODE_UNSPECIFIED"`)

* `INCLUSIVE` (value: `"INCLUSIVE"`)

* `EXCLUSIVE` (value: `"EXCLUSIVE"`)




