

# StatementGetResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** |  | Actions that the Policy will execute |  [optional] |
|**condition** | [**Condition**](Condition.md) |  |  [optional] |
|**effect** | **String** | This field is not functional at the moment. To create a correct request, fill the field with &#x60;Allow&#x60; |  |
|**operation** | **String** | This operation will determine if all the conditions need to be valid or at least one of them, if the conditions array is not empty.  The possible values to these fields are &#x60;None&#x60;, &#x60;stringEquals&#x60;, &#x60;stringEqualsIgnoreCase&#x60;, &#x60;numericEquals&#x60;, &#x60;numericLessThan&#x60;, &#x60;numericLessThanEquals&#x60;,   &#x60;numericGreaterThan&#x60;, &#x60;numericGreaterThanEquals&#x60;, &#x60;bool&#x60;, &#x60;not&#x60;, &#x60;or&#x60;, &#x60;and&#x60;, &#x60;dateTimeUtcGreaterThan&#x60;, &#x60;dateTimeUtcLessThan&#x60;, and &#x60;between&#x60; |  [optional] |
|**resource** | **String** | Scope on which this policy must be evaluated |  [optional] |



