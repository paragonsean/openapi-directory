

# UserInvitation

The `UserInvitation` resource represents an email that can be sent to an unmanaged user account inviting them to join the customer's Google Workspace or Cloud Identity account. An unmanaged account shares an email address domain with the Google Workspace or Cloud Identity account but is not managed by it yet. If the user accepts the `UserInvitation`, the user account will become managed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mailsSentCount** | **String** | Number of invitation emails sent to the user. |  [optional] |
|**name** | **String** | Shall be of the form &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the &#x60;UserInvitation&#x60;. |  [optional] |
|**updateTime** | **String** | Time when the &#x60;UserInvitation&#x60; was last updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_YET_SENT | &quot;NOT_YET_SENT&quot; |
| INVITED | &quot;INVITED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| DECLINED | &quot;DECLINED&quot; |



