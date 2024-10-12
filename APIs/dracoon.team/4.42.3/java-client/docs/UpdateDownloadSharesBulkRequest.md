

# UpdateDownloadSharesBulkRequest

Request model for updating a list of Download Shares

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  |  [optional] |
|**maxDownloads** | **Integer** | Max allowed downloads |  [optional] |
|**objectIds** | **List&lt;Long&gt;** | List of ids |  |
|**resetMaxDownloads** | **Boolean** | Set &#39;true&#39; to reset &#39;maxDownloads&#39; for Download Share. |  [optional] |
|**showCreatorName** | **Boolean** | Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | Show creator email address. |  [optional] |



