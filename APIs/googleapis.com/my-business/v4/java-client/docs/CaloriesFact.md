

# CaloriesFact

This message denotes calories information with an upper bound and lower bound range. Lower amount must be specified. Both lower and upper amounts are non-negative numbers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lowerAmount** | **Integer** | Required. Lower amount of calories |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Required. Unit of the given calories information. |  [optional] |
|**upperAmount** | **Integer** | Optional. Upper amount of calories |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| ENERGY_UNIT_UNSPECIFIED | &quot;ENERGY_UNIT_UNSPECIFIED&quot; |
| CALORIE | &quot;CALORIE&quot; |
| JOULE | &quot;JOULE&quot; |



