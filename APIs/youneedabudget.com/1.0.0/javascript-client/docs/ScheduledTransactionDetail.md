# YnabApiEndpoints.ScheduledTransactionDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** |  | 
**amount** | **Number** | The scheduled transaction amount in milliunits format | 
**categoryId** | **String** |  | [optional] 
**dateFirst** | **Date** | The first date for which the Scheduled Transaction was scheduled. | 
**dateNext** | **Date** | The next date for which the Scheduled Transaction is scheduled. | 
**deleted** | **Boolean** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. | 
**flagColor** | **String** | The scheduled transaction flag | [optional] 
**frequency** | **String** |  | 
**id** | **String** |  | 
**memo** | **String** |  | [optional] 
**payeeId** | **String** |  | [optional] 
**transferAccountId** | **String** | If a transfer, the account_id which the scheduled transaction transfers to | [optional] 
**accountName** | **String** |  | 
**categoryName** | **String** | The name of the category.  If a split scheduled transaction, this will be &#39;Split&#39;. | [optional] 
**payeeName** | **String** |  | [optional] 
**subtransactions** | [**[ScheduledSubTransaction]**](ScheduledSubTransaction.md) | If a split scheduled transaction, the subtransactions. | 



## Enum: FlagColorEnum


* `red` (value: `"red"`)

* `orange` (value: `"orange"`)

* `yellow` (value: `"yellow"`)

* `green` (value: `"green"`)

* `blue` (value: `"blue"`)

* `purple` (value: `"purple"`)





## Enum: FrequencyEnum


* `never` (value: `"never"`)

* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `everyOtherWeek` (value: `"everyOtherWeek"`)

* `twiceAMonth` (value: `"twiceAMonth"`)

* `every4Weeks` (value: `"every4Weeks"`)

* `monthly` (value: `"monthly"`)

* `everyOtherMonth` (value: `"everyOtherMonth"`)

* `every3Months` (value: `"every3Months"`)

* `every4Months` (value: `"every4Months"`)

* `twiceAYear` (value: `"twiceAYear"`)

* `yearly` (value: `"yearly"`)

* `everyOtherYear` (value: `"everyOtherYear"`)




