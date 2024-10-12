# YodleeCoreApis.UpdateAccountInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** |  | [optional] 
**accountNumber** | **String** |  | [optional] 
**accountStatus** | **String** |  | [optional] 
**address** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**amountDue** | [**Money**](Money.md) |  | [optional] 
**balance** | [**Money**](Money.md) |  | [optional] 
**container** | **String** |  | [optional] 
**dueDate** | **String** |  | [optional] 
**frequency** | **String** |  | [optional] 
**homeValue** | [**Money**](Money.md) |  | [optional] 
**includeInNetWorth** | **String** |  | [optional] 
**isEbillEnrolled** | **String** |  | [optional] 
**memo** | **String** |  | [optional] 
**nickname** | **String** |  | [optional] 



## Enum: AccountStatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `TO_BE_CLOSED` (value: `"TO_BE_CLOSED"`)

* `CLOSED` (value: `"CLOSED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: ContainerEnum


* `bank` (value: `"bank"`)

* `creditCard` (value: `"creditCard"`)

* `investment` (value: `"investment"`)

* `insurance` (value: `"insurance"`)

* `loan` (value: `"loan"`)

* `reward` (value: `"reward"`)

* `realEstate` (value: `"realEstate"`)

* `otherAssets` (value: `"otherAssets"`)

* `otherLiabilities` (value: `"otherLiabilities"`)





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




