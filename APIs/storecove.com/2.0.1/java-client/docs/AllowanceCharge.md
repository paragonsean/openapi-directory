

# AllowanceCharge


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountExcludingTax** | **BigDecimal** | The amount for the allowance or charge, excluding tax. |  [optional] |
|**amountExcludingVat** | **BigDecimal** | DEPRECATED. Use amountExcludingTax. The amount for the allowance or charge, excluding VAT. |  [optional] |
|**amountIncludingTax** | **BigDecimal** | The amount for the allowance or charge, including tax. |  [optional] |
|**baseAmountExcludingTax** | **BigDecimal** | The base amount for the allowance or charge, excluding tax. |  [optional] |
|**baseAmountIncludingTax** | **BigDecimal** | The base amount for the allowance or charge, including tax. |  [optional] |
|**reason** | **String** | The reason for the allowance or charge, free text |  [optional] |
|**reasonCode** | **String** | Do not use. Contact Storecove first if you want to use this field. |  [optional] |
|**tax** | [**Tax**](Tax.md) |  |  [optional] |
|**taxesDutiesFees** | [**List&lt;Tax&gt;**](Tax.md) | An array of taxes, duties and fees for this invoice line. At this moment, multiple Tax items is allowed only for IN (India) and US (USA) taxes. All other countries can only have a single Tax item in this array. |  [optional] |



