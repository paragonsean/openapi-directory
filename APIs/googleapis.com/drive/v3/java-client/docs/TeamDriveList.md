

# TeamDriveList

A list of Team Drives.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#teamDriveList\&quot;&#x60;. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of Team Drives. This will be absent if the end of the Team Drives list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. The page token is typically valid for several hours. However, if new items are added or removed, your expected results might differ. |  [optional] |
|**teamDrives** | [**List&lt;TeamDrive&gt;**](TeamDrive.md) | The list of Team Drives. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |  [optional] |



