

# IngredientObjectItemsInner

An object containing information for this specific item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calorieConversionFactor** | [**IngredientObjectItemsInnerCalorieConversionFactor**](IngredientObjectItemsInnerCalorieConversionFactor.md) |  |  [optional] |
|**categories** | **List&lt;String&gt;** |  |  [optional] |
|**commonName** | **String** | Common name associated with this item. These generally clarify what the item is (e.g. when the brand name is \&quot;BRAND&#39;s Spicy Enchilada\&quot; the common name may be \&quot;Chicken enchilada\&quot;) |  [optional] |
|**components** | [**List&lt;IngredientObjectItemsInnerComponentsInner&gt;**](IngredientObjectItemsInnerComponentsInner.md) | An array of objects containing the constituent parts of a food (e.g. bone is a component of meat) |  [optional] |
|**footnote** | **String** | Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall |  [optional] |
|**name** | **String** | Item name as provided by brand owner or as shown on packaging |  [optional] |
|**nutrients** | [**List&lt;IngredientObjectItemsInnerNutrientsInner&gt;**](IngredientObjectItemsInnerNutrientsInner.md) | An array containing nutrient informatio objects for this food item |  [optional] |
|**portions** | [**List&lt;IngredientObjectItemsInnerPortionsInner&gt;**](IngredientObjectItemsInnerPortionsInner.md) | An array of objects containing information on discrete amounts of a food found in this item |  [optional] |
|**proteinConversionFactor** | **BigDecimal** | The multiplication factor used to calculate protein from nitrogen |  [optional] |
|**score** | **String** | A value that represents how similar the name of this food item is to the original search term. The lower the value the closer this item&#39;s name is to the original search term. |  [optional] |
|**searchTerm** | **String** | The original search term that found this food item |  [optional] |



