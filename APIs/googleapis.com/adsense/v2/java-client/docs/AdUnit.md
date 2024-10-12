

# AdUnit

Representation of an ad unit. An ad unit represents a saved ad unit with a specific set of ad settings that have been customized within an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentAdsSettings** | [**ContentAdsSettings**](ContentAdsSettings.md) |  |  [optional] |
|**displayName** | **String** | Required. Display name of the ad unit, as provided when the ad unit was created. |  [optional] |
|**name** | **String** | Output only. Resource name of the ad unit. Format: accounts/{account}/adclients/{adclient}/adunits/{adunit} |  [optional] [readonly] |
|**reportingDimensionId** | **String** | Output only. Unique ID of the ad unit as used in the &#x60;AD_UNIT_ID&#x60; reporting dimension. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Required. State of the ad unit. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



