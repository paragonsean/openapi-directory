# ExaVault.UserAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTimestamp** | **String** | Timestamp of most recent successful user login. | [optional] 
**accountName** | **String** | Name of the account this user belongs to. | 
**created** | **Date** | Timestamp of user creation. | 
**email** | **String** | Email address of the user. | [optional] 
**expiration** | **String** | Timestamp of user expiration. | [optional] 
**firstLogin** | **Boolean** | &#x60;true&#x60; if the user has logged into the system. | [optional] 
**homePath** | **String** | Path to the user&#39;s home folder. | [optional] 
**locked** | **Boolean** | &#x60;true&#x60; if the user is locked and cannot log in. | [optional] 
**modified** | **Date** | Timestamp of user modification. | 
**nickname** | **String** | Nickname of the user. | 
**onboarding** | **Boolean** | Whether the onboarding help system is enabled for this user. &#x60;true&#x60; means that additional help popups are displayed in the web application for this user. | 
**permissions** | [**UserPermissions**](UserPermissions.md) |  | 
**role** | **String** | User&#39;s access level | 
**status** | **Number** | Indicates user activity status. &#x60;0&#x60; means the user is locked and cannot log in. &#x60;1&#x60; means the user is active and can log in. | 
**timeZone** | **String** | User&#39;s timezone. See &lt;a href&#x3D;&#39;https://php.net/manual/en/timezones.php&#39; target&#x3D;&#39;blank&#39;&gt;this page&lt;/a&gt; for allowed values. | 
**username** | **String** | Username of the user. | 



## Enum: RoleEnum


* `user` (value: `"user"`)

* `admin` (value: `"admin"`)

* `master` (value: `"master"`)





## Enum: StatusEnum


* `0` (value: `0`)

* `1` (value: `1`)




