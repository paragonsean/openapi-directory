

# TaxOrFee

Details of a tax or fee (included or excluded in a rate).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Structured information on what type the type of tax or fee. |  [optional] |
|**charges** | [**Money**](Money.md) |  |  [optional] |
|**formatted** | **String** | Formatted English description of this tax or fee, ready to be shown to your guests. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| VAT | &quot;VAT&quot; |
| CITY_TAX | &quot;CITY_TAX&quot; |
| OTHER | &quot;OTHER&quot; |



