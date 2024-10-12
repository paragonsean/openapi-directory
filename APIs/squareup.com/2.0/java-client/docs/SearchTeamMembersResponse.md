

# SearchTeamMembersResponse

Represents a response from a search request containing a filtered list of `TeamMember` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The opaque cursor for fetching the next page. For more information, see [pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | The errors that occurred during the request. |  [optional] |
|**teamMembers** | [**List&lt;TeamMember&gt;**](TeamMember.md) | The filtered list of &#x60;TeamMember&#x60; objects. |  [optional] |



