

# ResourceAttributes

Attributes of resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessedAt** | **OffsetDateTime** | Date-time of the time when resource was accessed. |  [optional] |
|**accessedTime** | **Integer** | UNIX timestamp of last access |  [optional] |
|**createdAt** | **OffsetDateTime** | Date-time of resource creation. |  [optional] |
|**createdBy** | **String** | Username of the creator. |  [optional] |
|**createdTime** | **Integer** | UNIX timestamp of resource creation |  [optional] |
|**extension** | **String** | Resource extension. Property exists only if resource &#x60;type&#x60; is file. |  [optional] |
|**fileCount** | **Integer** | Number of files within folder. null if resource type is a file. |  [optional] |
|**hash** | **String** | Unique hash of the resource. |  [optional] |
|**name** | **String** | Resource name, e.g. the name of the file or folder. |  [optional] |
|**path** | **String** | Full path to the resource. |  [optional] |
|**previewable** | **Boolean** | Can resource be previewed. Property equals &#x60;null&#x60; if resource &#x60;type&#x60; is dir. |  [optional] |
|**size** | **Long** | Resource size in bytes |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the resource. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date-time of resource modification. |  [optional] |
|**updatedTime** | **Integer** | UNIX timestamp of resource modification |  [optional] |
|**uploadDate** | **OffsetDateTime** | Timestamp of resource upload. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |
| DIR | &quot;dir&quot; |



