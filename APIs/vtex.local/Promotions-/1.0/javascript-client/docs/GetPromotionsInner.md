# PromotionsTaxesApi.GetPromotionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns** | **[String]** | Array with campaign audiences that activate this promotion. | [optional] 
**activateGiftsMultiplier** | **Boolean** | If set as &#x60;true&#x60;, it activates gifts Multiplier. | [optional] 
**areSalesChannelIdsExclusive** | **Boolean** | If set to &#x60;false&#x60;, this promotion will be applied to any trade policies present on the &#x60;idsSalesChannel&#x60; field. If set to &#x60;true&#x60;, trade policies present on that field will make this promotion not to be applied. | [optional] 
**beginDate** | **String** | Promotion Begin Date (UTC). | [optional] 
**description** | **String** | Promotion internal description. | [optional] 
**endDate** | **String** | Promotion End Date (UTC). | [optional] 
**hasMaxPricePerItem** | **Boolean** | Defines if there is a maximum price per item. | [optional] 
**idCalculatorConfiguration** | **String** | Promotion ID. | [optional] 
**idsSalesChannel** | **[String]** | List of Trade Policies that activate this promotion. | [optional] 
**isActive** | **Boolean** | If set as &#x60;true&#x60; the promotion is activated. If set as &#x60;false&#x60; the promotion is deactivated. | [optional] 
**isArchived** | **Boolean** | If set as &#x60;true&#x60; the Promotion is archived. If set as &#x60;false&#x60; the Promotion is not archived. | [optional] 
**isTax** | **Boolean** | Defines if it is a tax. | [optional] 
**lastModifiedUtc** | **String** | Date and time when the promotion was last modified (UTC). | [optional] 
**maxUsage** | **Number** | Defines how many times the promotion can be used. | [optional] 
**name** | **String** | Promotion Name. | [optional] 
**percentualTax** | **Number** | Percentual tax applied. | [optional] 
**scope** | [**GetPromotionsInnerScope**](GetPromotionsInnerScope.md) |  | [optional] 
**status** | **String** | Status of the promotion. | [optional] 
**type** | **String** | Defines the type of promotion. | [optional] 
**utmCampain** | **String** | utmCampaign code. | [optional] 
**utmSource** | **String** | utmSource code. | [optional] 
**utmiCampaign** | **String** | utmiCampaign code. | [optional] 


