

# CustomerInvoiceDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyId** | **Long** |  |  [optional] |
|**customerDetails** | [**CustomerDetailsDTO**](CustomerDetailsDTO.md) |  |  [optional] |
|**customerId** | **Long** |  |  [optional] |
|**dates** | [**CustomerInvoiceDatesDTO**](CustomerInvoiceDatesDTO.md) |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**invoiceNumber** | **String** |  |  [optional] |
|**paymentMethodId** | **Long** |  |  [optional] |
|**paymentTerms** | [**PaymentTermsDTO**](PaymentTermsDTO.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tasks** | [**List&lt;TaskDTO&gt;**](TaskDTO.md) |  |  [optional] |
|**tasksValue** | **BigDecimal** |  |  [optional] |
|**totalGross** | **BigDecimal** |  |  [optional] |
|**totalInWords** | **String** |  |  [optional] |
|**totalNetto** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**vatCalculationRule** | [**VatCalculationRuleEnum**](#VatCalculationRuleEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_READY | &quot;NOT_READY&quot; |
| READY | &quot;READY&quot; |
| SENT | &quot;SENT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FINAL | &quot;FINAL&quot; |
| DRAFT | &quot;DRAFT&quot; |
| CREDIT_NOTE | &quot;CREDIT_NOTE&quot; |



## Enum: VatCalculationRuleEnum

| Name | Value |
|---- | -----|
| SUM_ITEMS | &quot;SUM_ITEMS&quot; |
| BY_NET_TOTAL | &quot;BY_NET_TOTAL&quot; |



