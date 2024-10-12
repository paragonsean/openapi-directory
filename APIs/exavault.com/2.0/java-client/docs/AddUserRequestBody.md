

# AddUserRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email address for the user |  |
|**expiration** | **String** | Optional timestamp when the user should expire, formatted in date-time. |  [optional] |
|**homeResource** | **String** | Resource identifier for the user&#39;s home folder. See details on [how to specify resources](#section/Identifying-Resources) above.  The user will be locked to this directory and unable to move &#39;up&#39; in the account. If the folder does not exist in the account, it will be created when the user is created.   Users with the &#x60;role&#x60; **admin** should have their homeResource set to &#39;/&#39; |  |
|**locked** | **Boolean** | If true, the user will not be able to log in |  [optional] |
|**nickname** | **String** | An optional nickname (e.g. &#39;David from Sales&#39;). |  [optional] |
|**onboarding** | **Boolean** | Set this to **true** to enable extra help popups in the web file manager for this user. |  [optional] |
|**password** | **String** | Password for the user |  |
|**permissions** | [**AddUserRequestBodyPermissions**](AddUserRequestBodyPermissions.md) |  |  |
|**role** | [**RoleEnum**](#RoleEnum) | The type of user to create, either **user** or **admin**. |  |
|**timeZone** | **String** | Time zone, used for accurate time display within the application. See &lt;a href&#x3D;&#39;https://php.net/manual/en/timezones.php&#39; target&#x3D;&#39;blank&#39;&gt;this page&lt;/a&gt; for allowed values.  |  |
|**username** | **String** | Username of the user to create. This should follow standard username conventions - spaces are not allowed, etc. We do allow email addresses as usernames.  **Note** Usernames must be unique across all ExaVault accounts. |  |
|**welcomeEmail** | **Boolean** | If **true**, send this new user a welcome email upon creation. The content of the welcome email can be configured with the [PATCH /accounts](#operation/updateAccount) method. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| ADMIN | &quot;admin&quot; |



