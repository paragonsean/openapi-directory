

# ServerConfigCustomTranscoding

Settings pertaining to transcoding jobs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowAdditionalExtensions** | **Boolean** | Allow your users to upload .mkv, .mov, .avi, .wmv, .flv, .f4v, .3g2, .3gp, .mts, m2ts, .mxf, .nut videos |  [optional] |
|**allowAudioFiles** | **Boolean** | If a user uploads an audio file, PeerTube will create a video by merging the preview file and the audio file |  [optional] |
|**concurrency** | **BigDecimal** | Amount of transcoding jobs to execute in parallel |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**hls** | [**ServerConfigCustomTranscodingHls**](ServerConfigCustomTranscodingHls.md) |  |  [optional] |
|**profile** | [**ProfileEnum**](#ProfileEnum) | New profiles can be added by plugins ; available in core PeerTube: &#39;default&#39;.  |  [optional] |
|**resolutions** | [**ServerConfigCustomTranscodingResolutions**](ServerConfigCustomTranscodingResolutions.md) |  |  [optional] |
|**threads** | **Integer** | Amount of threads used by ffmpeg for 1 transcoding job |  [optional] |
|**webtorrent** | [**ServerConfigCustomTranscodingWebtorrent**](ServerConfigCustomTranscodingWebtorrent.md) |  |  [optional] |



## Enum: ProfileEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |



