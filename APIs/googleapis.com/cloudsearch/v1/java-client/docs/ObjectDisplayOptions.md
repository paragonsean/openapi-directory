

# ObjectDisplayOptions

The display options for an object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metalines** | [**List&lt;Metaline&gt;**](Metaline.md) | Defines the properties that are displayed in the metalines of the search results. The property values are displayed in the order given here. If a property holds multiple values, all of the values are displayed before the next properties. For this reason, it is a good practice to specify singular properties before repeated properties in this list. All of the properties must set is_returnable to true. The maximum number of metalines is 3. |  [optional] |
|**objectDisplayLabel** | **String** | The user friendly label to display in the search result to indicate the type of the item. This is OPTIONAL; if not provided, an object label isn&#39;t displayed on the context line of the search results. The maximum length is 64 characters. |  [optional] |



