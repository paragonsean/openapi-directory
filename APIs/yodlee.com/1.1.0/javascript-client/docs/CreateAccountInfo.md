# YodleeCoreApis.CreateAccountInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** |  | 
**accountNumber** | **String** |  | [optional] 
**accountType** | **String** |  | 
**address** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**amountDue** | [**Money**](Money.md) |  | [optional] 
**balance** | [**Money**](Money.md) |  | [optional] 
**dueDate** | **String** |  | [optional] 
**frequency** | **String** |  | [optional] 
**homeValue** | [**Money**](Money.md) |  | [optional] 
**includeInNetWorth** | **String** |  | [optional] 
**memo** | **String** |  | [optional] 
**nickname** | **String** |  | [optional] 
**valuationType** | **String** |  | [optional] 



## Enum: FrequencyEnum


* `DAILY` (value: `"DAILY"`)

* `ONE_TIME` (value: `"ONE_TIME"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `EVERY_2_WEEKS` (value: `"EVERY_2_WEEKS"`)

* `SEMI_MONTHLY` (value: `"SEMI_MONTHLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `SEMI_ANNUALLY` (value: `"SEMI_ANNUALLY"`)

* `ANNUALLY` (value: `"ANNUALLY"`)

* `EVERY_2_MONTHS` (value: `"EVERY_2_MONTHS"`)

* `EBILL` (value: `"EBILL"`)

* `FIRST_DAY_MONTHLY` (value: `"FIRST_DAY_MONTHLY"`)

* `LAST_DAY_MONTHLY` (value: `"LAST_DAY_MONTHLY"`)

* `EVERY_4_WEEKS` (value: `"EVERY_4_WEEKS"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `OTHER` (value: `"OTHER"`)





## Enum: ValuationTypeEnum


* `SYSTEM` (value: `"SYSTEM"`)

* `MANUAL` (value: `"MANUAL"`)




