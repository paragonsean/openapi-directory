

# Admin

An administrator of an Account or a Location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminName** | **String** | The name of the admin. When making the initial invitation, this is the invitee&#39;s email address. On &#x60;GET&#x60; calls, the user&#39;s email address is returned if the invitation is still pending. Otherwise, it contains the user&#39;s first and last names. |  [optional] |
|**name** | **String** | The resource name. For account admins, this is in the form: &#x60;accounts/{account_id}/admins/{admin_id}&#x60; For location admins, this is in the form: &#x60;accounts/{account_id}/locations/{location_id}/admins/{admin_id}&#x60; |  [optional] |
|**pendingInvitation** | **Boolean** | Output only. Indicates whether this admin has a pending invitation for the specified resource. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Specifies the AdminRole that this admin uses with the specified Account or Location resource. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN_ROLE_UNSPECIFIED | &quot;ADMIN_ROLE_UNSPECIFIED&quot; |
| OWNER | &quot;OWNER&quot; |
| CO_OWNER | &quot;CO_OWNER&quot; |
| MANAGER | &quot;MANAGER&quot; |
| COMMUNITY_MANAGER | &quot;COMMUNITY_MANAGER&quot; |



