

# GetSettlementIn


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region&#39;s currency code. |  [optional] |
|**endMonth** | **String** | Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. |  [optional] |
|**format** | **String** | Output format. &#39;csv&#39; value is accepted as well |  [optional] |
|**mossCountryCode** | **String** | MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code. |  [optional] |
|**mossTaxId** | **String** | MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. |  [optional] |
|**refundDateKindOverride** | **String** | Set to &#39;order_date&#39; to show only refunds for the transactions in the selected reporting period. Set to &#39;refund_timestamp&#39; to show refunds that were created in the selected reporting period. Do not set to use the default region&#39;s setting. |  [optional] |
|**startMonth** | **String** | Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. |  [optional] |
|**taxCountryCode** | **String** | Tax entity country code, used to determine currency/region.  |  [optional] |
|**taxId** | **String** | MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. |  [optional] |



