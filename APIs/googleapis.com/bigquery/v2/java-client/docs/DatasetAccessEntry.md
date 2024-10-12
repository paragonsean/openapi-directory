

# DatasetAccessEntry

Grants all resources of particular types in a particular dataset read access to the current dataset. Similar to how individually authorized views work, updates to any resource granted through its dataset (including creation of new resources) requires read permission to referenced resources, plus write permission to the authorizing dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | [**DatasetReference**](DatasetReference.md) |  |  [optional] |
|**targetTypes** | [**List&lt;TargetTypesEnum&gt;**](#List&lt;TargetTypesEnum&gt;) | Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. |  [optional] |



## Enum: List&lt;TargetTypesEnum&gt;

| Name | Value |
|---- | -----|
| TARGET_TYPE_UNSPECIFIED | &quot;TARGET_TYPE_UNSPECIFIED&quot; |
| VIEWS | &quot;VIEWS&quot; |
| ROUTINES | &quot;ROUTINES&quot; |



