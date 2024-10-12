

# NutritionFact

This message denotes nutrition information with an upper bound and lower bound range and can be represented by mass unit. Lower amount must be specified. Both lower and upper amounts are non-negative numbers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lowerAmount** | **Double** | Required. Lower amount of nutrition |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Required. Unit of the given nutrition information. |  [optional] |
|**upperAmount** | **Double** | Optional. Upper amount of nutrition |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MASS_UNIT_UNSPECIFIED | &quot;MASS_UNIT_UNSPECIFIED&quot; |
| GRAM | &quot;GRAM&quot; |
| MILLIGRAM | &quot;MILLIGRAM&quot; |



