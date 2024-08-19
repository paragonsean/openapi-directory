

# TrainSourceFilter

Filter to apply to the documents in the source path for training.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeSubFolders** | **Boolean** | A flag to indicate if sub folders within the set of prefix folders will also need to be included when searching for content to be preprocessed. |  [optional] |
|**prefix** | **String** | A case-sensitive prefix string to filter documents in the source path for training. For example, when using a Azure storage blob Uri, use the prefix to restrict sub folders for training. |  [optional] |



