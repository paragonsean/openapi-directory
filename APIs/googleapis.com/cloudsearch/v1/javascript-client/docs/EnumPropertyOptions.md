# CloudSearchApi.EnumPropertyOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operatorOptions** | [**EnumOperatorOptions**](EnumOperatorOptions.md) |  | [optional] 
**orderedRanking** | **String** | Used to specify the ordered ranking for the enumeration that determines how the integer values provided in the possible EnumValuePairs are used to rank results. If specified, integer values must be provided for all possible EnumValuePair values given for this property. Can only be used if isRepeatable is false. | [optional] 
**possibleValues** | [**[EnumValuePair]**](EnumValuePair.md) | The list of possible values for the enumeration property. All EnumValuePairs must provide a string value. If you specify an integer value for one EnumValuePair, then all possible EnumValuePairs must provide an integer value. Both the string value and integer value must be unique over all possible values. Once set, possible values cannot be removed or modified. If you supply an ordered ranking and think you might insert additional enum values in the future, leave gaps in the initial integer values to allow adding a value in between previously registered values. The maximum number of elements is 100. | [optional] 



## Enum: OrderedRankingEnum


* `NO_ORDER` (value: `"NO_ORDER"`)

* `ASCENDING` (value: `"ASCENDING"`)

* `DESCENDING` (value: `"DESCENDING"`)




