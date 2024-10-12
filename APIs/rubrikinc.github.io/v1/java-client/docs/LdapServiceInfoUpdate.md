

# LdapServiceInfoUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedOptions** | [**AdvancedLdapConfiguration**](AdvancedLdapConfiguration.md) |  |  [optional] |
|**authServers** | **List&lt;String&gt;** | An ordered list of authentication servers. Servers on this list have priority over servers discovered using dynamic DNS. |  [optional] |
|**baseDn** | **String** | The path to the directory where searches for users begin. |  [optional] |
|**bindUserName** | **String** | The name of the user that searches the authentication server for other users. |  [optional] |
|**bindUserPassword** | **String** | Password for the bind user. |  [optional] |
|**certificateId** | **String** | ID of the imported certificate to use for connections to this server. |  [optional] |
|**dynamicDnsName** | **String** | Dynamic DNS name for locating authentication servers. |  [optional] |
|**isTotpEnforced** | **Boolean** | Indicates whether the time-based one time password (TOTP) authentication method is being enforced. Returns true when TOTP is enforced and false when TOTP is not enforced.  |  [optional] |
|**mfaServerId** | **String** | MFA server associated with LDAP service. |  [optional] |
|**name** | **String** | Human friendly name. |  [optional] |



