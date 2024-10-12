

# AzureBlobStorageHttpLogsConfig

Http logs to azure blob storage configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Enabled |  [optional] |
|**retentionInDays** | **Integer** | Retention in days.              Remove blobs older than X days.              0 or lower means no retention. |  [optional] |
|**sasUrl** | **String** | SAS url to a azure blob container with read/write/list/delete permissions |  [optional] |



