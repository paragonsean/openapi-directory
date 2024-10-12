

# SalesRuleDataRuleInterface

Interface RuleInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionCondition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  |  [optional] |
|**applyToShipping** | **Boolean** | The rule applies to shipping |  |
|**condition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  |  [optional] |
|**couponType** | **String** | Coupon type |  |
|**customerGroupIds** | **List&lt;Integer&gt;** | Ids of customer groups that the rule applies to |  |
|**description** | **String** | Description |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount |  |
|**discountQty** | **BigDecimal** | Maximum qty discount is applied |  [optional] |
|**discountStep** | **Integer** | Discount step |  |
|**extensionAttributes** | [**SalesRuleDataRuleExtensionInterface**](SalesRuleDataRuleExtensionInterface.md) |  |  [optional] |
|**fromDate** | **String** | The start date when the coupon is active |  [optional] |
|**isActive** | **Boolean** | The coupon is active |  |
|**isAdvanced** | **Boolean** | Is this field needed |  |
|**isRss** | **Boolean** | Whether the rule is in RSS |  |
|**name** | **String** | Rule name |  [optional] |
|**productIds** | **List&lt;Integer&gt;** | Product ids |  [optional] |
|**ruleId** | **Integer** | Rule id |  [optional] |
|**simpleAction** | **String** | Simple action of the rule |  [optional] |
|**simpleFreeShipping** | **String** | To grant free shipping |  [optional] |
|**sortOrder** | **Integer** | Sort order |  |
|**stopRulesProcessing** | **Boolean** | To stop rule processing |  |
|**storeLabels** | [**List&lt;SalesRuleDataRuleLabelInterface&gt;**](SalesRuleDataRuleLabelInterface.md) | Display label |  [optional] |
|**timesUsed** | **Integer** | How many times the rule has been used |  |
|**toDate** | **String** | The end date when the coupon is active |  [optional] |
|**useAutoGeneration** | **Boolean** | To auto generate coupon |  |
|**usesPerCoupon** | **Integer** | Limit of uses per coupon |  |
|**usesPerCustomer** | **Integer** | Number of uses per customer |  |
|**websiteIds** | **List&lt;Integer&gt;** | A list of websites the rule applies to |  |



