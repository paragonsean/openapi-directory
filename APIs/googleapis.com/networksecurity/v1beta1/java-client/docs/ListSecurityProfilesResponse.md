

# ListSecurityProfilesResponse

Response returned by the ListSecurityProfiles method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. |  [optional] |
|**securityProfiles** | [**List&lt;SecurityProfile&gt;**](SecurityProfile.md) | List of SecurityProfile resources. |  [optional] |



