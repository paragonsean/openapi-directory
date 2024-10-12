# StorecoveApi.AllowanceCharge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountExcludingTax** | **Number** | The amount for the allowance or charge, excluding tax. | [optional] 
**amountExcludingVat** | **Number** | DEPRECATED. Use amountExcludingTax. The amount for the allowance or charge, excluding VAT. | [optional] 
**amountIncludingTax** | **Number** | The amount for the allowance or charge, including tax. | [optional] 
**baseAmountExcludingTax** | **Number** | The base amount for the allowance or charge, excluding tax. | [optional] 
**baseAmountIncludingTax** | **Number** | The base amount for the allowance or charge, including tax. | [optional] 
**reason** | **String** | The reason for the allowance or charge, free text | [optional] [default to &#39;Agreed settlement&#39;]
**reasonCode** | **String** | Do not use. Contact Storecove first if you want to use this field. | [optional] 
**tax** | [**Tax**](Tax.md) |  | [optional] 
**taxesDutiesFees** | [**[Tax]**](Tax.md) | An array of taxes, duties and fees for this invoice line. At this moment, multiple Tax items is allowed only for IN (India) and US (USA) taxes. All other countries can only have a single Tax item in this array. | [optional] 


