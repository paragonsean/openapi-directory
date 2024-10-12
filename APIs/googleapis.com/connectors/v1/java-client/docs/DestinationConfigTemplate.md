

# DestinationConfigTemplate

DestinationConfigTemplate defines required destinations supported by the Connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultPort** | **Integer** | The default port. |  [optional] |
|**description** | **String** | Description. |  [optional] |
|**displayName** | **String** | Display name of the parameter. |  [optional] |
|**isAdvanced** | **Boolean** | Whether the current destination tempalate is part of Advanced settings |  [optional] |
|**key** | **String** | Key of the destination. |  [optional] |
|**max** | **Integer** | The maximum number of destinations supported for this key. |  [optional] |
|**min** | **Integer** | The minimum number of destinations supported for this key. |  [optional] |
|**portFieldType** | [**PortFieldTypeEnum**](#PortFieldTypeEnum) | Whether port number should be provided by customers. |  [optional] |
|**regexPattern** | **String** | Regex pattern for host. |  [optional] |



## Enum: PortFieldTypeEnum

| Name | Value |
|---- | -----|
| FIELD_TYPE_UNSPECIFIED | &quot;FIELD_TYPE_UNSPECIFIED&quot; |
| REQUIRED | &quot;REQUIRED&quot; |
| OPTIONAL | &quot;OPTIONAL&quot; |
| NOT_USED | &quot;NOT_USED&quot; |



