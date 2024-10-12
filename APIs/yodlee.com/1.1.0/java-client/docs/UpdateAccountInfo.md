

# UpdateAccountInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** |  |  [optional] |
|**accountNumber** | **String** |  |  [optional] |
|**accountStatus** | [**AccountStatusEnum**](#AccountStatusEnum) |  |  [optional] |
|**address** | [**AccountAddress**](AccountAddress.md) |  |  [optional] |
|**amountDue** | [**Money**](Money.md) |  |  [optional] |
|**balance** | [**Money**](Money.md) |  |  [optional] |
|**container** | [**ContainerEnum**](#ContainerEnum) |  |  [optional] |
|**dueDate** | **String** |  |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) |  |  [optional] |
|**homeValue** | [**Money**](Money.md) |  |  [optional] |
|**includeInNetWorth** | **String** |  |  [optional] |
|**isEbillEnrolled** | **String** |  |  [optional] |
|**memo** | **String** |  |  [optional] |
|**nickname** | **String** |  |  [optional] |



## Enum: AccountStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| TO_BE_CLOSED | &quot;TO_BE_CLOSED&quot; |
| CLOSED | &quot;CLOSED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: ContainerEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDIT_CARD | &quot;creditCard&quot; |
| INVESTMENT | &quot;investment&quot; |
| INSURANCE | &quot;insurance&quot; |
| LOAN | &quot;loan&quot; |
| REWARD | &quot;reward&quot; |
| REAL_ESTATE | &quot;realEstate&quot; |
| OTHER_ASSETS | &quot;otherAssets&quot; |
| OTHER_LIABILITIES | &quot;otherLiabilities&quot; |



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



