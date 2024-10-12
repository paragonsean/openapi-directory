

# ModifyLabelsRequest

A request to modify the set of labels on a file. This request may contain many modifications that will either all succeed or all fail atomically.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | This is always drive#modifyLabelsRequest. |  [optional] |
|**labelModifications** | [**List&lt;LabelModification&gt;**](LabelModification.md) | The list of modifications to apply to the labels on the file. |  [optional] |



