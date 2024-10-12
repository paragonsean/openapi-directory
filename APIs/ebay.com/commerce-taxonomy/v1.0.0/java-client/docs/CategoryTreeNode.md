

# CategoryTreeNode

This type contains information about all nodes of a category tree or subtree hierarchy, including and below the specified <b>Category</b>, down to the leaf nodes. It is a recursive structure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**Category**](Category.md) |  |  [optional] |
|**categoryTreeNodeLevel** | **Integer** | The absolute level of the current category tree node in the hierarchy of its category tree. Note: The root node of any full category tree is always at level 0. |  [optional] |
|**childCategoryTreeNodes** | [**List&lt;CategoryTreeNode&gt;**](CategoryTreeNode.md) | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes. Returned only if the current category tree node is not a leaf node (the value of leafCategoryTreeNode is false). |  [optional] |
|**leafCategoryTreeNode** | **Boolean** | A value of true indicates that the current category tree node is a leaf node (it has no child nodes). A value of false indicates that the current node has one or more child nodes, which are identified by the childCategoryTreeNodes array. Returned only if the value of this field is true. |  [optional] |
|**parentCategoryTreeNodeHref** | **String** | The href portion of the getCategorySubtree call that retrieves the subtree below the parent of this category tree node. Not returned if the current category tree node is the root node of its tree. |  [optional] |



