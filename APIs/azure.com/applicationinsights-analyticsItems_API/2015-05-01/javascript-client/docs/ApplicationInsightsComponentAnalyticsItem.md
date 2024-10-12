# ApplicationInsightsManagementClient.ApplicationInsightsComponentAnalyticsItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The content of this item | [optional] 
**id** | **String** | Internally assigned unique id of the item definition. | [optional] 
**name** | **String** | The user-defined name of the item. | [optional] 
**properties** | [**ApplicationInsightsComponentAnalyticsItemProperties**](ApplicationInsightsComponentAnalyticsItemProperties.md) |  | [optional] 
**scope** | **String** | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [optional] 
**timeCreated** | **String** | Date and time in UTC when this item was created. | [optional] [readonly] 
**timeModified** | **String** | Date and time in UTC of the last modification that was made to this item. | [optional] [readonly] 
**type** | **String** | Enum indicating the type of the Analytics item. | [optional] 
**version** | **String** | This instance&#39;s version of the data model. This can change as new features are added. | [optional] [readonly] 



## Enum: ScopeEnum


* `shared` (value: `"shared"`)

* `user` (value: `"user"`)





## Enum: TypeEnum


* `query` (value: `"query"`)

* `function` (value: `"function"`)

* `folder` (value: `"folder"`)

* `recent` (value: `"recent"`)




