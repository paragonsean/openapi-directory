

# AssociateFileSystemAliasesRequest

The request object specifying one or more DNS alias names to associate with an Amazon FSx for Windows File Server file system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | **String** | (Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK. |  [optional] |
|**fileSystemId** | [**String**](String.md) |  |  |
|**aliases** | [**List**](List.md) |  |  |



