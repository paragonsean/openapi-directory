

# Settings

Subscriptions settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultSla** | **String** | Default delivery method. |  |
|**deliveryChannels** | **List&lt;String&gt;** | Array containing delivery channels. |  |
|**executionHourInUtc** | **Integer** | Indicates the time future subscription orders will be generated. |  |
|**isMultipleInstallmentsEnabledOnCreation** | **Boolean** | Defines whether or not multiple installments are enabled when a subscription is created. |  |
|**isMultipleInstallmentsEnabledOnUpdate** | **Boolean** | Defines whether or not multiple installments are enabled when a subscription is updated. |  |
|**isUsingV3** | **Boolean** | Indicates whether or not Subscriptions V3 is enabled. |  |
|**manualPriceAllowed** | **Boolean** | When set to &#x60;true&#x60;, this property enables manual price configuration in subscription items. This is valid for all existing subscriptions, provided that there is a manual price configured and that &#x60;isUsingV3&#x60; is &#x60;true&#x60;. |  |
|**onMigrationProcess** | **Boolean** | Indicates whether or not the account is in the migration process to Subscriptions V3. |  |
|**orderCustomDataAppId** | **String** | When filled, this field passes along the &#x60;customData&#x60; infomration in the order to the future recurrent subscription orders. |  |
|**postponeExpiration** | **Boolean** | Defines whether or not the expiration of subscriptions can be postponed. |  |
|**randomIdGeneration** | **Boolean** | Defines whether or not the subscription order IDs will be randomly generated. |  |
|**slaOption** | **String** | Delivery method. |  |
|**useItemPriceFromOriginalOrder** | **Boolean** | When set to &#x60;true&#x60;, this property enables using the manual price for each item from the original subscription order. This is only valid for new subscriptions, created from the moment this configuration is enabled. For this to work, it is mandatory that the &#x60;manualPriceAllowed&#x60; property is set to &#x60;true&#x60; and that &#x60;isUsingV3&#x60; is &#x60;true&#x60;. |  |
|**workflowVersion** | **String** | Workflow version. |  |



