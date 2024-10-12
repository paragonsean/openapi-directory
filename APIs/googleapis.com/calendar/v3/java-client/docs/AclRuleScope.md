

# AclRuleScope

The extent to which calendar access is granted by this ACL rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | The type of the scope. Possible values are:   - \&quot;default\&quot; - The public scope. This is the default value.  - \&quot;user\&quot; - Limits the scope to a single user.  - \&quot;group\&quot; - Limits the scope to a group.  - \&quot;domain\&quot; - Limits the scope to a domain.  Note: The permissions granted to the \&quot;default\&quot;, or public, scope apply to any user, authenticated or not. |  [optional] |
|**value** | **String** | The email address of a user or group, or the name of a domain, depending on the scope type. Omitted for type \&quot;default\&quot;. |  [optional] |



