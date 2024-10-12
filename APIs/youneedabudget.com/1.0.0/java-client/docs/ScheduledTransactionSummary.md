

# ScheduledTransactionSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **UUID** |  |  |
|**amount** | **Long** | The scheduled transaction amount in milliunits format |  |
|**categoryId** | **UUID** |  |  [optional] |
|**dateFirst** | **LocalDate** | The first date for which the Scheduled Transaction was scheduled. |  |
|**dateNext** | **LocalDate** | The next date for which the Scheduled Transaction is scheduled. |  |
|**deleted** | **Boolean** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. |  |
|**flagColor** | [**FlagColorEnum**](#FlagColorEnum) | The scheduled transaction flag |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) |  |  |
|**id** | **UUID** |  |  |
|**memo** | **String** |  |  [optional] |
|**payeeId** | **UUID** |  |  [optional] |
|**transferAccountId** | **UUID** | If a transfer, the account_id which the scheduled transaction transfers to |  [optional] |



## Enum: FlagColorEnum

| Name | Value |
|---- | -----|
| RED | &quot;red&quot; |
| ORANGE | &quot;orange&quot; |
| YELLOW | &quot;yellow&quot; |
| GREEN | &quot;green&quot; |
| BLUE | &quot;blue&quot; |
| PURPLE | &quot;purple&quot; |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| NEVER | &quot;never&quot; |
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| EVERY_OTHER_WEEK | &quot;everyOtherWeek&quot; |
| TWICE_A_MONTH | &quot;twiceAMonth&quot; |
| EVERY4_WEEKS | &quot;every4Weeks&quot; |
| MONTHLY | &quot;monthly&quot; |
| EVERY_OTHER_MONTH | &quot;everyOtherMonth&quot; |
| EVERY3_MONTHS | &quot;every3Months&quot; |
| EVERY4_MONTHS | &quot;every4Months&quot; |
| TWICE_A_YEAR | &quot;twiceAYear&quot; |
| YEARLY | &quot;yearly&quot; |
| EVERY_OTHER_YEAR | &quot;everyOtherYear&quot; |



