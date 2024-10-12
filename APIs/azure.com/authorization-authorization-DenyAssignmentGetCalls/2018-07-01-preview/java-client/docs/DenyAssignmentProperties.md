

# DenyAssignmentProperties

Deny assignment properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**denyAssignmentName** | **String** | The display name of the deny assignment. |  [optional] |
|**description** | **String** | The description of the deny assignment. |  [optional] |
|**doNotApplyToChildScopes** | **Boolean** | Determines if the deny assignment applies to child scopes. Default value is false. |  [optional] |
|**excludePrincipals** | [**List&lt;Principal&gt;**](Principal.md) | Array of principals to which the deny assignment does not apply. |  [optional] |
|**isSystemProtected** | **Boolean** | Specifies whether this deny assignment was created by Azure and cannot be edited or deleted. |  [optional] |
|**permissions** | [**List&lt;DenyAssignmentPermission&gt;**](DenyAssignmentPermission.md) | An array of permissions that are denied by the deny assignment. |  [optional] |
|**principals** | [**List&lt;Principal&gt;**](Principal.md) | Array of principals to which the deny assignment applies. |  [optional] |
|**scope** | **String** | The deny assignment scope. |  [optional] |



