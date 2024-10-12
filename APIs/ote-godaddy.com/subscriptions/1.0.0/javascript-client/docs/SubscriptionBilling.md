# OpenapiJsClient.SubscriptionBilling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment** | **String** | The financial commitment the customer has in the product | 
**pastDueTypes** | **[String]** | The types of charges that are past due when &#x60;status&#x60; is PAST_DUE | [optional] 
**renewAt** | **String** | The point in time after which the Subscription will bill for automatic renewal | 
**status** | **String** | Whether payments are past due | 



## Enum: CommitmentEnum


* `PAID` (value: `"PAID"`)

* `FREE` (value: `"FREE"`)

* `TRIAL` (value: `"TRIAL"`)





## Enum: [PastDueTypesEnum]


* `ADDON` (value: `"ADDON"`)

* `BURST` (value: `"BURST"`)

* `SUBSCRIPTION` (value: `"SUBSCRIPTION"`)





## Enum: StatusEnum


* `CURRENT` (value: `"CURRENT"`)

* `PAST_DUE` (value: `"PAST_DUE"`)




