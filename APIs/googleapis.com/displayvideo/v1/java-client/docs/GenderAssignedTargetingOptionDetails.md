

# GenderAssignedTargetingOptionDetails

Details for assigned gender targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_GENDER`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gender** | [**GenderEnum**](#GenderEnum) | Required. The gender of the audience. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_GENDER&#x60;. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GENDER_UNSPECIFIED&quot; |
| MALE | &quot;GENDER_MALE&quot; |
| FEMALE | &quot;GENDER_FEMALE&quot; |
| UNKNOWN | &quot;GENDER_UNKNOWN&quot; |



