

# ListUserInvitationsResponse

Response message for UserInvitation listing request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token for the next page. If not empty, indicates that there may be more &#x60;UserInvitation&#x60; resources that match the listing request; this value can be used in a subsequent ListUserInvitationsRequest to get continued results with the current list call. |  [optional] |
|**userInvitations** | [**List&lt;UserInvitation&gt;**](UserInvitation.md) | The list of UserInvitation resources. |  [optional] |



