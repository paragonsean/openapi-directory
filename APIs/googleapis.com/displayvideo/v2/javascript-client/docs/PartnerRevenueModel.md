# DisplayVideo360Api.PartnerRevenueModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markupAmount** | **String** | Required. The markup amount of the partner revenue model. Must be greater than or equal to 0. * When the markup_type is set to be &#x60;PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM&#x60;, this field represents the CPM markup in micros of advertiser&#39;s currency. For example, 1500000 represents 1.5 standard units of the currency. * When the markup_type is set to be &#x60;PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP&#x60;, this field represents the media cost percent markup in millis. For example, 100 represents 0.1% (decimal 0.001). * When the markup_type is set to be &#x60;PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP&#x60;, this field represents the total media cost percent markup in millis. For example, 100 represents 0.1% (decimal 0.001). | [optional] 
**markupType** | **String** | Required. The markup type of the partner revenue model. | [optional] 



## Enum: MarkupTypeEnum


* `UNSPECIFIED` (value: `"PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED"`)

* `CPM` (value: `"PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM"`)

* `MEDIA_COST_MARKUP` (value: `"PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP"`)

* `TOTAL_MEDIA_COST_MARKUP` (value: `"PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP"`)




