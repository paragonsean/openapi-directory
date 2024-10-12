# MagentoB2B.SalesRuleDataRuleInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionCondition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  | [optional] 
**applyToShipping** | **Boolean** | The rule applies to shipping | 
**condition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  | [optional] 
**couponType** | **String** | Coupon type | 
**customerGroupIds** | **[Number]** | Ids of customer groups that the rule applies to | 
**description** | **String** | Description | [optional] 
**discountAmount** | **Number** | Discount amount | 
**discountQty** | **Number** | Maximum qty discount is applied | [optional] 
**discountStep** | **Number** | Discount step | 
**extensionAttributes** | [**SalesRuleDataRuleExtensionInterface**](SalesRuleDataRuleExtensionInterface.md) |  | [optional] 
**fromDate** | **String** | The start date when the coupon is active | [optional] 
**isActive** | **Boolean** | The coupon is active | 
**isAdvanced** | **Boolean** | Is this field needed | 
**isRss** | **Boolean** | Whether the rule is in RSS | 
**name** | **String** | Rule name | [optional] 
**productIds** | **[Number]** | Product ids | [optional] 
**ruleId** | **Number** | Rule id | [optional] 
**simpleAction** | **String** | Simple action of the rule | [optional] 
**simpleFreeShipping** | **String** | To grant free shipping | [optional] 
**sortOrder** | **Number** | Sort order | 
**stopRulesProcessing** | **Boolean** | To stop rule processing | 
**storeLabels** | [**[SalesRuleDataRuleLabelInterface]**](SalesRuleDataRuleLabelInterface.md) | Display label | [optional] 
**timesUsed** | **Number** | How many times the rule has been used | 
**toDate** | **String** | The end date when the coupon is active | [optional] 
**useAutoGeneration** | **Boolean** | To auto generate coupon | 
**usesPerCoupon** | **Number** | Limit of uses per coupon | 
**usesPerCustomer** | **Number** | Number of uses per customer | 
**websiteIds** | **[Number]** | A list of websites the rule applies to | 


