

# ParentReference

A reference to a file's parent. Some resource methods (such as `parents.get`) require a `parentId`. Use the `parents.list` method to retrieve the ID for a parent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the parent. |  [optional] |
|**isRoot** | **Boolean** | Output only. Whether or not the parent is the root folder. |  [optional] |
|**kind** | **String** | Output only. This is always &#x60;drive#parentReference&#x60;. |  [optional] |
|**parentLink** | **String** | Output only. A link to the parent. |  [optional] |
|**selfLink** | **String** | Output only. A link back to this reference. |  [optional] |



