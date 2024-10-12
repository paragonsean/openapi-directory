

# ProviderInvoiceDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyId** | **Long** |  |  [optional] |
|**dates** | [**ProviderInvoiceDatesDTO**](ProviderInvoiceDatesDTO.md) |  |  [optional] |
|**draftNumber** | **String** |  |  [optional] |
|**finalNumber** | **String** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**internalNumber** | **String** |  |  [optional] |
|**jobsNetValue** | **BigDecimal** |  |  [optional] |
|**notesFromProvider** | **String** |  |  [optional] |
|**paymentStatus** | [**PaymentStatusEnum**](#PaymentStatusEnum) |  |  [optional] |
|**providerId** | **Long** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**totalGross** | **BigDecimal** |  |  [optional] |
|**totalGrossInWords** | **String** |  |  [optional] |
|**totalNetto** | **BigDecimal** |  |  [optional] |



## Enum: PaymentStatusEnum

| Name | Value |
|---- | -----|
| NOT_PAID | &quot;NOT_PAID&quot; |
| FULLY_PAID | &quot;FULLY_PAID&quot; |
| IRRECOVERABLE | &quot;IRRECOVERABLE&quot; |
| PARTIALLY_PAID | &quot;PARTIALLY_PAID&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| POSTPONED | &quot;POSTPONED&quot; |
| TO_BE_SENT | &quot;TO_BE_SENT&quot; |
| SENT | &quot;SENT&quot; |
| CONFIRMED | &quot;CONFIRMED&quot; |
| BILL_CREATED | &quot;BILL_CREATED&quot; |



