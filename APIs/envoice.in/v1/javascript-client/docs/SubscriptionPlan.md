# ApiV100.SubscriptionPlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellatedOn** | **Date** |  | [optional] 
**couponCode** | **String** |  | [optional] 
**currencyCode** | **String** |  | [optional] 
**externalIdentifier** | **String** |  | [optional] 
**features** | **[String]** |  | [optional] 
**hasDuePayment** | **Boolean** |  | [optional] 
**hasDuePaymentSince** | **Date** |  | [optional] 
**id** | **Number** |  | [optional] 
**identifier** | **String** |  | [optional] 
**isActive** | **Boolean** |  | [optional] 
**isLifetime** | **Boolean** |  | [optional] 
**lastPaymentOn** | **Date** |  | [optional] 
**maxClients** | **Number** |  | [optional] 
**name** | **String** |  | [optional] 
**onHold** | **Boolean** |  | [optional] 
**orderIdentifier** | **String** |  | [optional] 
**price** | **Number** |  | [optional] 
**recurrence** | **String** |  | [optional] 
**saleId** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**systemCancelationReason** | **String** |  | [optional] 
**trialEndsOn** | **Date** |  | [optional] 
**trialNumberOfDays** | **Number** |  | [optional] 
**trialStartsOn** | **Date** |  | [optional] 
**userId** | **Number** |  | [optional] 
**version** | **Number** |  | [optional] 



## Enum: [FeaturesEnum]


* `Api` (value: `"Api"`)

* `Teams` (value: `"Teams"`)

* `Clients` (value: `"Clients"`)

* `Shop` (value: `"Shop"`)

* `PaymentLinks` (value: `"PaymentLinks"`)

* `Cname` (value: `"Cname"`)





## Enum: RecurrenceEnum


* `Monthly` (value: `"Monthly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: StatusEnum


* `ActiveTrial` (value: `"ActiveTrial"`)

* `ExpiredTrial` (value: `"ExpiredTrial"`)

* `Active` (value: `"Active"`)

* `Canceled` (value: `"Canceled"`)

* `Fraudlent` (value: `"Fraudlent"`)





## Enum: SystemCancelationReasonEnum


* `FailToCaptureFee` (value: `"FailToCaptureFee"`)

* `Fraud` (value: `"Fraud"`)




