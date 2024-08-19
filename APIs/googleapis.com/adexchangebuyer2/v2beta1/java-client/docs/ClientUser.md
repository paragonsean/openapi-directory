

# ClientUser

A client user is created under a client buyer and has restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the associated client buyer. The only way a new client user can be created is through accepting an email invitation (see the accounts.clients.invitations.create method). All fields are required unless otherwise specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientAccountId** | **String** | Numerical account ID of the client buyer with which the user is associated; the buyer must be a client of the current sponsor buyer. The value of this field is ignored in an update operation. |  [optional] |
|**email** | **String** | User&#39;s email address. The value of this field is ignored in an update operation. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the client user. |  [optional] |
|**userId** | **String** | The unique numerical ID of the client user that has accepted an invitation. The value of this field is ignored in an update operation. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| USER_STATUS_UNSPECIFIED | &quot;USER_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DISABLED | &quot;DISABLED&quot; |



