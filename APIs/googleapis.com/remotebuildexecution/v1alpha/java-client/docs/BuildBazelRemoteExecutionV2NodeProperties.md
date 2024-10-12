

# BuildBazelRemoteExecutionV2NodeProperties

Node properties for FileNodes, DirectoryNodes, and SymlinkNodes. The server is responsible for specifying the properties that it accepts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mtime** | **String** | The file&#39;s last modification timestamp. |  [optional] |
|**properties** | [**List&lt;BuildBazelRemoteExecutionV2NodeProperty&gt;**](BuildBazelRemoteExecutionV2NodeProperty.md) | A list of string-based NodeProperties. |  [optional] |
|**unixMode** | **Integer** | The UNIX file mode, e.g., 0755. |  [optional] |



