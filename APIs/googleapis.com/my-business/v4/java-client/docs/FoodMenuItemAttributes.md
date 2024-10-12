

# FoodMenuItemAttributes

Attributes of a food item/dish.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allergen** | [**List&lt;AllergenEnum&gt;**](#List&lt;AllergenEnum&gt;) | Optional. Allergens associated with the food dish. It is highly recommended to provide this field. |  [optional] |
|**dietaryRestriction** | [**List&lt;DietaryRestrictionEnum&gt;**](#List&lt;DietaryRestrictionEnum&gt;) | Optional. Dietary information of the food dish. It is highly recommended to provide this field. |  [optional] |
|**ingredients** | [**List&lt;Ingredient&gt;**](Ingredient.md) | Optional. Ingredients of the food dish option. |  [optional] |
|**mediaKeys** | **List&lt;String&gt;** | Optional. The media keys of the media associated with the dish. Only photo media is supported. When there are multiple photos associated, the first photo is considered as the preferred photo. |  [optional] |
|**nutritionFacts** | [**NutritionFacts**](NutritionFacts.md) |  |  [optional] |
|**portionSize** | [**PortionSize**](PortionSize.md) |  |  [optional] |
|**preparationMethods** | [**List&lt;PreparationMethodsEnum&gt;**](#List&lt;PreparationMethodsEnum&gt;) | Optional. Methods on how the food dish option is prepared. |  [optional] |
|**price** | [**Money**](Money.md) |  |  [optional] |
|**servesNumPeople** | **Integer** | Optional. Number of people can be served by this food dish option. |  [optional] |
|**spiciness** | [**SpicinessEnum**](#SpicinessEnum) | Optional. Spiciness level of the food dish. |  [optional] |



## Enum: List&lt;AllergenEnum&gt;

| Name | Value |
|---- | -----|
| ALLERGEN_UNSPECIFIED | &quot;ALLERGEN_UNSPECIFIED&quot; |
| DAIRY | &quot;DAIRY&quot; |
| EGG | &quot;EGG&quot; |
| FISH | &quot;FISH&quot; |
| PEANUT | &quot;PEANUT&quot; |
| SHELLFISH | &quot;SHELLFISH&quot; |
| SOY | &quot;SOY&quot; |
| TREE_NUT | &quot;TREE_NUT&quot; |
| WHEAT | &quot;WHEAT&quot; |



## Enum: List&lt;DietaryRestrictionEnum&gt;

| Name | Value |
|---- | -----|
| DIETARY_RESTRICTION_UNSPECIFIED | &quot;DIETARY_RESTRICTION_UNSPECIFIED&quot; |
| HALAL | &quot;HALAL&quot; |
| KOSHER | &quot;KOSHER&quot; |
| ORGANIC | &quot;ORGANIC&quot; |
| VEGAN | &quot;VEGAN&quot; |
| VEGETARIAN | &quot;VEGETARIAN&quot; |



## Enum: List&lt;PreparationMethodsEnum&gt;

| Name | Value |
|---- | -----|
| PREPARATION_METHOD_UNSPECIFIED | &quot;PREPARATION_METHOD_UNSPECIFIED&quot; |
| BAKED | &quot;BAKED&quot; |
| BARBECUED | &quot;BARBECUED&quot; |
| BASTED | &quot;BASTED&quot; |
| BLANCHED | &quot;BLANCHED&quot; |
| BOILED | &quot;BOILED&quot; |
| BRAISED | &quot;BRAISED&quot; |
| CODDLED | &quot;CODDLED&quot; |
| FERMENTED | &quot;FERMENTED&quot; |
| FRIED | &quot;FRIED&quot; |
| GRILLED | &quot;GRILLED&quot; |
| KNEADED | &quot;KNEADED&quot; |
| MARINATED | &quot;MARINATED&quot; |
| PAN_FRIED | &quot;PAN_FRIED&quot; |
| PICKLED | &quot;PICKLED&quot; |
| PRESSURE_COOKED | &quot;PRESSURE_COOKED&quot; |
| ROASTED | &quot;ROASTED&quot; |
| SAUTEED | &quot;SAUTEED&quot; |
| SEARED | &quot;SEARED&quot; |
| SIMMERED | &quot;SIMMERED&quot; |
| SMOKED | &quot;SMOKED&quot; |
| STEAMED | &quot;STEAMED&quot; |
| STEEPED | &quot;STEEPED&quot; |
| STIR_FRIED | &quot;STIR_FRIED&quot; |
| OTHER_METHOD | &quot;OTHER_METHOD&quot; |



## Enum: SpicinessEnum

| Name | Value |
|---- | -----|
| SPICINESS_UNSPECIFIED | &quot;SPICINESS_UNSPECIFIED&quot; |
| MILD | &quot;MILD&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HOT | &quot;HOT&quot; |



