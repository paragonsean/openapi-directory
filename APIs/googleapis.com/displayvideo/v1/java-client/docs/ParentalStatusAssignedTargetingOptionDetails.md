

# ParentalStatusAssignedTargetingOptionDetails

Details for assigned parental status targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_PARENTAL_STATUS`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parentalStatus** | [**ParentalStatusEnum**](#ParentalStatusEnum) | Required. The parental status of the audience. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60;. |  [optional] |



## Enum: ParentalStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARENTAL_STATUS_UNSPECIFIED&quot; |
| PARENT | &quot;PARENTAL_STATUS_PARENT&quot; |
| NOT_A_PARENT | &quot;PARENTAL_STATUS_NOT_A_PARENT&quot; |
| UNKNOWN | &quot;PARENTAL_STATUS_UNKNOWN&quot; |



