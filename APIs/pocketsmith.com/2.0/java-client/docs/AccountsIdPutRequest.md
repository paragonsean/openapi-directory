

# AccountsIdPutRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | A new currency code for the account. |  [optional] |
|**isNetWorth** | **Boolean** | Whether the account is a net worth account. |  [optional] |
|**title** | **String** | A new title for the account. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the account. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDITS | &quot;credits&quot; |
| CASH | &quot;cash&quot; |
| LOANS | &quot;loans&quot; |
| MORTGAGE | &quot;mortgage&quot; |
| STOCKS | &quot;stocks&quot; |
| VEHICLE | &quot;vehicle&quot; |
| PROPERTY | &quot;property&quot; |
| INSURANCE | &quot;insurance&quot; |
| OTHER_ASSET | &quot;other_asset&quot; |
| OTHER_LIABILITY | &quot;other_liability&quot; |



