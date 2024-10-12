

# FoodMenu

Menu of a business that serves food dishes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cuisines** | [**List&lt;CuisinesEnum&gt;**](#List&lt;CuisinesEnum&gt;) | Optional. Cuisine information for the food menu. It is highly recommended to provide this field. |  [optional] |
|**labels** | [**List&lt;MenuLabel&gt;**](MenuLabel.md) | Required. Language-tagged labels for the menu. E.g. \&quot;menu\&quot;, \&quot;lunch special\&quot;. Display names should be 140 characters or less, with descriptions 1,000 characters or less. At least one set of labels is required. |  [optional] |
|**sections** | [**List&lt;FoodMenuSection&gt;**](FoodMenuSection.md) | Required. Sections of the menu. |  [optional] |
|**sourceUrl** | **String** | Optional. Source URL of menu if there is a webpage to go to. |  [optional] |



## Enum: List&lt;CuisinesEnum&gt;

| Name | Value |
|---- | -----|
| CUISINE_UNSPECIFIED | &quot;CUISINE_UNSPECIFIED&quot; |
| AMERICAN | &quot;AMERICAN&quot; |
| ASIAN | &quot;ASIAN&quot; |
| BRAZILIAN | &quot;BRAZILIAN&quot; |
| BREAK_FAST | &quot;BREAK_FAST&quot; |
| BRUNCH | &quot;BRUNCH&quot; |
| CHICKEN | &quot;CHICKEN&quot; |
| CHINESE | &quot;CHINESE&quot; |
| FAMILY | &quot;FAMILY&quot; |
| FAST_FOOD | &quot;FAST_FOOD&quot; |
| FRENCH | &quot;FRENCH&quot; |
| GREEK | &quot;GREEK&quot; |
| GERMAN | &quot;GERMAN&quot; |
| HAMBURGER | &quot;HAMBURGER&quot; |
| INDIAN | &quot;INDIAN&quot; |
| INDONESIAN | &quot;INDONESIAN&quot; |
| ITALIAN | &quot;ITALIAN&quot; |
| JAPANESE | &quot;JAPANESE&quot; |
| KOREAN | &quot;KOREAN&quot; |
| LATIN_AMERICAN | &quot;LATIN_AMERICAN&quot; |
| MEDITERRANEAN | &quot;MEDITERRANEAN&quot; |
| MEXICAN | &quot;MEXICAN&quot; |
| PAKISTANI | &quot;PAKISTANI&quot; |
| PIZZA | &quot;PIZZA&quot; |
| SEAFOOD | &quot;SEAFOOD&quot; |
| SPANISH | &quot;SPANISH&quot; |
| SUSHI | &quot;SUSHI&quot; |
| THAI | &quot;THAI&quot; |
| TURKISH | &quot;TURKISH&quot; |
| VEGETARIAN | &quot;VEGETARIAN&quot; |
| VIETNAMESE | &quot;VIETNAMESE&quot; |
| OTHER_CUISINE | &quot;OTHER_CUISINE&quot; |



