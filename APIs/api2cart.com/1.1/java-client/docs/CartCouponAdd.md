

# CartCouponAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionAmount** | **BigDecimal** | Defines the discount amount value. |  |
|**actionApplyTo** | [**ActionApplyToEnum**](#ActionApplyToEnum) | Defines where discount should be applied |  |
|**actionConditionEntity** | **String** | Defines entity for action condition. |  [optional] |
|**actionConditionKey** | **String** | Defines entity attribute code for action condition. |  [optional] |
|**actionConditionOperator** | **String** | Defines condition operator. |  [optional] |
|**actionConditionValue** | **String** | Defines condition attribute value/s. Can be comma separated string. |  [optional] |
|**actionScope** | [**ActionScopeEnum**](#ActionScopeEnum) | Specify how discount should be applied. If scope&#x3D;matching_items, then discount will be applied to each of the items that match action conditions. Scope order means that discount will be applied once. |  |
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | Coupon discount type |  |
|**code** | **String** | Coupon code |  |
|**codes** | **List&lt;String&gt;** | Entity codes |  [optional] |
|**dateEnd** | **String** | Defines when discount code will be expired. |  [optional] |
|**dateStart** | **String** | Defines when discount code will be available. |  [optional] |
|**name** | **String** | Coupon name |  [optional] |
|**storeId** | **String** | Store Id |  [optional] |
|**usageLimit** | **Integer** | Usage limit for coupon. |  [optional] |
|**usageLimitPerCustomer** | **Integer** | Usage limit per customer. |  [optional] |



## Enum: ActionApplyToEnum

| Name | Value |
|---- | -----|
| ORDER_TOTAL | &quot;order_total&quot; |
| ITEM_PRICE | &quot;item_price&quot; |
| SHIPPING | &quot;shipping&quot; |



## Enum: ActionScopeEnum

| Name | Value |
|---- | -----|
| ORDER | &quot;order&quot; |
| MATCHING_ITEMS | &quot;matching_items&quot; |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| PERCENT | &quot;percent&quot; |
| FIXED | &quot;fixed&quot; |



