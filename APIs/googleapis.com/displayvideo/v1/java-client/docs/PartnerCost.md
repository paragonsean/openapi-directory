

# PartnerCost

Settings that control a partner cost. A partner cost is any type of expense involved in running a campaign, other than the costs of purchasing impressions (which is called the media cost) and using third-party audience segment data (data fee). Some examples of partner costs include the fees for using DV360, a third-party ad server, or a third-party ad serving verification service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costType** | [**CostTypeEnum**](#CostTypeEnum) | Required. The type of the partner cost. |  [optional] |
|**feeAmount** | **String** | The CPM fee amount in micros of advertiser&#39;s currency. Applicable when the fee_type is &#x60;PARTNER_FEE_TYPE_CPM_FEE&#x60;. Must be greater than or equal to 0. For example, for 1.5 standard unit of the advertiser&#39;s currency, set this field to 1500000. |  [optional] |
|**feePercentageMillis** | **String** | The media fee percentage in millis (1/1000 of a percent). Applicable when the fee_type is &#x60;PARTNER_FEE_TYPE_MEDIA_FEE&#x60;. Must be greater than or equal to 0. For example: 100 represents 0.1%. |  [optional] |
|**feeType** | [**FeeTypeEnum**](#FeeTypeEnum) | Required. The fee type for this partner cost. |  [optional] |
|**invoiceType** | [**InvoiceTypeEnum**](#InvoiceTypeEnum) | The invoice type for this partner cost. * Required when cost_type is one of: - &#x60;PARTNER_COST_TYPE_ADLOOX&#x60; - &#x60;PARTNER_COST_TYPE_DOUBLE_VERIFY&#x60; - &#x60;PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE&#x60;. * Output only for other types. |  [optional] |



## Enum: CostTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARTNER_COST_TYPE_UNSPECIFIED&quot; |
| ADLOOX | &quot;PARTNER_COST_TYPE_ADLOOX&quot; |
| ADLOOX_PREBID | &quot;PARTNER_COST_TYPE_ADLOOX_PREBID&quot; |
| ADSAFE | &quot;PARTNER_COST_TYPE_ADSAFE&quot; |
| ADXPOSE | &quot;PARTNER_COST_TYPE_ADXPOSE&quot; |
| AGGREGATE_KNOWLEDGE | &quot;PARTNER_COST_TYPE_AGGREGATE_KNOWLEDGE&quot; |
| AGENCY_TRADING_DESK | &quot;PARTNER_COST_TYPE_AGENCY_TRADING_DESK&quot; |
| DV360_FEE | &quot;PARTNER_COST_TYPE_DV360_FEE&quot; |
| COMSCORE_VCE | &quot;PARTNER_COST_TYPE_COMSCORE_VCE&quot; |
| DATA_MANAGEMENT_PLATFORM | &quot;PARTNER_COST_TYPE_DATA_MANAGEMENT_PLATFORM&quot; |
| DEFAULT | &quot;PARTNER_COST_TYPE_DEFAULT&quot; |
| DOUBLE_VERIFY | &quot;PARTNER_COST_TYPE_DOUBLE_VERIFY&quot; |
| DOUBLE_VERIFY_PREBID | &quot;PARTNER_COST_TYPE_DOUBLE_VERIFY_PREBID&quot; |
| EVIDON | &quot;PARTNER_COST_TYPE_EVIDON&quot; |
| INTEGRAL_AD_SCIENCE_VIDEO | &quot;PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_VIDEO&quot; |
| INTEGRAL_AD_SCIENCE_PREBID | &quot;PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_PREBID&quot; |
| MEDIA_COST_DATA | &quot;PARTNER_COST_TYPE_MEDIA_COST_DATA&quot; |
| MOAT_VIDEO | &quot;PARTNER_COST_TYPE_MOAT_VIDEO&quot; |
| NIELSEN_DAR | &quot;PARTNER_COST_TYPE_NIELSEN_DAR&quot; |
| SHOP_LOCAL | &quot;PARTNER_COST_TYPE_SHOP_LOCAL&quot; |
| TERACENT | &quot;PARTNER_COST_TYPE_TERACENT&quot; |
| THIRD_PARTY_AD_SERVER | &quot;PARTNER_COST_TYPE_THIRD_PARTY_AD_SERVER&quot; |
| TRUST_METRICS | &quot;PARTNER_COST_TYPE_TRUST_METRICS&quot; |
| VIZU | &quot;PARTNER_COST_TYPE_VIZU&quot; |
| ADLINGO_FEE | &quot;PARTNER_COST_TYPE_ADLINGO_FEE&quot; |
| CUSTOM_FEE_1 | &quot;PARTNER_COST_TYPE_CUSTOM_FEE_1&quot; |
| CUSTOM_FEE_2 | &quot;PARTNER_COST_TYPE_CUSTOM_FEE_2&quot; |
| CUSTOM_FEE_3 | &quot;PARTNER_COST_TYPE_CUSTOM_FEE_3&quot; |
| CUSTOM_FEE_4 | &quot;PARTNER_COST_TYPE_CUSTOM_FEE_4&quot; |
| CUSTOM_FEE_5 | &quot;PARTNER_COST_TYPE_CUSTOM_FEE_5&quot; |
| SCIBIDS_FEE | &quot;PARTNER_COST_TYPE_SCIBIDS_FEE&quot; |



## Enum: FeeTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARTNER_COST_FEE_TYPE_UNSPECIFIED&quot; |
| CPM_FEE | &quot;PARTNER_COST_FEE_TYPE_CPM_FEE&quot; |
| MEDIA_FEE | &quot;PARTNER_COST_FEE_TYPE_MEDIA_FEE&quot; |



## Enum: InvoiceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARTNER_COST_INVOICE_TYPE_UNSPECIFIED&quot; |
| DV360 | &quot;PARTNER_COST_INVOICE_TYPE_DV360&quot; |
| PARTNER | &quot;PARTNER_COST_INVOICE_TYPE_PARTNER&quot; |



