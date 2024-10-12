

# SubscriptionCancellation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**appliedInvoiceId** | **String** | The identifier of the invoice where the cancellation fees or credits are applied. |  [optional] [readonly] |
|**canceledBy** | [**CanceledByEnum**](#CanceledByEnum) | Who did the cancellation. |  [optional] |
|**canceledTime** | **OffsetDateTime** | The cancellation time (when the status is confirmed which is by default unless specified \&quot;draft\&quot;). |  [optional] [readonly] |
|**churnTime** | **OffsetDateTime** | The time when the subscription will be deactivated. |  |
|**createdTime** | **OffsetDateTime** | The time of resource creation (when it is posted). |  [optional] [readonly] |
|**description** | **String** | Cancel reason description in free form. |  [optional] |
|**id** | **String** | Cancellation identifier. |  [optional] [readonly] |
|**lineItemSubtotal** | **BigDecimal** | Subtotal of the line items which will be added after the subscription&#39;s cancellation. |  [optional] [readonly] |
|**lineItems** | [**List&lt;UpcomingInvoiceItem&gt;**](UpcomingInvoiceItem.md) | Items to be added to the new invoice. Proration item is generated and added automatically. |  [optional] |
|**prorated** | **Boolean** | Defines if the customer gets a pro-rata credit for the time remaining between &#x60;churnTime&#x60; and subscription&#39;s next renewal time.  |  [optional] |
|**proratedInvoiceId** | **String** | Identifier of the invoice on which the cancellation proration is calculated. |  [optional] [readonly] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Cancellation reason. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | \&quot;draft\&quot; defines that the cancellation isn&#39;t applied on an invoice and subscription but can be inspected to see the charge. \&quot;confirmed\&quot; will set a subscription to be canceled when the &#x60;churnTime&#x60; is reached. \&quot;completed\&quot; is a read-only status which is set by the system when the churnTime is reached. The cancellation may not be changed or deleted when the status is \&quot;completed\&quot;.  |  [optional] |
|**subscriptionId** | **String** | Identifier of the canceled subscription order. |  |



## Enum: CanceledByEnum

| Name | Value |
|---- | -----|
| MERCHANT | &quot;merchant&quot; |
| CUSTOMER | &quot;customer&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| DID_NOT_USE | &quot;did-not-use&quot; |
| DID_NOT_WANT | &quot;did-not-want&quot; |
| MISSING_FEATURES | &quot;missing-features&quot; |
| BUGS_OR_PROBLEMS | &quot;bugs-or-problems&quot; |
| DO_NOT_REMEMBER | &quot;do-not-remember&quot; |
| RISK_WARNING | &quot;risk-warning&quot; |
| CONTRACT_EXPIRED | &quot;contract-expired&quot; |
| TOO_EXPENSIVE | &quot;too-expensive&quot; |
| OTHER | &quot;other&quot; |
| BILLING_FAILURE | &quot;billing-failure&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| CONFIRMED | &quot;confirmed&quot; |
| COMPLETED | &quot;completed&quot; |
| REVOKED | &quot;revoked&quot; |



