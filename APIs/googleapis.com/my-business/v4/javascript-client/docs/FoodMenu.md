# GoogleMyBusinessApi.FoodMenu

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cuisines** | **[String]** | Optional. Cuisine information for the food menu. It is highly recommended to provide this field. | [optional] 
**labels** | [**[MenuLabel]**](MenuLabel.md) | Required. Language-tagged labels for the menu. E.g. \&quot;menu\&quot;, \&quot;lunch special\&quot;. Display names should be 140 characters or less, with descriptions 1,000 characters or less. At least one set of labels is required. | [optional] 
**sections** | [**[FoodMenuSection]**](FoodMenuSection.md) | Required. Sections of the menu. | [optional] 
**sourceUrl** | **String** | Optional. Source URL of menu if there is a webpage to go to. | [optional] 



## Enum: [CuisinesEnum]


* `CUISINE_UNSPECIFIED` (value: `"CUISINE_UNSPECIFIED"`)

* `AMERICAN` (value: `"AMERICAN"`)

* `ASIAN` (value: `"ASIAN"`)

* `BRAZILIAN` (value: `"BRAZILIAN"`)

* `BREAK_FAST` (value: `"BREAK_FAST"`)

* `BRUNCH` (value: `"BRUNCH"`)

* `CHICKEN` (value: `"CHICKEN"`)

* `CHINESE` (value: `"CHINESE"`)

* `FAMILY` (value: `"FAMILY"`)

* `FAST_FOOD` (value: `"FAST_FOOD"`)

* `FRENCH` (value: `"FRENCH"`)

* `GREEK` (value: `"GREEK"`)

* `GERMAN` (value: `"GERMAN"`)

* `HAMBURGER` (value: `"HAMBURGER"`)

* `INDIAN` (value: `"INDIAN"`)

* `INDONESIAN` (value: `"INDONESIAN"`)

* `ITALIAN` (value: `"ITALIAN"`)

* `JAPANESE` (value: `"JAPANESE"`)

* `KOREAN` (value: `"KOREAN"`)

* `LATIN_AMERICAN` (value: `"LATIN_AMERICAN"`)

* `MEDITERRANEAN` (value: `"MEDITERRANEAN"`)

* `MEXICAN` (value: `"MEXICAN"`)

* `PAKISTANI` (value: `"PAKISTANI"`)

* `PIZZA` (value: `"PIZZA"`)

* `SEAFOOD` (value: `"SEAFOOD"`)

* `SPANISH` (value: `"SPANISH"`)

* `SUSHI` (value: `"SUSHI"`)

* `THAI` (value: `"THAI"`)

* `TURKISH` (value: `"TURKISH"`)

* `VEGETARIAN` (value: `"VEGETARIAN"`)

* `VIETNAMESE` (value: `"VIETNAMESE"`)

* `OTHER_CUISINE` (value: `"OTHER_CUISINE"`)




