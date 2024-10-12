

# User

Active Directory user information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountEnabled** | **Boolean** | Whether the account is enabled. |  [optional] |
|**displayName** | **String** | The display name of the user. |  [optional] |
|**givenName** | **String** | The given name for the user. |  [optional] |
|**immutableId** | **String** | This must be specified if you are using a federated domain for the user&#39;s userPrincipalName (UPN) property when creating a new user account. It is used to associate an on-premises Active Directory user account with their Azure AD user object. |  [optional] |
|**mail** | **String** | The primary email address of the user. |  [optional] |
|**mailNickname** | **String** | The mail alias for the user. |  [optional] |
|**signInNames** | **List&lt;SignInName&gt;** | The sign-in names of the user. |  [optional] |
|**surname** | **String** | The user&#39;s surname (family name or last name). |  [optional] |
|**usageLocation** | **String** | A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. Examples include: \&quot;US\&quot;, \&quot;JP\&quot;, and \&quot;GB\&quot;. |  [optional] |
|**userPrincipalName** | **String** | The principal name of the user. |  [optional] |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | A string value that can be used to classify user types in your directory, such as &#39;Member&#39; and &#39;Guest&#39;. |  [optional] |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| MEMBER | &quot;Member&quot; |
| GUEST | &quot;Guest&quot; |



