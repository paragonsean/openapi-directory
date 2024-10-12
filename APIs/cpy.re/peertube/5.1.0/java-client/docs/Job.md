

# Job


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**data** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**error** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**finishedOn** | **OffsetDateTime** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**processedOn** | **OffsetDateTime** |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |
| WAITING | &quot;waiting&quot; |
| DELAYED | &quot;delayed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACTIVITYPUB_HTTP_UNICAST | &quot;activitypub-http-unicast&quot; |
| ACTIVITYPUB_HTTP_BROADCAST | &quot;activitypub-http-broadcast&quot; |
| ACTIVITYPUB_HTTP_FETCHER | &quot;activitypub-http-fetcher&quot; |
| ACTIVITYPUB_FOLLOW | &quot;activitypub-follow&quot; |
| VIDEO_FILE_IMPORT | &quot;video-file-import&quot; |
| VIDEO_TRANSCODING | &quot;video-transcoding&quot; |
| EMAIL | &quot;email&quot; |
| VIDEO_IMPORT | &quot;video-import&quot; |
| VIDEOS_VIEWS_STATS | &quot;videos-views-stats&quot; |
| ACTIVITYPUB_REFRESHER | &quot;activitypub-refresher&quot; |
| VIDEO_REDUNDANCY | &quot;video-redundancy&quot; |
| VIDEO_CHANNEL_IMPORT | &quot;video-channel-import&quot; |



