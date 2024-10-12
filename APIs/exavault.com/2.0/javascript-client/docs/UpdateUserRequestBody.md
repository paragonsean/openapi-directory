# ExaVault.UpdateUserRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Email address for the user | [optional] 
**expiration** | **String** | Optional timestamp when the user should expire. | [optional] 
**homeResource** | **String** | Resource identifier for the user&#39;s home folder. See details on [how to specify resources](#section/Identifying-Resources) above.  The user will be locked to this directory and unable to move &#39;up&#39; in the account. If the folder does not exist in the account, it will be created when the user logs in.  This setting is ignored for users with the &#x60;role&#x60; **admin**. | [optional] 
**locked** | **Boolean** | If true, the user will be prevented from logging in | [optional] 
**nickname** | **String** | An optional nickname (e.g. &#39;David from Sales&#39;). | [optional] 
**onboarding** | **Boolean** | Set this to **true** to enable extra help popups in the web file manager for this user. | [optional] 
**password** | **String** | New password for the user | [optional] 
**permissions** | [**UserPermissions**](UserPermissions.md) |  | [optional] 
**role** | **String** | The type of user (**admin** or **user**). Note that admin users cannot have a &#x60;homeResource&#x60; other than &#39;/&#39;, and will have full permissions, but you must provide at least \&quot;download,upload,list,delete\&quot; in the &#x60;permissions&#x60; parameter. | [optional] 
**timeZone** | **String** | Time zone, used for accurate time display within the application. See &lt;a href&#x3D;&#39;https://php.net/manual/en/timezones.php&#39; target&#x3D;&#39;blank&#39;&gt;this page&lt;/a&gt; for allowed values.  | [optional] 
**username** | **String** | New username for the user. This should follow standard username conventions - spaces are not allowed, etc. We do allow email addresses as usernames.  **Note** Usernames must be unique across all ExaVault accounts. | [optional] 



## Enum: RoleEnum


* `user` (value: `"user"`)

* `admin` (value: `"admin"`)




