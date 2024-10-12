

# Model

The model that describes the cost and pricing for apps

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingPeriod** | [**BillingPeriodEnum**](#BillingPeriodEnum) | The billingPeriod along with the billingPeriodUnit make up the time between billing cycles |  [optional] |
|**billingPeriodUnit** | **Integer** | The billingPeriod along with the billingPeriodUnit make up the time between billing cycles |  [optional] |
|**commission** | **Integer** | The marketplace commission applied to this app&#39;s model multiplied by 100 to include two digits for fractions of a percent |  |
|**currency** | **String** | The ISO 4217 currency code for this price |  |
|**customData** | **Object** | A custom JSON object that you can create and attach to this record |  [optional] |
|**feePayer** | [**FeePayerEnum**](#FeePayerEnum) | The payee that will be paying for any payment processing fees |  |
|**license** | [**LicenseEnum**](#LicenseEnum) | The license model type. Single allows a purchase to a single user or organization |  |
|**modelId** | **String** | The id that uniquely identifies this model |  [optional] |
|**price** | **Integer** | The price of this app in cents |  |
|**subtype** | [**SubtypeEnum**](#SubtypeEnum) | The pricing model subtype |  [optional] |
|**trial** | **Integer** | The maximum number of free trial days available |  |
|**type** | [**TypeEnum**](#TypeEnum) | The pricing model type. Free has no cost, single has a one time purchase cost and recurring requires a monthly subscription |  |



## Enum: BillingPeriodEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |
| ANNUALLY | &quot;annually&quot; |



## Enum: FeePayerEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;developer&quot; |
| MARKETPLACE | &quot;marketplace&quot; |



## Enum: LicenseEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



## Enum: SubtypeEnum

| Name | Value |
|---- | -----|
| USAGE | &quot;usage&quot; |
| SEAT | &quot;seat&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FREE | &quot;free&quot; |
| SINGLE | &quot;single&quot; |
| RECURRING | &quot;recurring&quot; |



