# RebillyRestApi.SubscriptionOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationTime** | **Date** | Order activation time. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | Order billing address. | [optional] 
**billingStatus** | **String** | The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service.  | [optional] [readonly] 
**couponIds** | **[String]** | A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued.  | [optional] 
**deliveryAddress** | [**ContactObject**](ContactObject.md) | Order delivery address. | [optional] 
**id** | **String** | The order identifier string. | [optional] [readonly] 
**initialInvoiceId** | **String** | The initial invoice identifier string. | [optional] [readonly] 
**items** | [**[CommonSubscriptionItemsInner]**](CommonSubscriptionItemsInner.md) |  | 
**orderType** | **String** | Specifies the type of order, a subscription or a one-time purchase.  | [default to &#39;subscription-order&#39;]
**poNumber** | **String** | Purchase order number, will be displayed on the issued invoices. | [optional] 
**recentInvoiceId** | **String** | Most recently issued invoice identifier string. It might not be &#x60;paid&#x60; yet. | [optional] [readonly] 
**voidTime** | **Date** | Order void time. | [optional] [readonly] 
**websiteId** | **String** | The website identifier string. | 
**autopay** | **Boolean** | Autopay determines if a payment attempt will be automatic. | [optional] [default to true]
**endTime** | **Date** | Subscription end time. | [optional] [readonly] 
**inTrial** | **Boolean** | True if the subscription is currently in a trial period. | [optional] [readonly] 
**invoiceTimeShift** | [**InvoiceTimeShift**](InvoiceTimeShift.md) | You can shift issue time and due time of invoices for this subscription. This setting overrides plan settings. To use plan settings, set &#x60;null&#x60;. To use multiple plans in one subscription they all must have the same billing period, this property allows to subscribe to different plans.  | [optional] 
**isTrialOnly** | **Boolean** | Whether a subscription ends after a trial period. Recurring settings are ignored if it&#39;s &#x60;true&#x60;. | [optional] [default to false]
**lineItemSubtotal** | [**CommonSubscriptionOrderAllOfLineItemSubtotal**](CommonSubscriptionOrderAllOfLineItemSubtotal.md) |  | [optional] 
**lineItems** | [**[UpcomingInvoiceItem]**](UpcomingInvoiceItem.md) | Subscription line items which queue until the next renewal (or interim) invoice is issued for the subscription. | [optional] [readonly] 
**rebillNumber** | **Number** | The current period number. | [optional] [readonly] 
**recurringInterval** | [**CommonSubscriptionOrderAllOfRecurringInterval**](CommonSubscriptionOrderAllOfRecurringInterval.md) |  | [optional] 
**renewalTime** | **Date** | Subscription renewal time. | [optional] 
**startTime** | **Date** | Subscription start time.  When the value is sent as null, it will use the current time. This value can&#39;t be in past more than one service period. | [optional] 
**status** | **String** | The status of the subscription service. A subscription starts in the &#x60;pending&#x60; status, and will become &#x60;active&#x60; when the service period begins.  | [optional] [readonly] 
**trial** | [**CommonSubscriptionOrderAllOfTrial**](CommonSubscriptionOrderAllOfTrial.md) |  | [optional] 
**cancelCategory** | **String** | Cancel category. | [optional] [readonly] 
**cancelDescription** | **String** | Cancel reason description in free form. | [optional] [readonly] 
**canceledBy** | **String** | Canceled by. | [optional] [readonly] 
**canceledTime** | **Date** | Subscription order canceled time. | [optional] [readonly] 
**embedded** | [**[SubscriptionMetadataEmbeddedInner]**](SubscriptionMetadataEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[SubscriptionMetadataLinksInner]**](SubscriptionMetadataLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Order created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**revision** | **Number** | The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  | [optional] [readonly] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token. | [optional] 
**updatedTime** | **Date** | Order updated time. | [optional] [readonly] 
**customerId** | **String** | The customer identifier string. | 
**renewalReminderNumber** | **Number** | Number of renewal reminder events triggered. | [optional] [readonly] 
**renewalReminderTime** | **Date** | Time renewal reminder event will be triggered. | [optional] [readonly] 
**trialReminderNumber** | **Number** | Number of renewal reminder events triggered. | [optional] [readonly] 
**trialReminderTime** | **Date** | Time renewal reminder event will be triggered. | [optional] [readonly] 



## Enum: BillingStatusEnum


* `unpaid` (value: `"unpaid"`)

* `past-due` (value: `"past-due"`)

* `delinquent` (value: `"delinquent"`)

* `paid` (value: `"paid"`)

* `voided` (value: `"voided"`)

* `refunded` (value: `"refunded"`)

* `disputed` (value: `"disputed"`)

* `voided2` (value: `"voided"`)





## Enum: OrderTypeEnum


* `subscription-order` (value: `"subscription-order"`)

* `one-time-order` (value: `"one-time-order"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `active` (value: `"active"`)

* `canceled` (value: `"canceled"`)

* `churned` (value: `"churned"`)

* `suspended` (value: `"suspended"`)

* `paused` (value: `"paused"`)

* `abandoned` (value: `"abandoned"`)

* `trial-ended` (value: `"trial-ended"`)





## Enum: CancelCategoryEnum


* `billing-failure` (value: `"billing-failure"`)

* `did-not-use` (value: `"did-not-use"`)

* `did-not-want` (value: `"did-not-want"`)

* `missing-features` (value: `"missing-features"`)

* `bugs-or-problems` (value: `"bugs-or-problems"`)

* `do-not-remember` (value: `"do-not-remember"`)

* `risk-warning` (value: `"risk-warning"`)

* `contract-expired` (value: `"contract-expired"`)

* `too-expensive` (value: `"too-expensive"`)

* `never-started` (value: `"never-started"`)

* `switched-plan` (value: `"switched-plan"`)

* `other` (value: `"other"`)





## Enum: CanceledByEnum


* `merchant` (value: `"merchant"`)

* `customer` (value: `"customer"`)

* `rebilly` (value: `"rebilly"`)




