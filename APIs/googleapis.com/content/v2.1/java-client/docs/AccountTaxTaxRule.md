

# AccountTaxTaxRule

Tax calculation rule to apply in a state or province (US only).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | Country code in which tax is applicable. |  [optional] |
|**locationId** | **String** | Required. State (or province) is which the tax is applicable, described by its location ID (also called criteria ID). |  [optional] |
|**ratePercent** | **String** | Explicit tax rate in percent, represented as a floating point number without the percentage character. Must not be negative. |  [optional] |
|**shippingTaxed** | **Boolean** | If true, shipping charges are also taxed. |  [optional] |
|**useGlobalRate** | **Boolean** | Whether the tax rate is taken from a global tax table or specified explicitly. |  [optional] |



