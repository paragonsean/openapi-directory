# PromotionsTaxesApi.SetcampaignconfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beginDateUtc** | **String** | Start date of the campaign audience in UTC format. | [optional] 
**endDateUtc** | **String** | End date of the campaign audience in UTC format. | [optional] 
**id** | **String** | Campaign audience ID. | [optional] 
**isActive** | **Boolean** | Defines if the campaign audience is active (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
**isAndOperator** | **Boolean** | When &#x60;true&#x60;, determines that all the &#x60;targetConfigurations&#x60; need to be valid for the campaign audience to be active. When &#x60;false&#x60;, determines that if at least one of the &#x60;targetConfigurations&#x60; is valid, the campaign audience will be active. | [optional] 
**isArchived** | **Boolean** | Defines if the campaign audience is archived (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
**lastModified** | [**SetcampaignconfigurationRequestLastModified**](SetcampaignconfigurationRequestLastModified.md) |  | [optional] 
**name** | **String** | Campaign audience name. | [optional] 
**targetConfigurations** | [**[SetcampaignconfigurationRequestTargetConfigurationsInner]**](SetcampaignconfigurationRequestTargetConfigurationsInner.md) | Array that contains all target audience that the campaign audience will be valid. | [optional] 


