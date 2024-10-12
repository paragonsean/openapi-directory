# SubscriptionsApiV3.Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultSla** | **String** | Default delivery method. | 
**deliveryChannels** | **[String]** | Array containing delivery channels. | 
**executionHourInUtc** | **Number** | Indicates the time future subscription orders will be generated. | [default to 0]
**isMultipleInstallmentsEnabledOnCreation** | **Boolean** | Defines whether or not multiple installments are enabled when a subscription is created. | [default to false]
**isMultipleInstallmentsEnabledOnUpdate** | **Boolean** | Defines whether or not multiple installments are enabled when a subscription is updated. | [default to false]
**isUsingV3** | **Boolean** | Indicates whether or not Subscriptions V3 is enabled. | [default to false]
**manualPriceAllowed** | **Boolean** | When set to &#x60;true&#x60;, this property enables manual price configuration in subscription items. This is valid for all existing subscriptions, provided that there is a manual price configured and that &#x60;isUsingV3&#x60; is &#x60;true&#x60;. | [default to false]
**onMigrationProcess** | **Boolean** | Indicates whether or not the account is in the migration process to Subscriptions V3. | [default to false]
**orderCustomDataAppId** | **String** | When filled, this field passes along the &#x60;customData&#x60; infomration in the order to the future recurrent subscription orders. | 
**postponeExpiration** | **Boolean** | Defines whether or not the expiration of subscriptions can be postponed. | [default to false]
**randomIdGeneration** | **Boolean** | Defines whether or not the subscription order IDs will be randomly generated. | [default to false]
**slaOption** | **String** | Delivery method. | [default to &#39;&#39;]
**useItemPriceFromOriginalOrder** | **Boolean** | When set to &#x60;true&#x60;, this property enables using the manual price for each item from the original subscription order. This is only valid for new subscriptions, created from the moment this configuration is enabled. For this to work, it is mandatory that the &#x60;manualPriceAllowed&#x60; property is set to &#x60;true&#x60; and that &#x60;isUsingV3&#x60; is &#x60;true&#x60;. | [default to false]
**workflowVersion** | **String** | Workflow version. | [default to &#39;&#39;]


