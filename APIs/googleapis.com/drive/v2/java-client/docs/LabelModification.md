

# LabelModification

A modification to a label on a file. A LabelModification can be used to apply a label to a file, update an existing label on a file, or remove a label from a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldModifications** | [**List&lt;LabelFieldModification&gt;**](LabelFieldModification.md) | The list of modifications to this label&#39;s fields. |  [optional] |
|**kind** | **String** | This is always &#x60;drive#labelModification&#x60;. |  [optional] |
|**labelId** | **String** | The ID of the label to modify. |  [optional] |
|**removeLabel** | **Boolean** | If true, the label will be removed from the file. |  [optional] |



