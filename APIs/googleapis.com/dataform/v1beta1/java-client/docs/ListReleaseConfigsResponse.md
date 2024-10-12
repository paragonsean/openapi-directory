

# ListReleaseConfigsResponse

`ListReleaseConfigs` response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**releaseConfigs** | [**List&lt;ReleaseConfig&gt;**](ReleaseConfig.md) | List of release configs. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations which could not be reached. |  [optional] |



