# PosApi.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closedDate** | **Date** |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customerId** | **String** |  | [optional] 
**customers** | [**[OrderCustomersInner]**](OrderCustomersInner.md) |  | [optional] 
**discounts** | [**[OrderDiscountsInner]**](OrderDiscountsInner.md) |  | [optional] 
**employeeId** | **String** |  | [optional] 
**fulfillments** | [**[OrderFulfillmentsInner]**](OrderFulfillmentsInner.md) |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**idempotencyKey** | **String** | A value you specify that uniquely identifies this request among requests you have sent. | [optional] 
**lineItems** | [**[OrderLineItemsInner]**](OrderLineItemsInner.md) |  | [optional] 
**locationId** | **String** |  | 
**merchantId** | **String** |  | 
**note** | **String** | A note with information about this order, may be printed on the order receipt and displayed in apps | [optional] 
**orderDate** | **Date** |  | [optional] 
**orderNumber** | **String** |  | [optional] 
**orderTypeId** | **String** |  | [optional] 
**paymentStatus** | **String** | Is this order paid or not? | [optional] 
**payments** | [**[OrderPaymentsInner]**](OrderPaymentsInner.md) |  | [optional] 
**referenceId** | **String** | An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system. | [optional] 
**refunded** | **Boolean** |  | [optional] 
**refunds** | [**[OrderRefundsInner]**](OrderRefundsInner.md) |  | [optional] 
**seat** | **String** |  | [optional] 
**serviceCharges** | [**[ServiceCharge]**](ServiceCharge.md) | Optional service charges or gratuity tip applied to the order. | [optional] 
**source** | **String** | Source of order. Indicates the way that the order was placed. | [optional] [readonly] 
**status** | **String** | Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to &#39;open&#39;. More info [https://docs.clover.com/reference/orderupdateorder]() | [optional] 
**table** | **String** |  | [optional] 
**taxes** | [**[OrderTaxesInner]**](OrderTaxesInner.md) |  | [optional] 
**tenders** | [**[OrderTendersInner]**](OrderTendersInner.md) |  | [optional] 
**title** | **String** |  | [optional] 
**totalAmount** | **Number** |  | [optional] 
**totalDiscount** | **Number** |  | [optional] 
**totalRefund** | **Number** |  | [optional] 
**totalServiceCharge** | **Number** |  | [optional] 
**totalTax** | **Number** |  | [optional] 
**totalTip** | **Number** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**version** | **String** |  | [optional] 
**voided** | **Boolean** |  | [optional] 
**voidedAt** | **Date** |  | [optional] [readonly] 



## Enum: PaymentStatusEnum


* `open` (value: `"open"`)

* `paid` (value: `"paid"`)

* `refunded` (value: `"refunded"`)

* `credited` (value: `"credited"`)

* `partially_paid` (value: `"partially_paid"`)

* `partially_refunded` (value: `"partially_refunded"`)

* `unknown` (value: `"unknown"`)





## Enum: SourceEnum


* `in-store` (value: `"in-store"`)

* `online` (value: `"online"`)

* `opt` (value: `"opt"`)

* `api` (value: `"api"`)

* `kiosk` (value: `"kiosk"`)

* `caller-id` (value: `"caller-id"`)

* `google` (value: `"google"`)

* `invoice` (value: `"invoice"`)





## Enum: StatusEnum


* `open` (value: `"open"`)

* `draft` (value: `"draft"`)

* `delivered` (value: `"delivered"`)

* `delayed` (value: `"delayed"`)

* `voided` (value: `"voided"`)

* `completed` (value: `"completed"`)

* `hidden` (value: `"hidden"`)




