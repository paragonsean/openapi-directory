

# UsersIdAccountsPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | A currency code for the account. |  |
|**institutionId** | **Integer** | The ID of the institution to create this account in. |  |
|**title** | **String** | A title for the account. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the account. |  |



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



