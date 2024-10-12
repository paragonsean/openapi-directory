# GoogleMyBusinessApi.FoodMenuItemAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen** | **[String]** | Optional. Allergens associated with the food dish. It is highly recommended to provide this field. | [optional] 
**dietaryRestriction** | **[String]** | Optional. Dietary information of the food dish. It is highly recommended to provide this field. | [optional] 
**ingredients** | [**[Ingredient]**](Ingredient.md) | Optional. Ingredients of the food dish option. | [optional] 
**mediaKeys** | **[String]** | Optional. The media keys of the media associated with the dish. Only photo media is supported. When there are multiple photos associated, the first photo is considered as the preferred photo. | [optional] 
**nutritionFacts** | [**NutritionFacts**](NutritionFacts.md) |  | [optional] 
**portionSize** | [**PortionSize**](PortionSize.md) |  | [optional] 
**preparationMethods** | **[String]** | Optional. Methods on how the food dish option is prepared. | [optional] 
**price** | [**Money**](Money.md) |  | [optional] 
**servesNumPeople** | **Number** | Optional. Number of people can be served by this food dish option. | [optional] 
**spiciness** | **String** | Optional. Spiciness level of the food dish. | [optional] 



## Enum: [AllergenEnum]


* `ALLERGEN_UNSPECIFIED` (value: `"ALLERGEN_UNSPECIFIED"`)

* `DAIRY` (value: `"DAIRY"`)

* `EGG` (value: `"EGG"`)

* `FISH` (value: `"FISH"`)

* `PEANUT` (value: `"PEANUT"`)

* `SHELLFISH` (value: `"SHELLFISH"`)

* `SOY` (value: `"SOY"`)

* `TREE_NUT` (value: `"TREE_NUT"`)

* `WHEAT` (value: `"WHEAT"`)





## Enum: [DietaryRestrictionEnum]


* `DIETARY_RESTRICTION_UNSPECIFIED` (value: `"DIETARY_RESTRICTION_UNSPECIFIED"`)

* `HALAL` (value: `"HALAL"`)

* `KOSHER` (value: `"KOSHER"`)

* `ORGANIC` (value: `"ORGANIC"`)

* `VEGAN` (value: `"VEGAN"`)

* `VEGETARIAN` (value: `"VEGETARIAN"`)





## Enum: [PreparationMethodsEnum]


* `PREPARATION_METHOD_UNSPECIFIED` (value: `"PREPARATION_METHOD_UNSPECIFIED"`)

* `BAKED` (value: `"BAKED"`)

* `BARBECUED` (value: `"BARBECUED"`)

* `BASTED` (value: `"BASTED"`)

* `BLANCHED` (value: `"BLANCHED"`)

* `BOILED` (value: `"BOILED"`)

* `BRAISED` (value: `"BRAISED"`)

* `CODDLED` (value: `"CODDLED"`)

* `FERMENTED` (value: `"FERMENTED"`)

* `FRIED` (value: `"FRIED"`)

* `GRILLED` (value: `"GRILLED"`)

* `KNEADED` (value: `"KNEADED"`)

* `MARINATED` (value: `"MARINATED"`)

* `PAN_FRIED` (value: `"PAN_FRIED"`)

* `PICKLED` (value: `"PICKLED"`)

* `PRESSURE_COOKED` (value: `"PRESSURE_COOKED"`)

* `ROASTED` (value: `"ROASTED"`)

* `SAUTEED` (value: `"SAUTEED"`)

* `SEARED` (value: `"SEARED"`)

* `SIMMERED` (value: `"SIMMERED"`)

* `SMOKED` (value: `"SMOKED"`)

* `STEAMED` (value: `"STEAMED"`)

* `STEEPED` (value: `"STEEPED"`)

* `STIR_FRIED` (value: `"STIR_FRIED"`)

* `OTHER_METHOD` (value: `"OTHER_METHOD"`)





## Enum: SpicinessEnum


* `SPICINESS_UNSPECIFIED` (value: `"SPICINESS_UNSPECIFIED"`)

* `MILD` (value: `"MILD"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HOT` (value: `"HOT"`)




