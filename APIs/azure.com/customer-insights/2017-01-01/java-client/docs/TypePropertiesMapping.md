

# TypePropertiesMapping

Metadata for a Link's property mapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interactionTypePropertyName** | **String** |  Property name on the source Interaction Type. |  |
|**isProfileTypeId** | **Boolean** | Flag to indicate whether the Profile Type property is an id on the Profile Type. |  [optional] |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | Link type. |  [optional] |
|**profileTypePropertyName** | **String** | Property name on the target Profile Type. |  |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| UPDATE_ALWAYS | &quot;UpdateAlways&quot; |
| COPY_IF_NULL | &quot;CopyIfNull&quot; |



