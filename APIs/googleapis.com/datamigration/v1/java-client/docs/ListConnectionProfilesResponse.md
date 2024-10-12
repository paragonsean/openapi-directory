

# ListConnectionProfilesResponse

Response message for 'ListConnectionProfiles' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionProfiles** | [**List&lt;ConnectionProfile&gt;**](ConnectionProfile.md) | The response list of connection profiles. |  [optional] |
|**nextPageToken** | **String** | A token which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



