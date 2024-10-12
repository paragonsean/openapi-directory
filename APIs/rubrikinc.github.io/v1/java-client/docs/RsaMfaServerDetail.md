

# RsaMfaServerDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Specifies the name to identify MFA server configuration.  |  |
|**timeout** | **Integer** | Specifies a number of seconds to wait for server response to a given authentication method.  |  |
|**assurancePolicyName** | **String** | The name of a Cloud Authentication Service policy. This setting is only required for RSA Cloud Service configurations.  |  [optional] |
|**baseUrl** | **String** | The base url for RSA REST API server including the host name and port number. A valid input looks like https://&lt;SECURID_ACCESS_HOST &gt;:&lt;REST_API_PORT&gt;/mfa/v1_1.  |  |
|**certificateId** | **String** | ID corresponding to the imported certificate. |  [optional] |
|**clientId** | **String** | A unique name to identify the client. When the client is configured to use RSA Authentication Manager, the client ID must match an authentication agent name.  |  [optional] |
|**ldapUsernameAttribute** | **String** | LDAP attribute to query the username used for performing MFA.  |  |
|**id** | **String** | Unique server identifier. |  |



