

# SalesOrderFreightDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | The amounts calculated based on the ship terms.  /// |  [optional] |
|**amountInBaseCurrency** | **Double** | The amounts calculated based on the ship terms in base currency of the order. |  [optional] |
|**cost** | **Double** | The freight cost calculated for the sales order, |  [optional] |
|**costInBaseCurrency** | **Double** | The freight cost calculated for the sales order in base currency. |  [optional] |
|**premiumAmount** | **Double** | The additional freight charges for handling the order. |  [optional] [readonly] |
|**premiumAmountInBaseCurrency** | **Double** | The additional freight charges in base currency for handling the order. |  [optional] [readonly] |
|**taxCategoryId** | **String** | The tax category that applies to the freight amount.  By default, it is the tax category associated with the ship via code selected for the order. |  [optional] [readonly] |
|**volume** | **Double** |  |  [optional] |
|**weight** | **Double** |  |  [optional] |



