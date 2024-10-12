

# AdvancedLdapConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupMaxLevel** | **Integer** | Maximum level of groups to query. Set to 1 to query the immediate groups to which a user belongs. Leave blank to query all the groups to which a user belongs. Valid values are between 1 and 50 inclusive. When ldapSearchAcrossIntegrations is set to be true, this value is ignored. When this value is set, then for this ldap service, ldapActiveDirectoryDisableMatchingRuleInChain is ignored and assumed to be true. |  [optional] |
|**groupMemberAttribute** | **String** | LDAP field that contains the group members. For example, Active Directory uses the field \&quot;member\&quot;. |  [optional] |
|**groupMembershipAttribute** | **String** | Points to the group that this entry belongs to. For example, Active Directory uses the field \&quot;memberOf\&quot;. |  [optional] |
|**groupSearchFilter** | **String** | A string representation of the LDAP group search filter in RFC4515 format. For example, a group search filter for Active Directory has the string representation (objectCategory&#x3D;group). |  [optional] |
|**userNameSearchAttribute** | **String** | Specifies the user name. Active Directory searches can use the attributes sAMAccountName and userPrincipalName. |  [optional] |
|**userSearchFilter** | **String** | A string representation of the LDAP user search filter in RFC4515 format. For example, an Active Directory user search filter that selects all enabled user objects has the following string representation (&amp;(objectCategory&#x3D;person) (objectClass&#x3D;user) (!(userAccountControl:1.2.840.113556.1.4.803:&#x3D;2))). |  [optional] |



