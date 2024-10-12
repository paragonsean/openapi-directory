

# BrandedFoodObjectItemsInner

An object containing information for this specific item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allergens** | **List&lt;String&gt;** | An array of ingredients in this item that may cause allergic reactions in people |  [optional] |
|**barcode** | **String** | EAN/UPC barcode |  [optional] |
|**brand** | **String** | The brand name that owns this item |  [optional] |
|**brandList** | **List&lt;String&gt;** | An array of brands we have associated with this item. Some items are sold by more than 1 brand. |  [optional] |
|**categories** | **List&lt;String&gt;** |  |  [optional] |
|**countries** | **List&lt;String&gt;** | An array of countries where this item is sold |  [optional] |
|**countryDetails** | [**BrandedFoodObjectItemsInnerCountryDetails**](BrandedFoodObjectItemsInnerCountryDetails.md) |  |  [optional] |
|**description** | **String** | A description of this item |  [optional] |
|**dietFlags** | [**List&lt;BrandedFoodObjectItemsInnerDietFlagsInner&gt;**](BrandedFoodObjectItemsInnerDietFlagsInner.md) | An array of ingredient objects that were flagged while grading this item for compatibility with each diet |  [optional] |
|**dietLabels** | [**BrandedFoodObjectItemsInnerDietLabels**](BrandedFoodObjectItemsInnerDietLabels.md) |  |  [optional] |
|**hasEnglishIngredients** | **Boolean** | A boolean indicating if we have English ingredients for this item |  [optional] |
|**ingredientList** | **List&lt;String&gt;** | An array of this item&#39;s ingredients |  [optional] |
|**ingredients** | **String** | This food item&#39;s ingredients from greatest quantity to least |  [optional] |
|**keywords** | **List&lt;String&gt;** | An array of keywords that can be used to describe this item |  [optional] |
|**minerals** | **List&lt;String&gt;** | An array of minerals that this item contains |  [optional] |
|**name** | **String** | Item name as provided by brand owner or as shown on packaging |  [optional] |
|**nutrients** | [**List&lt;BrandedFoodObjectItemsInnerNutrientsInner&gt;**](BrandedFoodObjectItemsInnerNutrientsInner.md) | An array containing nutrient informatio objects for this food item |  [optional] |
|**_package** | [**BrandedFoodObjectItemsInnerPackage**](BrandedFoodObjectItemsInnerPackage.md) |  |  [optional] |
|**packagingPhotos** | [**BrandedFoodObjectItemsInnerPackagingPhotos**](BrandedFoodObjectItemsInnerPackagingPhotos.md) |  |  [optional] |
|**palmOilIngredients** | **List&lt;String&gt;** | An array of ingredients made from palm oil |  [optional] |
|**serving** | [**BrandedFoodObjectItemsInnerServing**](BrandedFoodObjectItemsInnerServing.md) |  |  [optional] |
|**traces** | **List&lt;String&gt;** | An array of trace ingredients that may be found in this item |  [optional] |
|**vitamins** | **List&lt;String&gt;** | An array of vitamins that are found in this item |  [optional] |



