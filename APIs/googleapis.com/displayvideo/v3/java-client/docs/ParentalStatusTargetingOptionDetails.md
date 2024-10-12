

# ParentalStatusTargetingOptionDetails

Represents a targetable parental status. This will be populated in the parental_status_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_PARENTAL_STATUS`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parentalStatus** | [**ParentalStatusEnum**](#ParentalStatusEnum) | Output only. The parental status of an audience. |  [optional] [readonly] |



## Enum: ParentalStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARENTAL_STATUS_UNSPECIFIED&quot; |
| PARENT | &quot;PARENTAL_STATUS_PARENT&quot; |
| NOT_A_PARENT | &quot;PARENTAL_STATUS_NOT_A_PARENT&quot; |
| UNKNOWN | &quot;PARENTAL_STATUS_UNKNOWN&quot; |



