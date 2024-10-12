# RealTimeBiddingApi.AddTargetedSitesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sites** | **[String]** | A list of site URLs to target in the pretargeting configuration. These values will be added to the list of targeted URLs in PretargetingConfig.webTargeting.values. | [optional] 
**targetingMode** | **String** | Required. The targeting mode that should be applied to the list of site URLs. If there are existing targeted sites, must be equal to the existing PretargetingConfig.webTargeting.targetingMode or a 400 bad request error will be returned. | [optional] 



## Enum: TargetingModeEnum


* `TARGETING_MODE_UNSPECIFIED` (value: `"TARGETING_MODE_UNSPECIFIED"`)

* `INCLUSIVE` (value: `"INCLUSIVE"`)

* `EXCLUSIVE` (value: `"EXCLUSIVE"`)




