

# AddTargetedPublishersRequest

A request to start targeting the provided publishers in a specific pretargeting configuration. The pretargeting configuration itself specifies how these publishers are targeted in PretargetingConfig.publisherTargeting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publisherIds** | **List&lt;String&gt;** | A list of publisher IDs to target in the pretargeting configuration. These values will be added to the list of targeted publisher IDs in PretargetingConfig.publisherTargeting.values. Publishers are identified by their publisher ID from ads.txt / app-ads.txt. See https://iabtechlab.com/ads-txt/ and https://iabtechlab.com/app-ads-txt/ for more details. |  [optional] |
|**targetingMode** | [**TargetingModeEnum**](#TargetingModeEnum) | Required. The targeting mode that should be applied to the list of publisher IDs. If are existing publisher IDs, must be equal to the existing PretargetingConfig.publisherTargeting.targetingMode or a 400 bad request error will be returned. |  [optional] |



## Enum: TargetingModeEnum

| Name | Value |
|---- | -----|
| TARGETING_MODE_UNSPECIFIED | &quot;TARGETING_MODE_UNSPECIFIED&quot; |
| INCLUSIVE | &quot;INCLUSIVE&quot; |
| EXCLUSIVE | &quot;EXCLUSIVE&quot; |



