

# AssetStaticRenditions

An object containing the current status of any static renditions (mp4s). The object does not exist if no static renditions have been requested. See [Download your videos](https://docs.mux.com/guides/video/download-your-videos) for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**files** | [**List&lt;AssetStaticRenditionsFilesInner&gt;**](AssetStaticRenditionsFilesInner.md) | Array of file objects. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates the status of downloadable MP4 versions of this asset. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| PREPARING | &quot;preparing&quot; |
| DISABLED | &quot;disabled&quot; |
| ERRORED | &quot;errored&quot; |



