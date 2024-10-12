

# AppRole


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedMemberTypes** | **List&lt;String&gt;** | Specifies whether this app role definition can be assigned to users and groups by setting to &#39;User&#39;, or to other applications (that are accessing this application in daemon service scenarios) by setting to &#39;Application&#39;, or to both.  |  [optional] |
|**description** | **String** | Permission help text that appears in the admin app assignment and consent experiences. |  [optional] |
|**displayName** | **String** | Display name for the permission that appears in the admin consent and app assignment experiences. |  [optional] |
|**id** | **String** | Unique role identifier inside the appRoles collection. |  [optional] |
|**isEnabled** | **Boolean** | When creating or updating a role definition, this must be set to true (which is the default). To delete a role, this must first be set to false. At that point, in a subsequent call, this role may be removed. |  [optional] |
|**value** | **String** | Specifies the value of the roles claim that the application should expect in the authentication and access tokens. |  [optional] |



