

# Entity

A workspace entity that may represent a tag, trigger, variable, or folder in addition to its status in the workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtInVariable** | [**BuiltInVariable**](BuiltInVariable.md) |  |  [optional] |
|**changeStatus** | [**ChangeStatusEnum**](#ChangeStatusEnum) | Represents how the entity has been changed in the workspace. |  [optional] |
|**client** | [**Client**](Client.md) |  |  [optional] |
|**customTemplate** | [**CustomTemplate**](CustomTemplate.md) |  |  [optional] |
|**folder** | [**Folder**](Folder.md) |  |  [optional] |
|**gtagConfig** | [**GtagConfig**](GtagConfig.md) |  |  [optional] |
|**tag** | [**Tag**](Tag.md) |  |  [optional] |
|**transformation** | [**Transformation**](Transformation.md) |  |  [optional] |
|**trigger** | [**Trigger**](Trigger.md) |  |  [optional] |
|**variable** | [**Variable**](Variable.md) |  |  [optional] |
|**zone** | [**Zone**](Zone.md) |  |  [optional] |



## Enum: ChangeStatusEnum

| Name | Value |
|---- | -----|
| CHANGE_STATUS_UNSPECIFIED | &quot;changeStatusUnspecified&quot; |
| NONE | &quot;none&quot; |
| ADDED | &quot;added&quot; |
| DELETED | &quot;deleted&quot; |
| UPDATED | &quot;updated&quot; |



