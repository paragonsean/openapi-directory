# FilesComApi.SsoStrategyEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprovisionBehavior** | **String** | Method used for deprovisioning users. | [optional] 
**deprovisionGroups** | **Boolean** | Auto-deprovision group membership based on group memberships on the SSO side? | [optional] 
**deprovisionUsers** | **Boolean** | Auto-deprovision users? | [optional] 
**enabled** | **Boolean** | Is strategy enabled?  This may become automatically set to &#x60;false&#x60; after a high number and duration of failures. | [optional] 
**id** | **Number** | ID | [optional] 
**label** | **String** | Custom label for the SSO provider on the login page. | [optional] 
**ldapBaseDn** | **String** | Base DN for looking up users in LDAP server | [optional] 
**ldapDomain** | **String** | Domain name that will be appended to LDAP usernames | [optional] 
**ldapHost** | **String** | LDAP host | [optional] 
**ldapHost2** | **String** | LDAP backup host | [optional] 
**ldapHost3** | **String** | LDAP backup host | [optional] 
**ldapPort** | **Number** | LDAP port | [optional] 
**ldapSecure** | **Boolean** | Use secure LDAP? | [optional] 
**ldapUsername** | **String** | Username for signing in to LDAP server. | [optional] 
**ldapUsernameField** | **String** | LDAP username field | [optional] 
**logoUrl** | **String** | URL holding a custom logo for the SSO provider on the login page. | [optional] 
**protocol** | **String** | SSO Protocol | [optional] 
**provider** | **String** | Provider name | [optional] 
**provisionAttachmentsPermission** | **Boolean** | DEPRECATED: Auto-provisioned users get Sharing permission. Use a Group with the Bundle permission instead. | [optional] 
**provisionCompany** | **String** | Default company for auto provisioned users. | [optional] 
**provisionDavPermission** | **Boolean** | Auto-provisioned users get WebDAV permission? | [optional] 
**provisionEmailSignupGroups** | **String** | Comma-separated list of group names whose members will be created with email_signup authentication. | [optional] 
**provisionFtpPermission** | **Boolean** | Auto-provisioned users get FTP permission? | [optional] 
**provisionGroupDefault** | **String** | Comma-separated list of group names for groups to automatically add all auto-provisioned users to. | [optional] 
**provisionGroupExclusion** | **String** | Comma-separated list of group names for groups (with optional wildcards) that will be excluded from auto-provisioning. | [optional] 
**provisionGroupInclusion** | **String** | Comma-separated list of group names for groups (with optional wildcards) that will be auto-provisioned. | [optional] 
**provisionGroupRequired** | **String** | Comma or newline separated list of group names (with optional wildcards) to require membership for user provisioning. | [optional] 
**provisionGroups** | **Boolean** | Auto-provision group membership based on group memberships on the SSO side? | [optional] 
**provisionSftpPermission** | **Boolean** | Auto-provisioned users get SFTP permission? | [optional] 
**provisionSiteAdminGroups** | **String** | Comma-separated list of group names whose members will be created as Site Admins. | [optional] 
**provisionTimeZone** | **String** | Default time zone for auto provisioned users. | [optional] 
**provisionUsers** | **Boolean** | Auto-provision users? | [optional] 
**samlProviderCertFingerprint** | **String** | Identity provider sha256 cert fingerprint if saml_provider_metadata_url is not available. | [optional] 
**samlProviderIssuerUrl** | **String** | Identity provider issuer url | [optional] 
**samlProviderMetadataContent** | **String** | Custom identity provider metadata | [optional] 
**samlProviderMetadataUrl** | **String** | Metadata URL for the SAML identity provider | [optional] 
**samlProviderSloTargetUrl** | **String** | Identity provider SLO endpoint | [optional] 
**samlProviderSsoTargetUrl** | **String** | Identity provider SSO endpoint if saml_provider_metadata_url is not available. | [optional] 
**scimAuthenticationMethod** | **String** | SCIM authentication type. | [optional] 
**scimOauthAccessToken** | **String** | SCIM OAuth Access Token. | [optional] 
**scimOauthAccessTokenExpiresAt** | **String** | SCIM OAuth Access Token Expiration Time. | [optional] 
**scimUsername** | **String** | SCIM username. | [optional] 
**subdomain** | **String** | Subdomain | [optional] 



## Enum: DeprovisionBehaviorEnum


* `disable` (value: `"disable"`)

* `delete` (value: `"delete"`)





## Enum: LdapUsernameFieldEnum


* `sAMAccountName` (value: `"sAMAccountName"`)

* `userPrincipalName` (value: `"userPrincipalName"`)





## Enum: ProtocolEnum


* `oauth2` (value: `"oauth2"`)

* `_unused_openid2` (value: `"_unused_openid2"`)

* `saml` (value: `"saml"`)

* `active_directory` (value: `"active_directory"`)

* `open_ldap` (value: `"open_ldap"`)

* `scim` (value: `"scim"`)





## Enum: ProviderEnum


* `google` (value: `"google"`)

* `auth0` (value: `"auth0"`)

* `okta` (value: `"okta"`)

* `atlassian` (value: `"atlassian"`)

* `azure` (value: `"azure"`)

* `box` (value: `"box"`)

* `dropbox` (value: `"dropbox"`)

* `slack` (value: `"slack"`)

* `_unused_ubuntu` (value: `"_unused_ubuntu"`)

* `onelogin` (value: `"onelogin"`)

* `saml` (value: `"saml"`)

* `idaptive` (value: `"idaptive"`)

* `ldap` (value: `"ldap"`)

* `scim` (value: `"scim"`)





## Enum: ScimAuthenticationMethodEnum


* `none` (value: `"none"`)

* `basic` (value: `"basic"`)

* `token` (value: `"token"`)




