

# ApplicationInsightsComponentAnalyticsItem

Properties that define an Analytics item that is associated to an Application Insights component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The content of this item |  [optional] |
|**id** | **String** | Internally assigned unique id of the item definition. |  [optional] |
|**name** | **String** | The user-defined name of the item. |  [optional] |
|**properties** | [**ApplicationInsightsComponentAnalyticsItemProperties**](ApplicationInsightsComponentAnalyticsItemProperties.md) |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. |  [optional] |
|**timeCreated** | **String** | Date and time in UTC when this item was created. |  [optional] [readonly] |
|**timeModified** | **String** | Date and time in UTC of the last modification that was made to this item. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Enum indicating the type of the Analytics item. |  [optional] |
|**version** | **String** | This instance&#39;s version of the data model. This can change as new features are added. |  [optional] [readonly] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;shared&quot; |
| USER | &quot;user&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| QUERY | &quot;query&quot; |
| FUNCTION | &quot;function&quot; |
| FOLDER | &quot;folder&quot; |
| RECENT | &quot;recent&quot; |



