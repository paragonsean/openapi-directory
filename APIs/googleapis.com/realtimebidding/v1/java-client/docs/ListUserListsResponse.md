

# ListUserListsResponse

The list user list response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The continuation page token to send back to the server in a subsequent request. Due to a currently known issue, it is recommended that the caller keep invoking the list method until the time a next page token is not returned, even if the result set is empty. |  [optional] |
|**userLists** | [**List&lt;UserList&gt;**](UserList.md) | List of user lists from the search. |  [optional] |



