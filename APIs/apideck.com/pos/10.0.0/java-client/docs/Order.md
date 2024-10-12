

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedDate** | **LocalDate** |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**customerId** | **String** |  |  [optional] |
|**customers** | [**List&lt;OrderCustomersInner&gt;**](OrderCustomersInner.md) |  |  [optional] |
|**discounts** | [**List&lt;OrderDiscountsInner&gt;**](OrderDiscountsInner.md) |  |  [optional] |
|**employeeId** | **String** |  |  [optional] |
|**fulfillments** | [**List&lt;OrderFulfillmentsInner&gt;**](OrderFulfillmentsInner.md) |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this request among requests you have sent. |  [optional] |
|**lineItems** | [**List&lt;OrderLineItemsInner&gt;**](OrderLineItemsInner.md) |  |  [optional] |
|**locationId** | **String** |  |  |
|**merchantId** | **String** |  |  |
|**note** | **String** | A note with information about this order, may be printed on the order receipt and displayed in apps |  [optional] |
|**orderDate** | **LocalDate** |  |  [optional] |
|**orderNumber** | **String** |  |  [optional] |
|**orderTypeId** | **String** |  |  [optional] |
|**paymentStatus** | [**PaymentStatusEnum**](#PaymentStatusEnum) | Is this order paid or not? |  [optional] |
|**payments** | [**List&lt;OrderPaymentsInner&gt;**](OrderPaymentsInner.md) |  |  [optional] |
|**referenceId** | **String** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. |  [optional] |
|**refunded** | **Boolean** |  |  [optional] |
|**refunds** | [**List&lt;OrderRefundsInner&gt;**](OrderRefundsInner.md) |  |  [optional] |
|**seat** | **String** |  |  [optional] |
|**serviceCharges** | [**List&lt;ServiceCharge&gt;**](ServiceCharge.md) | Optional service charges or gratuity tip applied to the order. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | Source of order. Indicates the way that the order was placed. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to &#39;open&#39;. More info [https://docs.clover.com/reference/orderupdateorder]() |  [optional] |
|**table** | **String** |  |  [optional] |
|**taxes** | [**List&lt;OrderTaxesInner&gt;**](OrderTaxesInner.md) |  |  [optional] |
|**tenders** | [**List&lt;OrderTendersInner&gt;**](OrderTendersInner.md) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**totalAmount** | **Integer** |  |  [optional] |
|**totalDiscount** | **Integer** |  |  [optional] |
|**totalRefund** | **Integer** |  |  [optional] |
|**totalServiceCharge** | **Integer** |  |  [optional] |
|**totalTax** | **Integer** |  |  [optional] |
|**totalTip** | **Integer** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**version** | **String** |  |  [optional] |
|**voided** | **Boolean** |  |  [optional] |
|**voidedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: PaymentStatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| PAID | &quot;paid&quot; |
| REFUNDED | &quot;refunded&quot; |
| CREDITED | &quot;credited&quot; |
| PARTIALLY_PAID | &quot;partially_paid&quot; |
| PARTIALLY_REFUNDED | &quot;partially_refunded&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| IN_STORE | &quot;in-store&quot; |
| ONLINE | &quot;online&quot; |
| OPT | &quot;opt&quot; |
| API | &quot;api&quot; |
| KIOSK | &quot;kiosk&quot; |
| CALLER_ID | &quot;caller-id&quot; |
| GOOGLE | &quot;google&quot; |
| INVOICE | &quot;invoice&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| DRAFT | &quot;draft&quot; |
| DELIVERED | &quot;delivered&quot; |
| DELAYED | &quot;delayed&quot; |
| VOIDED | &quot;voided&quot; |
| COMPLETED | &quot;completed&quot; |
| HIDDEN | &quot;hidden&quot; |



