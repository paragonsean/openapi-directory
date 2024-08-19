# RocketServices.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The unique subscription code. | 
**endDate** | **Date** | The end date of a subscription.  After this date the subscription will become expired. If this is a recurring subscription which has not been cancelled then the account holder will be automatically charged and a new subscription will be activated.  Some subscriptions may not have an end date, in which case this property will not exist.  | [optional] 
**id** | **String** | Unique identifier for the subscription. | [optional] 
**isTrialPeriod** | **Boolean** | True if a subscription is in its trial period, false if not. | 
**planId** | **String** | The plan a subscription belongs to. | 
**startDate** | **Date** | The start date of a subscription. | 
**status** | **String** | The status of a subscription. | 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Cancelled` (value: `"Cancelled"`)

* `Lapsed` (value: `"Lapsed"`)

* `Expired` (value: `"Expired"`)

* `None` (value: `"None"`)




