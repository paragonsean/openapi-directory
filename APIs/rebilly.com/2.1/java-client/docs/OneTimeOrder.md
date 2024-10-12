

# OneTimeOrder


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
|**status** | [**StatusEnum**](#StatusEnum) | One-time order status. |  [optional] [readonly] |
|**embedded** | [**List&lt;SubscriptionMetadataEmbeddedInner&gt;**](SubscriptionMetadataEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;SubscriptionMetadataLinksInner&gt;**](SubscriptionMetadataLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Order created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**revision** | **Integer** | The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  |  [optional] [readonly] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token. |  [optional] |
|**updatedTime** | **OffsetDateTime** | Order updated time. |  [optional] [readonly] |
|**customerId** | **String** | The customer identifier string. |  |



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
| COMPLETED | &quot;completed&quot; |
| ABANDONED | &quot;abandoned&quot; |



