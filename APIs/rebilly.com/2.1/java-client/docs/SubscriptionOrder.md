

# SubscriptionOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationTime** | **OffsetDateTime** | Order activation time. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | Order billing address. |  [optional] |
|**billingStatus** | [**BillingStatusEnum**](#BillingStatusEnum) | The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service.  |  [optional] [readonly] |
|**couponIds** | **List&lt;String&gt;** | A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued.  |  [optional] |
|**deliveryAddress** | [**ContactObject**](ContactObject.md) | Order delivery address. |  [optional] |
|**id** | **String** | The order identifier string. |  [optional] [readonly] |
|**initialInvoiceId** | **String** | The initial invoice identifier string. |  [optional] [readonly] |
|**items** | [**List&lt;CommonSubscriptionItemsInner&gt;**](CommonSubscriptionItemsInner.md) |  |  |
|**orderType** | [**OrderTypeEnum**](#OrderTypeEnum) | Specifies the type of order, a subscription or a one-time purchase.  |  |
|**poNumber** | **String** | Purchase order number, will be displayed on the issued invoices. |  [optional] |
|**recentInvoiceId** | **String** | Most recently issued invoice identifier string. It might not be &#x60;paid&#x60; yet. |  [optional] [readonly] |
|**voidTime** | **OffsetDateTime** | Order void time. |  [optional] [readonly] |
|**websiteId** | **String** | The website identifier string. |  |
|**autopay** | **Boolean** | Autopay determines if a payment attempt will be automatic. |  [optional] |
|**endTime** | **OffsetDateTime** | Subscription end time. |  [optional] [readonly] |
|**inTrial** | **Boolean** | True if the subscription is currently in a trial period. |  [optional] [readonly] |
|**invoiceTimeShift** | [**InvoiceTimeShift**](InvoiceTimeShift.md) | You can shift issue time and due time of invoices for this subscription. This setting overrides plan settings. To use plan settings, set &#x60;null&#x60;. To use multiple plans in one subscription they all must have the same billing period, this property allows to subscribe to different plans.  |  [optional] |
|**isTrialOnly** | **Boolean** | Whether a subscription ends after a trial period. Recurring settings are ignored if it&#39;s &#x60;true&#x60;. |  [optional] |
|**lineItemSubtotal** | [**CommonSubscriptionOrderAllOfLineItemSubtotal**](CommonSubscriptionOrderAllOfLineItemSubtotal.md) |  |  [optional] |
|**lineItems** | [**List&lt;UpcomingInvoiceItem&gt;**](UpcomingInvoiceItem.md) | Subscription line items which queue until the next renewal (or interim) invoice is issued for the subscription. |  [optional] [readonly] |
|**rebillNumber** | **Integer** | The current period number. |  [optional] [readonly] |
|**recurringInterval** | [**CommonSubscriptionOrderAllOfRecurringInterval**](CommonSubscriptionOrderAllOfRecurringInterval.md) |  |  [optional] |
|**renewalTime** | **OffsetDateTime** | Subscription renewal time. |  [optional] |
|**startTime** | **OffsetDateTime** | Subscription start time.  When the value is sent as null, it will use the current time. This value can&#39;t be in past more than one service period. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the subscription service. A subscription starts in the &#x60;pending&#x60; status, and will become &#x60;active&#x60; when the service period begins.  |  [optional] [readonly] |
|**trial** | [**CommonSubscriptionOrderAllOfTrial**](CommonSubscriptionOrderAllOfTrial.md) |  |  [optional] |
|**cancelCategory** | [**CancelCategoryEnum**](#CancelCategoryEnum) | Cancel category. |  [optional] [readonly] |
|**cancelDescription** | **String** | Cancel reason description in free form. |  [optional] [readonly] |
|**canceledBy** | [**CanceledByEnum**](#CanceledByEnum) | Canceled by. |  [optional] [readonly] |
|**canceledTime** | **OffsetDateTime** | Subscription order canceled time. |  [optional] [readonly] |
|**embedded** | [**List&lt;SubscriptionMetadataEmbeddedInner&gt;**](SubscriptionMetadataEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;SubscriptionMetadataLinksInner&gt;**](SubscriptionMetadataLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Order created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**revision** | **Integer** | The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  |  [optional] [readonly] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token. |  [optional] |
|**updatedTime** | **OffsetDateTime** | Order updated time. |  [optional] [readonly] |
|**customerId** | **String** | The customer identifier string. |  |
|**renewalReminderNumber** | **Integer** | Number of renewal reminder events triggered. |  [optional] [readonly] |
|**renewalReminderTime** | **OffsetDateTime** | Time renewal reminder event will be triggered. |  [optional] [readonly] |
|**trialReminderNumber** | **Integer** | Number of renewal reminder events triggered. |  [optional] [readonly] |
|**trialReminderTime** | **OffsetDateTime** | Time renewal reminder event will be triggered. |  [optional] [readonly] |



## Enum: BillingStatusEnum

| Name | Value |
|---- | -----|
| UNPAID | &quot;unpaid&quot; |
| PAST_DUE | &quot;past-due&quot; |
| DELINQUENT | &quot;delinquent&quot; |
| PAID | &quot;paid&quot; |
| VOIDED | &quot;voided&quot; |
| REFUNDED | &quot;refunded&quot; |
| DISPUTED | &quot;disputed&quot; |
| VOIDED2 | &quot;voided&quot; |



## Enum: OrderTypeEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION_ORDER | &quot;subscription-order&quot; |
| ONE_TIME_ORDER | &quot;one-time-order&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |
| CANCELED | &quot;canceled&quot; |
| CHURNED | &quot;churned&quot; |
| SUSPENDED | &quot;suspended&quot; |
| PAUSED | &quot;paused&quot; |
| ABANDONED | &quot;abandoned&quot; |
| TRIAL_ENDED | &quot;trial-ended&quot; |



## Enum: CancelCategoryEnum

| Name | Value |
|---- | -----|
| BILLING_FAILURE | &quot;billing-failure&quot; |
| DID_NOT_USE | &quot;did-not-use&quot; |
| DID_NOT_WANT | &quot;did-not-want&quot; |
| MISSING_FEATURES | &quot;missing-features&quot; |
| BUGS_OR_PROBLEMS | &quot;bugs-or-problems&quot; |
| DO_NOT_REMEMBER | &quot;do-not-remember&quot; |
| RISK_WARNING | &quot;risk-warning&quot; |
| CONTRACT_EXPIRED | &quot;contract-expired&quot; |
| TOO_EXPENSIVE | &quot;too-expensive&quot; |
| NEVER_STARTED | &quot;never-started&quot; |
| SWITCHED_PLAN | &quot;switched-plan&quot; |
| OTHER | &quot;other&quot; |



## Enum: CanceledByEnum

| Name | Value |
|---- | -----|
| MERCHANT | &quot;merchant&quot; |
| CUSTOMER | &quot;customer&quot; |
| REBILLY | &quot;rebilly&quot; |



