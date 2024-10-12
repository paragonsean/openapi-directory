

# DestinyDefinitionsDestinyItemSocketCategoryDefinition

Sockets are grouped into categories in the UI. These define which category and which sockets are under that category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**socketCategoryHash** | **Integer** | The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info. |  [optional] |
|**socketIndexes** | **List&lt;Integer&gt;** | Use these indexes to look up the sockets in the \&quot;sockets.socketEntries\&quot; property on the item definition. These are the indexes under the category, in game-rendered order. |  [optional] |



