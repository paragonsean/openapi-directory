

# Change

A change to a file or shared drive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeType** | **String** | The type of the change. Possible values are &#x60;file&#x60; and &#x60;drive&#x60;. |  [optional] |
|**drive** | [**Drive**](Drive.md) |  |  [optional] |
|**driveId** | **String** | The ID of the shared drive associated with this change. |  [optional] |
|**_file** | [**ModelFile**](ModelFile.md) |  |  [optional] |
|**fileId** | **String** | The ID of the file which has changed. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#change\&quot;&#x60;. |  [optional] |
|**removed** | **Boolean** | Whether the file or shared drive has been removed from this list of changes, for example by deletion or loss of access. |  [optional] |
|**teamDrive** | [**TeamDrive**](TeamDrive.md) |  |  [optional] |
|**teamDriveId** | **String** | Deprecated: Use &#x60;driveId&#x60; instead. |  [optional] |
|**time** | **OffsetDateTime** | The time of this change (RFC 3339 date-time). |  [optional] |
|**type** | **String** | Deprecated: Use &#x60;changeType&#x60; instead. |  [optional] |



