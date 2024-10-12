

# TypePropertiesMapping

Metadata for a Link's property mapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | Link type. |  [optional] |
|**sourcePropertyName** | **String** |  Property name on the source Entity Type. |  |
|**targetPropertyName** | **String** | Property name on the target Entity Type. |  |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| UPDATE_ALWAYS | &quot;UpdateAlways&quot; |
| COPY_IF_NULL | &quot;CopyIfNull&quot; |



