

# PricingConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockAccount** | **Boolean** | Defines if access to the Pricing APIs is blocked for external requests. |  [optional] |
|**blockedRoutes** | **List&lt;String&gt;** | Array with all blocked routes. |  [optional] |
|**defaultMarkup** | **Integer** | Account default markup. |  |
|**hasMigrated** | **Boolean** | Defines if the account has migrated to Pricing V2. |  |
|**hasOptionalBasePrice** | **Boolean** | Defines if optional base price is allowed. |  [optional] |
|**hasPriceInheritance** | **Boolean** | Deprecated. Use the &#x60;priceInheritance&#x60; field instead. |  [optional] |
|**migrationStatus** | **String** | Pricing V2 migration status. |  [optional] |
|**minimumMarkups** | **Map&lt;String, Integer&gt;** | Account minimum markup. |  |
|**priceInheritance** | **String** | Condition of price inheritance from its parent account. This field can have three possible values: &#x60;never&#x60; if the store should never inherit prices, &#x60;nonexistent&#x60; if the store should only inherit prices in case of nonexistent prices for a given product, or &#x60;always&#x60; if the store should always inherit prices, regardless of its own prices. |  [optional] |
|**priceTableLimit** | **Integer** | Price Table Limit. |  [optional] |
|**priceTableSelectionStrategy** | **String** | The strategy used to get prices when there is more than one option. Possible values: &#x60;first&#x60;, &#x60;highest&#x60;, &#x60;lowest&#x60;. Default: &#x60;first&#x60;. |  [optional] |
|**priceVariation** | [**PricingConfigurationPriceVariation**](PricingConfigurationPriceVariation.md) |  |  [optional] |
|**sellersToOverride** | **List&lt;Object&gt;** | Overrides prices from sellers. |  [optional] |
|**tradePolicyConfigs** | [**List&lt;PricingConfigurationTradePolicyConfigsInner&gt;**](PricingConfigurationTradePolicyConfigsInner.md) | Trade Policy Configurations array. |  [optional] |



