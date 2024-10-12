

# ContainerProperties

The container properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerStatus** | [**ContainerStatusEnum**](#ContainerStatusEnum) | Current status of the container. |  [optional] [readonly] |
|**createdDateTime** | **OffsetDateTime** | The UTC time when container got created. |  [optional] [readonly] |
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | DataFormat for Container |  |
|**refreshDetails** | [**RefreshDetails**](RefreshDetails.md) |  |  [optional] |



## Enum: ContainerStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| OFFLINE | &quot;Offline&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| UPDATING | &quot;Updating&quot; |
| NEEDS_ATTENTION | &quot;NeedsAttention&quot; |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| BLOCK_BLOB | &quot;BlockBlob&quot; |
| PAGE_BLOB | &quot;PageBlob&quot; |
| AZURE_FILE | &quot;AzureFile&quot; |



