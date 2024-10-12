

# OmidAssignedTargetingOptionDetails

Represents a targetable Open Measurement enabled inventory type. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_OMID`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**omid** | [**OmidEnum**](#OmidEnum) | Required. The type of Open Measurement enabled inventory. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_OMID&#x60;. |  [optional] |



## Enum: OmidEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OMID_UNSPECIFIED&quot; |
| FOR_MOBILE_DISPLAY_ADS | &quot;OMID_FOR_MOBILE_DISPLAY_ADS&quot; |



