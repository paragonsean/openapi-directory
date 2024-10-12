# PosApi.OrderTendersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** |  | [optional] 
**buyerTenderedCashAmount** | **Number** | The amount (in cents) of cash tendered by the buyer. Only applicable when the tender type is cash. | [optional] 
**card** | [**PaymentCard**](PaymentCard.md) |  | [optional] 
**cardEntryMethod** | **String** | The entry method of the card. Only applicable when the tender type is card. | [optional] 
**cardStatus** | **String** | The status of the card. Only applicable when the tender type is card. | [optional] 
**changeBackCashAmount** | **Number** | The amount (in cents) of cash returned to the buyer. Only applicable when the tender type is cash. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**locationId** | **String** | A unique identifier for an object. | [optional] [readonly] 
**name** | **String** |  | [optional] 
**note** | **String** |  | [optional] 
**paymentId** | **String** | A unique identifier for an object. | [optional] [readonly] 
**percentage** | **Number** |  | [optional] 
**totalAmount** | **Number** |  | [optional] 
**totalDiscount** | **Number** |  | [optional] 
**totalProcessingFee** | **Number** |  | [optional] 
**totalRefund** | **Number** |  | [optional] 
**totalServiceCharge** | **Number** |  | [optional] 
**totalTax** | **Number** |  | [optional] 
**totalTip** | **Number** |  | [optional] 
**transactionId** | **String** | A unique identifier for an object. | [optional] [readonly] 
**type** | **String** |  | [optional] 



## Enum: CardEntryMethodEnum


* `evm` (value: `"evm"`)

* `swiped` (value: `"swiped"`)

* `keyed` (value: `"keyed"`)

* `on-file` (value: `"on-file"`)

* `contactless` (value: `"contactless"`)





## Enum: CardStatusEnum


* `authorized` (value: `"authorized"`)

* `captured` (value: `"captured"`)

* `failed` (value: `"failed"`)

* `voided` (value: `"voided"`)





## Enum: TypeEnum


* `cash` (value: `"cash"`)

* `card` (value: `"card"`)

* `other` (value: `"other"`)




