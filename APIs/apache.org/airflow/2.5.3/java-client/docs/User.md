

# User

A user object with sensitive data.  *New in version 2.1.0* 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether the user is active |  [optional] [readonly] |
|**changedOn** | **String** | The date user was changed |  [optional] [readonly] |
|**createdOn** | **String** | The date user was created |  [optional] [readonly] |
|**email** | **String** | The user&#39;s email.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  |  [optional] |
|**failedLoginCount** | **Integer** | The number of times the login failed |  [optional] [readonly] |
|**firstName** | **String** | The user&#39;s first name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  |  [optional] |
|**lastLogin** | **String** | The last user login |  [optional] [readonly] |
|**lastName** | **String** | The user&#39;s last name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  |  [optional] |
|**loginCount** | **Integer** | The login count |  [optional] [readonly] |
|**roles** | [**List&lt;UserCollectionItemRolesInner&gt;**](UserCollectionItemRolesInner.md) | User roles.  *Changed in version 2.2.0*&amp;#58; Field is no longer read-only.  |  [optional] |
|**username** | **String** | The username.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  |  [optional] |
|**password** | **String** |  |  [optional] |



