

# CategorySubtree

This type contains information about a particular subtree of a specified eBay category tree. A category subtree consists of a non-root node of the category tree, and all of its descendants down to the leaf nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categorySubtreeNode** | [**CategoryTreeNode**](CategoryTreeNode.md) |  |  [optional] |
|**categoryTreeId** | **String** | The unique identifier of the eBay category tree to which this subtree belongs. |  [optional] |
|**categoryTreeVersion** | **String** | The version of the category tree identified by categoryTreeId. It&#39;s a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls. |  [optional] |



