

# TaxSubtotal

The total amount of tax of this type in the invoice.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The tax category. For a description see &lt;&lt;_openapi_tax&gt;&gt; |  [optional] |
|**country** | **Country** |  |  |
|**percentage** | **BigDecimal** | The tax percentage. This should be a valid tax percentage in the country at the time of the taxpointDate of this invoice. |  |
|**taxAmount** | **BigDecimal** | The amount of tax. |  |
|**taxableAmount** | **BigDecimal** | The amount on which the tax is levied. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| ZERO_RATED | &quot;zero_rated&quot; |
| REVERSE_CHARGE | &quot;reverse_charge&quot; |
| INTRA_COMMUNITY | &quot;intra_community&quot; |
| EXEMPT | &quot;exempt&quot; |
| EXPORT | &quot;export&quot; |
| OUTSIDE_SCOPE | &quot;outside_scope&quot; |
| REGULATION33_EXEMPT | &quot;regulation33_exempt&quot; |
| NONREGULATION33_EXEMPT | &quot;nonregulation33_exempt&quot; |
| DEEMED_SUPPLY | &quot;deemed_supply&quot; |
| SRCA_S | &quot;srca_s&quot; |
| SRCA_C | &quot;srca_c&quot; |
| NOT_REGISTERED | &quot;not_registered&quot; |
| IGST | &quot;igst&quot; |
| CGST | &quot;cgst&quot; |
| SGST | &quot;sgst&quot; |
| CESS | &quot;cess&quot; |
| STATE_CESS | &quot;state_cess&quot; |
| SROVR | &quot;srovr&quot; |
| SROVR_RS | &quot;srovr_rs&quot; |
| SROVR_LVG | &quot;srovr_lvg&quot; |
| SRLVG | &quot;srlvg&quot; |



