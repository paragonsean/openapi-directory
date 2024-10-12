

# API2ModelsRecipesRecipeResponse

DTO used to return a recipe with videos

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeMinutes** | **Integer** |  |  [optional] |
|**adTags** | **String** |  |  [optional] |
|**adminBoost** | **Integer** |  |  [optional] |
|**allCategoriesText** | **String** |  |  [optional] |
|**bookmarkImageURL** | **String** |  |  [optional] |
|**bookmarkSiteLogo** | **String** |  |  [optional] |
|**bookmarkURL** | **String** |  |  [optional] |
|**category** | **String** |  |  [optional] |
|**collection** | **String** |  |  [optional] |
|**collectionID** | **Integer** |  |  [optional] |
|**creationDate** | **OffsetDateTime** |  |  [optional] |
|**cuisine** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**favoriteCount** | **Integer** |  |  [optional] |
|**imageSquares** | **List&lt;Integer&gt;** |  |  [optional] |
|**imageURL** | **String** |  |  [optional] |
|**ingredients** | [**List&lt;BigOvenModelAPIIngredient&gt;**](BigOvenModelAPIIngredient.md) |  |  [optional] |
|**ingredientsTextBlock** | **String** |  |  [optional] |
|**instructions** | **String** |  |  [optional] |
|**isBookmark** | **Boolean** |  |  [optional] |
|**isPrivate** | **Boolean** |  |  [optional] |
|**isRecipeScan** | **Boolean** |  |  [optional] |
|**isSponsored** | **Boolean** |  |  [optional] |
|**lastModified** | **OffsetDateTime** |  |  [optional] |
|**maxImageSquare** | **Integer** |  |  [optional] |
|**medalCount** | **Integer** |  |  [optional] |
|**menuCount** | **Integer** |  |  [optional] |
|**microcategory** | **String** |  |  [optional] |
|**notesCount** | **Integer** |  |  [optional] |
|**nutritionInfo** | [**BigOvenModelAPINutritionInfo**](BigOvenModelAPINutritionInfo.md) |  |  [optional] |
|**photoUrl** | **String** |  |  [optional] |
|**poster** | [**BigOvenModelAPIUserInfo**](BigOvenModelAPIUserInfo.md) |  |  [optional] |
|**primaryIngredient** | **String** |  |  [optional] |
|**recipeID** | **Integer** |  |  [optional] |
|**reviewCount** | **Integer** |  |  [optional] |
|**starRating** | **Double** |  |  [optional] |
|**steps** | [**List&lt;BigOvenModelInstructionStep&gt;**](BigOvenModelInstructionStep.md) |  |  [optional] |
|**subcategory** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**totalMinutes** | **Integer** |  |  [optional] |
|**variantOfRecipeID** | **Integer** |  |  [optional] |
|**verifiedByClass** | **String** |  |  [optional] |
|**verifiedDateTime** | **OffsetDateTime** |  |  [optional] |
|**videos** | [**List&lt;API2ModelsRecipesRecipeVideoResponse&gt;**](API2ModelsRecipesRecipeVideoResponse.md) | Gets or sets the recipe videos, i.e. a list of type {API2.Models.Recipes.RecipeVideoResponse} |  [optional] |
|**webURL** | **String** |  |  [optional] |
|**yieldNumber** | **Double** |  |  [optional] |
|**yieldUnit** | **String** |  |  [optional] |



