# GoogleMyBusinessApi.Admin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminName** | **String** | The name of the admin. When making the initial invitation, this is the invitee&#39;s email address. On &#x60;GET&#x60; calls, the user&#39;s email address is returned if the invitation is still pending. Otherwise, it contains the user&#39;s first and last names. | [optional] 
**name** | **String** | The resource name. For account admins, this is in the form: &#x60;accounts/{account_id}/admins/{admin_id}&#x60; For location admins, this is in the form: &#x60;accounts/{account_id}/locations/{location_id}/admins/{admin_id}&#x60; | [optional] 
**pendingInvitation** | **Boolean** | Output only. Indicates whether this admin has a pending invitation for the specified resource. | [optional] 
**role** | **String** | Specifies the AdminRole that this admin uses with the specified Account or Location resource. | [optional] 



## Enum: RoleEnum


* `ADMIN_ROLE_UNSPECIFIED` (value: `"ADMIN_ROLE_UNSPECIFIED"`)

* `OWNER` (value: `"OWNER"`)

* `CO_OWNER` (value: `"CO_OWNER"`)

* `MANAGER` (value: `"MANAGER"`)

* `COMMUNITY_MANAGER` (value: `"COMMUNITY_MANAGER"`)




