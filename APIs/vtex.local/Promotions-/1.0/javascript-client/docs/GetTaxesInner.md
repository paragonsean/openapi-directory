# PromotionsTaxesApi.GetTaxesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns** | **[String]** | Array with campaign audiences that activate this tax. | [optional] 
**activateGiftsMultiplier** | **Boolean** | If set as &#x60;true&#x60;, it activates gifts Multiplier. | [optional] 
**areSalesChannelIdsExclusive** | **Boolean** | If set to &#x60;false&#x60;, this tax will be applied to any trade policies present on the &#x60;idsSalesChannel&#x60; field. If set to &#x60;true&#x60;, trade policies present on that field will make this tax not to be applied. | [optional] 
**beginDate** | **String** | Tax start date (UTC). | [optional] 
**description** | **String** | Tax internal description. | [optional] 
**endDate** | **String** | Tax end date (UTC). | [optional] 
**hasMaxPricePerItem** | **Boolean** | Defines if there is a maximum price per item. | [optional] 
**idCalculatorConfiguration** | **String** | Tax ID. | [optional] 
**idsSalesChannel** | **[String]** | List of Trade Policies that activate this tax. | [optional] 
**isActive** | **Boolean** | If set as &#x60;true&#x60; the tax is activated. If set as &#x60;false&#x60; the tax is deactivated. | [optional] 
**isArchived** | **Boolean** | If set as &#x60;true&#x60; the tax is archived. If set as &#x60;false&#x60; the tax is not archived. | [optional] 
**isTax** | **Boolean** | Defines if it is a tax. | [optional] 
**lastModifiedUtc** | **String** | Date and time when the tax was last modified (UTC). | [optional] 
**maxUsage** | **Number** | Defines how many times the tax can be used. | [optional] 
**name** | **String** | Tax name. | [optional] 
**percentualTax** | **Number** | Percentual tax applied. | [optional] 
**scope** | [**GetTaxesInnerScope**](GetTaxesInnerScope.md) |  | [optional] 
**status** | **String** | Status of the tax. | [optional] 
**type** | **String** | Defines the type of tax. | [optional] 
**utmCampain** | **String** | utmCampaign code. | [optional] 
**utmSource** | **String** | utmSource code. | [optional] 
**utmiCampaign** | **String** | utmiCampaign code. | [optional] 


