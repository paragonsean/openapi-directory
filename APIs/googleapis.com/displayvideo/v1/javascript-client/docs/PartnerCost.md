# DisplayVideo360Api.PartnerCost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costType** | **String** | Required. The type of the partner cost. | [optional] 
**feeAmount** | **String** | The CPM fee amount in micros of advertiser&#39;s currency. Applicable when the fee_type is &#x60;PARTNER_FEE_TYPE_CPM_FEE&#x60;. Must be greater than or equal to 0. For example, for 1.5 standard unit of the advertiser&#39;s currency, set this field to 1500000. | [optional] 
**feePercentageMillis** | **String** | The media fee percentage in millis (1/1000 of a percent). Applicable when the fee_type is &#x60;PARTNER_FEE_TYPE_MEDIA_FEE&#x60;. Must be greater than or equal to 0. For example: 100 represents 0.1%. | [optional] 
**feeType** | **String** | Required. The fee type for this partner cost. | [optional] 
**invoiceType** | **String** | The invoice type for this partner cost. * Required when cost_type is one of: - &#x60;PARTNER_COST_TYPE_ADLOOX&#x60; - &#x60;PARTNER_COST_TYPE_DOUBLE_VERIFY&#x60; - &#x60;PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE&#x60;. * Output only for other types. | [optional] 



## Enum: CostTypeEnum


* `UNSPECIFIED` (value: `"PARTNER_COST_TYPE_UNSPECIFIED"`)

* `ADLOOX` (value: `"PARTNER_COST_TYPE_ADLOOX"`)

* `ADLOOX_PREBID` (value: `"PARTNER_COST_TYPE_ADLOOX_PREBID"`)

* `ADSAFE` (value: `"PARTNER_COST_TYPE_ADSAFE"`)

* `ADXPOSE` (value: `"PARTNER_COST_TYPE_ADXPOSE"`)

* `AGGREGATE_KNOWLEDGE` (value: `"PARTNER_COST_TYPE_AGGREGATE_KNOWLEDGE"`)

* `AGENCY_TRADING_DESK` (value: `"PARTNER_COST_TYPE_AGENCY_TRADING_DESK"`)

* `DV360_FEE` (value: `"PARTNER_COST_TYPE_DV360_FEE"`)

* `COMSCORE_VCE` (value: `"PARTNER_COST_TYPE_COMSCORE_VCE"`)

* `DATA_MANAGEMENT_PLATFORM` (value: `"PARTNER_COST_TYPE_DATA_MANAGEMENT_PLATFORM"`)

* `DEFAULT` (value: `"PARTNER_COST_TYPE_DEFAULT"`)

* `DOUBLE_VERIFY` (value: `"PARTNER_COST_TYPE_DOUBLE_VERIFY"`)

* `DOUBLE_VERIFY_PREBID` (value: `"PARTNER_COST_TYPE_DOUBLE_VERIFY_PREBID"`)

* `EVIDON` (value: `"PARTNER_COST_TYPE_EVIDON"`)

* `INTEGRAL_AD_SCIENCE_VIDEO` (value: `"PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_VIDEO"`)

* `INTEGRAL_AD_SCIENCE_PREBID` (value: `"PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_PREBID"`)

* `MEDIA_COST_DATA` (value: `"PARTNER_COST_TYPE_MEDIA_COST_DATA"`)

* `MOAT_VIDEO` (value: `"PARTNER_COST_TYPE_MOAT_VIDEO"`)

* `NIELSEN_DAR` (value: `"PARTNER_COST_TYPE_NIELSEN_DAR"`)

* `SHOP_LOCAL` (value: `"PARTNER_COST_TYPE_SHOP_LOCAL"`)

* `TERACENT` (value: `"PARTNER_COST_TYPE_TERACENT"`)

* `THIRD_PARTY_AD_SERVER` (value: `"PARTNER_COST_TYPE_THIRD_PARTY_AD_SERVER"`)

* `TRUST_METRICS` (value: `"PARTNER_COST_TYPE_TRUST_METRICS"`)

* `VIZU` (value: `"PARTNER_COST_TYPE_VIZU"`)

* `ADLINGO_FEE` (value: `"PARTNER_COST_TYPE_ADLINGO_FEE"`)

* `CUSTOM_FEE_1` (value: `"PARTNER_COST_TYPE_CUSTOM_FEE_1"`)

* `CUSTOM_FEE_2` (value: `"PARTNER_COST_TYPE_CUSTOM_FEE_2"`)

* `CUSTOM_FEE_3` (value: `"PARTNER_COST_TYPE_CUSTOM_FEE_3"`)

* `CUSTOM_FEE_4` (value: `"PARTNER_COST_TYPE_CUSTOM_FEE_4"`)

* `CUSTOM_FEE_5` (value: `"PARTNER_COST_TYPE_CUSTOM_FEE_5"`)

* `SCIBIDS_FEE` (value: `"PARTNER_COST_TYPE_SCIBIDS_FEE"`)





## Enum: FeeTypeEnum


* `UNSPECIFIED` (value: `"PARTNER_COST_FEE_TYPE_UNSPECIFIED"`)

* `CPM_FEE` (value: `"PARTNER_COST_FEE_TYPE_CPM_FEE"`)

* `MEDIA_FEE` (value: `"PARTNER_COST_FEE_TYPE_MEDIA_FEE"`)





## Enum: InvoiceTypeEnum


* `UNSPECIFIED` (value: `"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED"`)

* `DV360` (value: `"PARTNER_COST_INVOICE_TYPE_DV360"`)

* `PARTNER` (value: `"PARTNER_COST_INVOICE_TYPE_PARTNER"`)




