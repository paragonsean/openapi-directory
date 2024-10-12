

# CommonSubscriptionOrder


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
|**items** | [**List&lt;CommonSubscriptionItemsInner&gt;**](CommonSubscriptionItemsInner.md) |  |  [optional] |
|**orderType** | [**OrderTypeEnum**](#OrderTypeEnum) | Specifies the type of order, a subscription or a one-time purchase.  |  [optional] |
|**poNumber** | **String** | Purchase order number, will be displayed on the issued invoices. |  [optional] |
|**recentInvoiceId** | **String** | Most recently issued invoice identifier string. It might not be &#x60;paid&#x60; yet. |  [optional] [readonly] |
|**voidTime** | **OffsetDateTime** | Order void time. |  [optional] [readonly] |
|**websiteId** | **String** | The website identifier string. |  [optional] |
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



