

# ChannelMetadataInteractionsAddTo

When a channel appears in the context of adding or removing a video from it (`/videos/{video_id}/available_channels`), include information about adding or removing the video. This data requires a bearer token with the `private` scope.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**options** | **List&lt;String&gt;** | An array of HTTP methods permitted on this URI. This data requires a bearer token with the &#x60;private&#x60; scope. |  |
|**uri** | **String** | The API URI that resolves to the connection data. This data requires a bearer token with the &#x60;private&#x60; scope. |  |



