

# ListVolumeSnapshotsResponse

Response message containing the list of volume snapshots.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token identifying a page of results from the server. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |
|**volumeSnapshots** | [**List&lt;VolumeSnapshot&gt;**](VolumeSnapshot.md) | The list of snapshots. |  [optional] |



