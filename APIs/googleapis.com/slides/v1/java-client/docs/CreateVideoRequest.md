

# CreateVideoRequest

Creates a video. NOTE: Creating a video from Google Drive requires that the requesting app have at least one of the drive, drive.readonly, or drive.file OAuth scopes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elementProperties** | [**PageElementProperties**](PageElementProperties.md) |  |  [optional] |
|**id** | **String** | The video source&#39;s unique identifier for this video. e.g. For YouTube video https://www.youtube.com/watch?v&#x3D;7U3axjORYZ0, the ID is 7U3axjORYZ0. For a Google Drive video https://drive.google.com/file/d/1xCgQLFTJi5_Xl8DgW_lcUYq5e-q6Hi5Q the ID is 1xCgQLFTJi5_Xl8DgW_lcUYq5e-q6Hi5Q. To access a Google Drive video file, you might need to add a resource key to the HTTP header for a subset of old files. For more information, see [Access link-shared files using resource keys](https://developers.google.com/drive/api/v3/resource-keys). |  [optional] |
|**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the ID must not be less than 5 or greater than 50. If you don&#39;t specify an ID, a unique one is generated. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The video source. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| SOURCE_UNSPECIFIED | &quot;SOURCE_UNSPECIFIED&quot; |
| YOUTUBE | &quot;YOUTUBE&quot; |
| DRIVE | &quot;DRIVE&quot; |



