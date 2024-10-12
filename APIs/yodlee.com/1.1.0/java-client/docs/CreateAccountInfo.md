

# CreateAccountInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** |  |  |
|**accountNumber** | **String** |  |  [optional] |
|**accountType** | **String** |  |  |
|**address** | [**AccountAddress**](AccountAddress.md) |  |  [optional] |
|**amountDue** | [**Money**](Money.md) |  |  [optional] |
|**balance** | [**Money**](Money.md) |  |  [optional] |
|**dueDate** | **String** |  |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) |  |  [optional] |
|**homeValue** | [**Money**](Money.md) |  |  [optional] |
|**includeInNetWorth** | **String** |  |  [optional] |
|**memo** | **String** |  |  [optional] |
|**nickname** | **String** |  |  [optional] |
|**valuationType** | [**ValuationTypeEnum**](#ValuationTypeEnum) |  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;DAILY&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| EVERY_2_WEEKS | &quot;EVERY_2_WEEKS&quot; |
| SEMI_MONTHLY | &quot;SEMI_MONTHLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| SEMI_ANNUALLY | &quot;SEMI_ANNUALLY&quot; |
| ANNUALLY | &quot;ANNUALLY&quot; |
| EVERY_2_MONTHS | &quot;EVERY_2_MONTHS&quot; |
| EBILL | &quot;EBILL&quot; |
| FIRST_DAY_MONTHLY | &quot;FIRST_DAY_MONTHLY&quot; |
| LAST_DAY_MONTHLY | &quot;LAST_DAY_MONTHLY&quot; |
| EVERY_4_WEEKS | &quot;EVERY_4_WEEKS&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: ValuationTypeEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| MANUAL | &quot;MANUAL&quot; |



