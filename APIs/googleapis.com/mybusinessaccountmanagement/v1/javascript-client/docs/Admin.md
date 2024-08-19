# MyBusinessAccountManagementApi.Admin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Immutable. The name of the Account resource that this Admin refers to. Used when calling locations.admins.create to invite a LocationGroup as an admin. If both this field and &#x60;admin&#x60; are set on &#x60;CREATE&#x60; requests, this field takes precedence and the email address in &#x60;admin&#x60; will be ignored. Format: &#x60;accounts/{account}&#x60;. | [optional] 
**admin** | **String** | Optional. The name of the admin. When making the initial invitation, this is the invitee&#39;s email address. On &#x60;GET&#x60; calls, the user&#39;s email address is returned if the invitation is still pending. Otherwise, it contains the user&#39;s first and last names. This field is only needed to be set during admin creation. | [optional] 
**name** | **String** | Immutable. The resource name. For account admins, this is in the form: &#x60;accounts/{account_id}/admins/{admin_id}&#x60; For location admins, this is in the form: &#x60;locations/{location_id}/admins/{admin_id}&#x60; This field will be ignored if set during admin creation. | [optional] 
**pendingInvitation** | **Boolean** | Output only. Indicates whether this admin has a pending invitation for the specified resource. | [optional] [readonly] 
**role** | **String** | Required. Specifies the role that this admin uses with the specified Account or Location. | [optional] 



## Enum: RoleEnum


* `ADMIN_ROLE_UNSPECIFIED` (value: `"ADMIN_ROLE_UNSPECIFIED"`)

* `PRIMARY_OWNER` (value: `"PRIMARY_OWNER"`)

* `OWNER` (value: `"OWNER"`)

* `MANAGER` (value: `"MANAGER"`)

* `SITE_MANAGER` (value: `"SITE_MANAGER"`)




