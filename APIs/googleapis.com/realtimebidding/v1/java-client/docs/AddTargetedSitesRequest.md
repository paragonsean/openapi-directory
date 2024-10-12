

# AddTargetedSitesRequest

A request to start targeting the provided sites in a specific pretargeting configuration. The pretargeting configuration itself specifies how these sites are targeted in PretargetingConfig.webTargeting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sites** | **List&lt;String&gt;** | A list of site URLs to target in the pretargeting configuration. These values will be added to the list of targeted URLs in PretargetingConfig.webTargeting.values. |  [optional] |
|**targetingMode** | [**TargetingModeEnum**](#TargetingModeEnum) | Required. The targeting mode that should be applied to the list of site URLs. If there are existing targeted sites, must be equal to the existing PretargetingConfig.webTargeting.targetingMode or a 400 bad request error will be returned. |  [optional] |



## Enum: TargetingModeEnum

| Name | Value |
|---- | -----|
| TARGETING_MODE_UNSPECIFIED | &quot;TARGETING_MODE_UNSPECIFIED&quot; |
| INCLUSIVE | &quot;INCLUSIVE&quot; |
| EXCLUSIVE | &quot;EXCLUSIVE&quot; |



