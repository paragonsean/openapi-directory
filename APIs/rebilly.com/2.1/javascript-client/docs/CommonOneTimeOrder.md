# RebillyRestApi.CommonOneTimeOrder

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
**items** | [**[CommonSubscriptionItemsInner]**](CommonSubscriptionItemsInner.md) |  | [optional] 
**orderType** | **String** | Specifies the type of order, a subscription or a one-time purchase.  | [optional] [default to &#39;subscription-order&#39;]
**poNumber** | **String** | Purchase order number, will be displayed on the issued invoices. | [optional] 
**recentInvoiceId** | **String** | Most recently issued invoice identifier string. It might not be &#x60;paid&#x60; yet. | [optional] [readonly] 
**voidTime** | **Date** | Order void time. | [optional] [readonly] 
**websiteId** | **String** | The website identifier string. | [optional] 
**status** | **String** | One-time order status. | [optional] [readonly] 



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

* `completed` (value: `"completed"`)

* `abandoned` (value: `"abandoned"`)




