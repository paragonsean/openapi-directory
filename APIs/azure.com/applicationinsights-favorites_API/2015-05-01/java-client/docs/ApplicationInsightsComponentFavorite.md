

# ApplicationInsightsComponentFavorite

Properties that define a favorite that is associated to an Application Insights component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | Favorite category, as defined by the user at creation time. |  [optional] |
|**config** | **String** | Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON |  [optional] |
|**favoriteId** | **String** | Internally assigned unique id of the favorite definition. |  [optional] [readonly] |
|**favoriteType** | [**FavoriteTypeEnum**](#FavoriteTypeEnum) | Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component. |  [optional] |
|**isGeneratedFromTemplate** | **Boolean** | Flag denoting wether or not this favorite was generated from a template. |  [optional] |
|**name** | **String** | The user-defined name of the favorite. |  [optional] |
|**sourceType** | **String** | The source of the favorite definition. |  [optional] |
|**tags** | **List&lt;String&gt;** | A list of 0 or more tags that are associated with this favorite definition |  [optional] |
|**timeModified** | **String** | Date and time in UTC of the last modification that was made to this favorite definition. |  [optional] [readonly] |
|**userId** | **String** | Unique user id of the specific user that owns this favorite. |  [optional] [readonly] |
|**version** | **String** | This instance&#39;s version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search. |  [optional] |



## Enum: FavoriteTypeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;shared&quot; |
| USER | &quot;user&quot; |



