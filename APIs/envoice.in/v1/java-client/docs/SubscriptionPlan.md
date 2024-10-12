

# SubscriptionPlan


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellatedOn** | **OffsetDateTime** |  |  [optional] |
|**couponCode** | **String** |  |  [optional] |
|**currencyCode** | **String** |  |  [optional] |
|**externalIdentifier** | **String** |  |  [optional] |
|**features** | [**List&lt;FeaturesEnum&gt;**](#List&lt;FeaturesEnum&gt;) |  |  [optional] |
|**hasDuePayment** | **Boolean** |  |  [optional] |
|**hasDuePaymentSince** | **OffsetDateTime** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**identifier** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**isLifetime** | **Boolean** |  |  [optional] |
|**lastPaymentOn** | **OffsetDateTime** |  |  [optional] |
|**maxClients** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**onHold** | **Boolean** |  |  [optional] |
|**orderIdentifier** | **String** |  |  [optional] |
|**price** | **Double** |  |  [optional] |
|**recurrence** | [**RecurrenceEnum**](#RecurrenceEnum) |  |  [optional] |
|**saleId** | **Long** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**systemCancelationReason** | [**SystemCancelationReasonEnum**](#SystemCancelationReasonEnum) |  |  [optional] |
|**trialEndsOn** | **OffsetDateTime** |  |  [optional] |
|**trialNumberOfDays** | **Integer** |  |  [optional] |
|**trialStartsOn** | **OffsetDateTime** |  |  [optional] |
|**userId** | **Integer** |  |  [optional] |
|**version** | **Integer** |  |  [optional] |



## Enum: List&lt;FeaturesEnum&gt;

| Name | Value |
|---- | -----|
| API | &quot;Api&quot; |
| TEAMS | &quot;Teams&quot; |
| CLIENTS | &quot;Clients&quot; |
| SHOP | &quot;Shop&quot; |
| PAYMENT_LINKS | &quot;PaymentLinks&quot; |
| CNAME | &quot;Cname&quot; |



## Enum: RecurrenceEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;Monthly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE_TRIAL | &quot;ActiveTrial&quot; |
| EXPIRED_TRIAL | &quot;ExpiredTrial&quot; |
| ACTIVE | &quot;Active&quot; |
| CANCELED | &quot;Canceled&quot; |
| FRAUDLENT | &quot;Fraudlent&quot; |



## Enum: SystemCancelationReasonEnum

| Name | Value |
|---- | -----|
| FAIL_TO_CAPTURE_FEE | &quot;FailToCaptureFee&quot; |
| FRAUD | &quot;Fraud&quot; |



