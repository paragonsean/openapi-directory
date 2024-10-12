# RubrikRestApi.LdapServiceSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedOptions** | [**AdvancedLdapConfiguration**](AdvancedLdapConfiguration.md) |  | [optional] 
**authServers** | **[String]** | An ordered list of authentication servers. Servers on this list have priority over servers discovered using dynamic DNS. | [optional] 
**baseDn** | **String** | The path to the directory where searches for users begin. | [optional] 
**bindUserName** | **String** | The name of the user that searches the authentication server for other users. | [optional] 
**certificateId** | **String** | ID of the imported certificate to use for connections to this server. | [optional] 
**domainType** | **String** | Domain type, for example local or LDAP/Active Directory. | 
**dynamicDnsName** | **String** | Dynamic DNS name for locating authentication servers. | [optional] 
**id** | **String** | ID of this authentication domain. | 
**initialRefreshStatus** | **String** | Status message from the initial refresh. | [optional] 
**isTotpEnforced** | **Boolean** | Indicates whether the time-based one time password (TOTP) authentication method is being enforced. Returns true when TOTP is enforced and false when TOTP is not enforced.  | [optional] 
**mfaServerId** | **String** | MFA server associated with LDAP service. | [optional] 
**name** | **String** | Domain name. | 
**serviceAccount** | **String** | Computer account name associated with this cluster. | [optional] 


