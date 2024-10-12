# StorecoveApi.TaxSubtotal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The tax category. For a description see &lt;&lt;_openapi_tax&gt;&gt; | [optional] 
**country** | [**Country**](Country.md) |  | 
**percentage** | **Number** | The tax percentage. This should be a valid tax percentage in the country at the time of the taxpointDate of this invoice. | 
**taxAmount** | **Number** | The amount of tax. | 
**taxableAmount** | **Number** | The amount on which the tax is levied. | 



## Enum: CategoryEnum


* `standard` (value: `"standard"`)

* `zero_rated` (value: `"zero_rated"`)

* `reverse_charge` (value: `"reverse_charge"`)

* `intra_community` (value: `"intra_community"`)

* `exempt` (value: `"exempt"`)

* `export` (value: `"export"`)

* `outside_scope` (value: `"outside_scope"`)

* `regulation33_exempt` (value: `"regulation33_exempt"`)

* `nonregulation33_exempt` (value: `"nonregulation33_exempt"`)

* `deemed_supply` (value: `"deemed_supply"`)

* `srca_s` (value: `"srca_s"`)

* `srca_c` (value: `"srca_c"`)

* `not_registered` (value: `"not_registered"`)

* `igst` (value: `"igst"`)

* `cgst` (value: `"cgst"`)

* `sgst` (value: `"sgst"`)

* `cess` (value: `"cess"`)

* `state_cess` (value: `"state_cess"`)

* `srovr` (value: `"srovr"`)

* `srovr_rs` (value: `"srovr_rs"`)

* `srovr_lvg` (value: `"srovr_lvg"`)

* `srlvg` (value: `"srlvg"`)




