

# CreateMerchantRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessLineId** | **String** | The unique identifier of the [business line](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines). Required for an Adyen for Platforms Manage integration. |  [optional] |
|**companyId** | **String** | The unique identifier of the company account. |  |
|**description** | **String** | Your description for the merchant account, maximum 300 characters. |  [optional] |
|**legalEntityId** | **String** | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities). Required for an Adyen for Platforms Manage integration. |  [optional] |
|**pricingPlan** | **String** | Sets the pricing plan for the merchant account. Required for an Adyen for Platforms Manage integration. Your Adyen contact will provide the values that you can use. |  [optional] |
|**reference** | **String** | Your reference for the merchant account. To make this reference the unique identifier of the merchant account, your Adyen contact can set up a template on your company account. The template can have 6 to 255 characters with upper- and lower-case letters, underscores, and numbers. When your company account has a template, then the &#x60;reference&#x60; is required and must be unique within the company account. |  [optional] |
|**salesChannels** | **List&lt;String&gt;** | List of sales channels that the merchant will process payments with |  [optional] |



