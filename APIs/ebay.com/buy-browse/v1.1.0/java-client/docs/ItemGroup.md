

# ItemGroup

The type that defines the fields for the item details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonDescriptions** | [**List&lt;CommonDescriptions&gt;**](CommonDescriptions.md) | An array of containers for a description and the item IDs of all the items that have this exact description. Often the item variations within an item group all have the same description. Instead of repeating this description in the item details of each item, a description that is shared by at least one other item is returned in this container. If the description is unique, it is returned in the items.description field. |  [optional] |
|**items** | [**List&lt;Item&gt;**](Item.md) | An array of containers for all the item variation details, excluding the description. |  [optional] |
|**warnings** | [**List&lt;Error&gt;**](Error.md) | An array of warning messages. These types of errors do not prevent the method from executing but should be checked. |  [optional] |



