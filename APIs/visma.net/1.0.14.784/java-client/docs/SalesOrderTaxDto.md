

# SalesOrderTaxDto

The Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderTaxDto specifies a tax line detail for a sales order

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exemptTax** | **Boolean** | Indicates if the taxable amount will be included in taxExemptTotal |  [optional] |
|**includeInTaxable** | **Boolean** | Indicates if the taxable amount will be included in taxableTotal |  [optional] |
|**isPendingTax** | **Boolean** | Indicates if the tax calculated is treated as a pending tax |  [optional] |
|**isReverseTax** | **Boolean** | Indicates if the tax is treated as a reverse tax |  [optional] |
|**isStatisticalTax** | **Boolean** | Indicates if the tax calculated is treated as a statistical tax |  [optional] |
|**taxAmount** | **Double** | The calculated tax amount for the specific tax |  [optional] |
|**taxId** | **String** | The unique tax identifier of the specific tax applied to the document |  [optional] |
|**taxRate** | **Double** | The tax rate used for the tax |  [optional] |
|**taxType** | **String** | The type of tax, which can be Sales, Use, VAT or Withholding |  [optional] |
|**taxableAmount** | **Double** | The calculated taxable amount for the specific tax |  [optional] |



