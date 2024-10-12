# RebillyRestApi.SubscriptionCancellation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**appliedInvoiceId** | **String** | The identifier of the invoice where the cancellation fees or credits are applied. | [optional] [readonly] 
**canceledBy** | **String** | Who did the cancellation. | [optional] [default to &#39;customer&#39;]
**canceledTime** | **Date** | The cancellation time (when the status is confirmed which is by default unless specified \&quot;draft\&quot;). | [optional] [readonly] 
**churnTime** | **Date** | The time when the subscription will be deactivated. | 
**createdTime** | **Date** | The time of resource creation (when it is posted). | [optional] [readonly] 
**description** | **String** | Cancel reason description in free form. | [optional] 
**id** | **String** | Cancellation identifier. | [optional] [readonly] 
**lineItemSubtotal** | **Number** | Subtotal of the line items which will be added after the subscription&#39;s cancellation. | [optional] [readonly] 
**lineItems** | [**[UpcomingInvoiceItem]**](UpcomingInvoiceItem.md) | Items to be added to the new invoice. Proration item is generated and added automatically. | [optional] 
**prorated** | **Boolean** | Defines if the customer gets a pro-rata credit for the time remaining between &#x60;churnTime&#x60; and subscription&#39;s next renewal time.  | [optional] [default to false]
**proratedInvoiceId** | **String** | Identifier of the invoice on which the cancellation proration is calculated. | [optional] [readonly] 
**reason** | **String** | Cancellation reason. | [optional] [default to &#39;other&#39;]
**status** | **String** | \&quot;draft\&quot; defines that the cancellation isn&#39;t applied on an invoice and subscription but can be inspected to see the charge. \&quot;confirmed\&quot; will set a subscription to be canceled when the &#x60;churnTime&#x60; is reached. \&quot;completed\&quot; is a read-only status which is set by the system when the churnTime is reached. The cancellation may not be changed or deleted when the status is \&quot;completed\&quot;.  | [optional] [default to &#39;confirmed&#39;]
**subscriptionId** | **String** | Identifier of the canceled subscription order. | 



## Enum: CanceledByEnum


* `merchant` (value: `"merchant"`)

* `customer` (value: `"customer"`)





## Enum: ReasonEnum


* `did-not-use` (value: `"did-not-use"`)

* `did-not-want` (value: `"did-not-want"`)

* `missing-features` (value: `"missing-features"`)

* `bugs-or-problems` (value: `"bugs-or-problems"`)

* `do-not-remember` (value: `"do-not-remember"`)

* `risk-warning` (value: `"risk-warning"`)

* `contract-expired` (value: `"contract-expired"`)

* `too-expensive` (value: `"too-expensive"`)

* `other` (value: `"other"`)

* `billing-failure` (value: `"billing-failure"`)





## Enum: StatusEnum


* `draft` (value: `"draft"`)

* `confirmed` (value: `"confirmed"`)

* `completed` (value: `"completed"`)

* `revoked` (value: `"revoked"`)




