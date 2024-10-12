

# ListVolumeBackupsResponse

Response message for ListVolumeBackups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token which may be sent as page_token in a subsequent &#x60;ListVolumeBackups&#x60; call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |  [optional] |
|**volumeBackups** | [**List&lt;VolumeBackup&gt;**](VolumeBackup.md) | The list of VolumeBackups matching the given criteria. |  [optional] |



