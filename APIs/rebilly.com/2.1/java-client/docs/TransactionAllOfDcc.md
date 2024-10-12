

# TransactionAllOfDcc

Dynamic Currency Conversion detailed information. Null if hasDcc is false.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**base** | [**Money**](Money.md) | Initial amount and currency to convert from. |  [optional] |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | Dynamic Currency Conversion outcome. |  [optional] |
|**quote** | [**Money**](Money.md) | Suggested amount and currency to convert to. |  [optional] |
|**usdMarkup** | **Double** | The amount of markup translated to USD. |  [optional] |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| REJECTED | &quot;rejected&quot; |
| SELECTED | &quot;selected&quot; |
| UNKNOWN | &quot;unknown&quot; |



