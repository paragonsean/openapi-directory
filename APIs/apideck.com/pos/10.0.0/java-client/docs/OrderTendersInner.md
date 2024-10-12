

# OrderTendersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  [optional] |
|**buyerTenderedCashAmount** | **Integer** | The amount (in cents) of cash tendered by the buyer. Only applicable when the tender type is cash. |  [optional] |
|**card** | [**PaymentCard**](PaymentCard.md) |  |  [optional] |
|**cardEntryMethod** | [**CardEntryMethodEnum**](#CardEntryMethodEnum) | The entry method of the card. Only applicable when the tender type is card. |  [optional] |
|**cardStatus** | [**CardStatusEnum**](#CardStatusEnum) | The status of the card. Only applicable when the tender type is card. |  [optional] |
|**changeBackCashAmount** | **Integer** | The amount (in cents) of cash returned to the buyer. Only applicable when the tender type is cash. |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**locationId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**note** | **String** |  |  [optional] |
|**paymentId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**percentage** | **BigDecimal** |  |  [optional] |
|**totalAmount** | **Integer** |  |  [optional] |
|**totalDiscount** | **Integer** |  |  [optional] |
|**totalProcessingFee** | **Integer** |  |  [optional] |
|**totalRefund** | **Integer** |  |  [optional] |
|**totalServiceCharge** | **Integer** |  |  [optional] |
|**totalTax** | **Integer** |  |  [optional] |
|**totalTip** | **Integer** |  |  [optional] |
|**transactionId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: CardEntryMethodEnum

| Name | Value |
|---- | -----|
| EVM | &quot;evm&quot; |
| SWIPED | &quot;swiped&quot; |
| KEYED | &quot;keyed&quot; |
| ON_FILE | &quot;on-file&quot; |
| CONTACTLESS | &quot;contactless&quot; |



## Enum: CardStatusEnum

| Name | Value |
|---- | -----|
| AUTHORIZED | &quot;authorized&quot; |
| CAPTURED | &quot;captured&quot; |
| FAILED | &quot;failed&quot; |
| VOIDED | &quot;voided&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CASH | &quot;cash&quot; |
| CARD | &quot;card&quot; |
| OTHER | &quot;other&quot; |



