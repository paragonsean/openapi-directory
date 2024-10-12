

# ClientUserInvitation

An invitation for a new client user to get access to the Authorized Buyers UI. All fields are required unless otherwise specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientAccountId** | **String** | Numerical account ID of the client buyer that the invited user is associated with. The value of this field is ignored in create operations. |  [optional] |
|**email** | **String** | The email address to which the invitation is sent. Email addresses should be unique among all client users under each sponsor buyer. |  [optional] |
|**invitationId** | **String** | The unique numerical ID of the invitation that is sent to the user. The value of this field is ignored in create operations. |  [optional] |



