

# Project

Represents a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Gets the date this project was created. |  [optional] [readonly] |
|**description** | **String** | Gets or sets the description of the project. |  |
|**drModeEnabled** | **Boolean** | Gets if the Disaster Recovery (DR) mode is on, indicating the project is temporarily read-only. |  [optional] [readonly] |
|**id** | **UUID** | Gets the project id. |  [optional] [readonly] |
|**lastModified** | **OffsetDateTime** | Gets the date this project was last modified. |  [optional] [readonly] |
|**name** | **String** | Gets or sets the name of the project. |  |
|**settings** | [**ProjectSettings**](ProjectSettings.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Gets the status of the project. |  [optional] |
|**thumbnailUri** | **String** | Gets the thumbnail url representing the image. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| IMPORTING | &quot;Importing&quot; |
| FAILED | &quot;Failed&quot; |



