

# CreateUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**username** | **String** | The user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [a-zA-Z0-9_-.\\@]+. |  |
|**password** | **String** | The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password. |  [optional] |
|**identityInfo** | [**CreateUserRequestIdentityInfo**](CreateUserRequestIdentityInfo.md) |  |  [optional] |
|**phoneConfig** | [**CreateUserRequestPhoneConfig**](CreateUserRequestPhoneConfig.md) |  |  |
|**directoryUserId** | **String** | &lt;p&gt;The identifier of the user account in the directory used for identity management. If Amazon Connect cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Amazon Connect cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.&lt;/p&gt; &lt;p&gt;This parameter is required if you are using an existing directory for identity management in Amazon Connect when Amazon Connect cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.&lt;/p&gt; |  [optional] |
|**securityProfileIds** | **List&lt;String&gt;** | The identifier of the security profile for the user. |  |
|**routingProfileId** | **String** | The identifier of the routing profile for the user. |  |
|**hierarchyGroupId** | **String** | The identifier of the hierarchy group for the user. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



