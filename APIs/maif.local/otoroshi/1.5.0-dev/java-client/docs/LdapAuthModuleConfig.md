

# LdapAuthModuleConfig

Settings to authenticate users using a generic OAuth2 provider

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminPassword** | **String** | The admin password |  |
|**adminUsername** | **String** | The admin username |  |
|**desc** | **String** | Description of the config |  |
|**emailField** | **String** | Field name to get email from user profile |  |
|**groupFilter** | **String** | Filter for groups |  |
|**id** | **String** | Unique id of the config |  |
|**name** | **String** | Name of the config |  |
|**nameField** | **String** | Field name to get name from user profile |  |
|**otoroshiDataField** | **String** | Field name to get otoroshi metadata from. You can specify sub fields using | as separator |  [optional] |
|**searchBase** | **String** | LDAP search base |  |
|**searchFilter** | **String** | Filter for users |  |
|**serverUrl** | **String** | URL of the ldap server |  |
|**sessionMaxAge** | **Integer** | Max age of the session |  |
|**type** | **String** | Type of settings. value is ldap |  |
|**userBase** | **String** | LDAP user base DN |  |



