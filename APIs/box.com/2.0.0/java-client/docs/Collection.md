

# Collection

A collection of items, including files and folders.  Currently, the only collection available is the `favorites` collection.  The contents of a collection can be explored in a similar way to which the contents of a folder is explored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionType** | [**CollectionTypeEnum**](#CollectionTypeEnum) | The type of the collection. This is used to determine the proper visual treatment for collections. |  [optional] |
|**id** | **String** | The unique identifier for this collection. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | The name of the collection. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;collection&#x60; |  [optional] |



## Enum: CollectionTypeEnum

| Name | Value |
|---- | -----|
| FAVORITES | &quot;favorites&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| FAVORITES | &quot;Favorites&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COLLECTION | &quot;collection&quot; |



