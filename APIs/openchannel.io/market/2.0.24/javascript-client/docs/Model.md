# OpenChannelMarketApi.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingPeriod** | **String** | The billingPeriod along with the billingPeriodUnit make up the time between billing cycles | [optional] 
**billingPeriodUnit** | **Number** | The billingPeriod along with the billingPeriodUnit make up the time between billing cycles | [optional] 
**commission** | **Number** | The marketplace commission applied to this app&#39;s model multiplied by 100 to include two digits for fractions of a percent | 
**currency** | **String** | The ISO 4217 currency code for this price | 
**customData** | **Object** | A custom JSON object that you can create and attach to this record | [optional] 
**feePayer** | **String** | The payee that will be paying for any payment processing fees | 
**license** | **String** | The license model type. Single allows a purchase to a single user or organization | 
**modelId** | **String** | The id that uniquely identifies this model | [optional] 
**price** | **Number** | The price of this app in cents | 
**subtype** | **String** | The pricing model subtype | [optional] 
**trial** | **Number** | The maximum number of free trial days available | 
**type** | **String** | The pricing model type. Free has no cost, single has a one time purchase cost and recurring requires a monthly subscription | 



## Enum: BillingPeriodEnum


* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `monthly` (value: `"monthly"`)

* `annually` (value: `"annually"`)





## Enum: FeePayerEnum


* `developer` (value: `"developer"`)

* `marketplace` (value: `"marketplace"`)





## Enum: LicenseEnum


* `single` (value: `"single"`)





## Enum: SubtypeEnum


* `usage` (value: `"usage"`)

* `seat` (value: `"seat"`)





## Enum: TypeEnum


* `free` (value: `"free"`)

* `single` (value: `"single"`)

* `recurring` (value: `"recurring"`)




