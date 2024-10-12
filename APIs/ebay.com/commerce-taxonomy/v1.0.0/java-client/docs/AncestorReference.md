

# AncestorReference

This type contains information about one of the ancestors of a suggested category. An ordered list of these references describes the path from the suggested category to the root of the category tree it belongs to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryId** | **String** | The unique identifier of the eBay ancestor category. Note: The root node of a full default category tree includes the categoryId field, but its value should not be relied upon. It provides no useful information for application development. |  [optional] |
|**categoryName** | **String** | The name of the ancestor category identified by categoryId. |  [optional] |
|**categorySubtreeNodeHref** | **String** | The href portion of the getCategorySubtree call that retrieves the subtree below the ancestor category node. |  [optional] |
|**categoryTreeNodeLevel** | **Integer** | The absolute level of the ancestor category node in the hierarchy of its category tree. Note: The root node of any full category tree is always at level 0. |  [optional] |



