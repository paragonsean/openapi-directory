

# ListConnectionProfilesResponse

Response message for listing connection profiles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionProfiles** | [**List&lt;ConnectionProfile&gt;**](ConnectionProfile.md) | List of connection profiles. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



