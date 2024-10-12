

# HouseholdIncomeAssignedTargetingOptionDetails

Details for assigned household income targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_HOUSEHOLD_INCOME`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**householdIncome** | [**HouseholdIncomeEnum**](#HouseholdIncomeEnum) | Required. The household income of the audience. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60;. |  [optional] |



## Enum: HouseholdIncomeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HOUSEHOLD_INCOME_UNSPECIFIED&quot; |
| UNKNOWN | &quot;HOUSEHOLD_INCOME_UNKNOWN&quot; |
| LOWER_50_PERCENT | &quot;HOUSEHOLD_INCOME_LOWER_50_PERCENT&quot; |
| TOP_41_TO_50_PERCENT | &quot;HOUSEHOLD_INCOME_TOP_41_TO_50_PERCENT&quot; |
| TOP_31_TO_40_PERCENT | &quot;HOUSEHOLD_INCOME_TOP_31_TO_40_PERCENT&quot; |
| TOP_21_TO_30_PERCENT | &quot;HOUSEHOLD_INCOME_TOP_21_TO_30_PERCENT&quot; |
| TOP_11_TO_20_PERCENT | &quot;HOUSEHOLD_INCOME_TOP_11_TO_20_PERCENT&quot; |
| TOP_10_PERCENT | &quot;HOUSEHOLD_INCOME_TOP_10_PERCENT&quot; |



