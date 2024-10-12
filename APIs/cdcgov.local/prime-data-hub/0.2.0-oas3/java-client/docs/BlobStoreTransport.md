

# BlobStoreTransport

Moves results to a Azure Blob Store. Typcially used for HHS Protect interfaces.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerName** | **String** | This name of the Azure container |  |
|**storageName** | **String** | This looks for an env var with this name. env var value is the connection string |  |
|**type** | **String** | The discriminator |  |



