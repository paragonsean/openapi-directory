# GraphRbacManagementClient.UserBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**givenName** | **String** | The given name for the user. | [optional] 
**immutableId** | **String** | This must be specified if you are using a federated domain for the user&#39;s userPrincipalName (UPN) property when creating a new user account. It is used to associate an on-premises Active Directory user account with their Azure AD user object. | [optional] 
**surname** | **String** | The user&#39;s surname (family name or last name). | [optional] 
**usageLocation** | **String** | A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. Examples include: \&quot;US\&quot;, \&quot;JP\&quot;, and \&quot;GB\&quot;. | [optional] 
**userType** | **String** | A string value that can be used to classify user types in your directory, such as &#39;Member&#39; and &#39;Guest&#39;. | [optional] 



## Enum: UserTypeEnum


* `Member` (value: `"Member"`)

* `Guest` (value: `"Guest"`)




