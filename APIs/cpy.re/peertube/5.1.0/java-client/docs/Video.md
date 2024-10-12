

# Video


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**AccountSummary**](AccountSummary.md) |  |  [optional] |
|**blacklisted** | **Boolean** |  |  [optional] |
|**blacklistedReason** | **String** |  |  [optional] |
|**category** | [**VideoConstantNumberCategory**](VideoConstantNumberCategory.md) | category in which the video is classified |  [optional] |
|**channel** | [**VideoChannelSummary**](VideoChannelSummary.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | time at which the video object was first drafted |  [optional] |
|**description** | **String** | truncated description of the video, written in Markdown. Resolve &#x60;descriptionPath&#x60; to get the full description of maximum &#x60;10000&#x60; characters.  |  [optional] |
|**dislikes** | **Integer** |  |  [optional] |
|**duration** | **Integer** | duration of the video in seconds |  [optional] |
|**embedPath** | **String** |  |  [optional] |
|**id** | **Integer** | object id for the video |  [optional] |
|**isLive** | **Boolean** |  |  [optional] |
|**isLocal** | **Boolean** |  |  [optional] |
|**language** | [**VideoConstantStringLanguage**](VideoConstantStringLanguage.md) | main language used in the video |  [optional] |
|**licence** | [**VideoConstantNumberLicence**](VideoConstantNumberLicence.md) | licence under which the video is distributed |  [optional] |
|**likes** | **Integer** |  |  [optional] |
|**name** | **String** | title of the video |  [optional] |
|**nsfw** | **Boolean** |  |  [optional] |
|**originallyPublishedAt** | **OffsetDateTime** | used to represent a date of first publication, prior to the practical publication date of &#x60;publishedAt&#x60; |  [optional] |
|**previewPath** | **String** |  |  [optional] |
|**privacy** | [**VideoPrivacyConstant**](VideoPrivacyConstant.md) | privacy policy used to distribute the video |  [optional] |
|**publishedAt** | **OffsetDateTime** | time at which the video was marked as ready for playback (with restrictions depending on &#x60;privacy&#x60;). Usually set after a &#x60;state&#x60; evolution. |  [optional] |
|**scheduledUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md) |  |  [optional] |
|**shortUUID** | **String** | translation of a uuid v4 with a bigger alphabet to have a shorter uuid |  [optional] |
|**state** | [**VideoStateConstant**](VideoStateConstant.md) | represents the internal state of the video processing within the PeerTube instance |  [optional] |
|**thumbnailPath** | **String** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | last time the video&#39;s metadata was modified |  [optional] |
|**userHistory** | [**VideoUserHistory**](VideoUserHistory.md) |  |  [optional] |
|**uuid** | **UUID** | universal identifier for the video, that can be used across instances |  [optional] |
|**views** | **Integer** |  |  [optional] |
|**waitTranscoding** | **Boolean** |  |  [optional] |



