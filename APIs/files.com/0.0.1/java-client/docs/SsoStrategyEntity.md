

# SsoStrategyEntity

List Sso Strategies

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deprovisionBehavior** | [**DeprovisionBehaviorEnum**](#DeprovisionBehaviorEnum) | Method used for deprovisioning users. |  [optional] |
|**deprovisionGroups** | **Boolean** | Auto-deprovision group membership based on group memberships on the SSO side? |  [optional] |
|**deprovisionUsers** | **Boolean** | Auto-deprovision users? |  [optional] |
|**enabled** | **Boolean** | Is strategy enabled?  This may become automatically set to &#x60;false&#x60; after a high number and duration of failures. |  [optional] |
|**id** | **Integer** | ID |  [optional] |
|**label** | **String** | Custom label for the SSO provider on the login page. |  [optional] |
|**ldapBaseDn** | **String** | Base DN for looking up users in LDAP server |  [optional] |
|**ldapDomain** | **String** | Domain name that will be appended to LDAP usernames |  [optional] |
|**ldapHost** | **String** | LDAP host |  [optional] |
|**ldapHost2** | **String** | LDAP backup host |  [optional] |
|**ldapHost3** | **String** | LDAP backup host |  [optional] |
|**ldapPort** | **Integer** | LDAP port |  [optional] |
|**ldapSecure** | **Boolean** | Use secure LDAP? |  [optional] |
|**ldapUsername** | **String** | Username for signing in to LDAP server. |  [optional] |
|**ldapUsernameField** | [**LdapUsernameFieldEnum**](#LdapUsernameFieldEnum) | LDAP username field |  [optional] |
|**logoUrl** | **String** | URL holding a custom logo for the SSO provider on the login page. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | SSO Protocol |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | Provider name |  [optional] |
|**provisionAttachmentsPermission** | **Boolean** | DEPRECATED: Auto-provisioned users get Sharing permission. Use a Group with the Bundle permission instead. |  [optional] |
|**provisionCompany** | **String** | Default company for auto provisioned users. |  [optional] |
|**provisionDavPermission** | **Boolean** | Auto-provisioned users get WebDAV permission? |  [optional] |
|**provisionEmailSignupGroups** | **String** | Comma-separated list of group names whose members will be created with email_signup authentication. |  [optional] |
|**provisionFtpPermission** | **Boolean** | Auto-provisioned users get FTP permission? |  [optional] |
|**provisionGroupDefault** | **String** | Comma-separated list of group names for groups to automatically add all auto-provisioned users to. |  [optional] |
|**provisionGroupExclusion** | **String** | Comma-separated list of group names for groups (with optional wildcards) that will be excluded from auto-provisioning. |  [optional] |
|**provisionGroupInclusion** | **String** | Comma-separated list of group names for groups (with optional wildcards) that will be auto-provisioned. |  [optional] |
|**provisionGroupRequired** | **String** | Comma or newline separated list of group names (with optional wildcards) to require membership for user provisioning. |  [optional] |
|**provisionGroups** | **Boolean** | Auto-provision group membership based on group memberships on the SSO side? |  [optional] |
|**provisionSftpPermission** | **Boolean** | Auto-provisioned users get SFTP permission? |  [optional] |
|**provisionSiteAdminGroups** | **String** | Comma-separated list of group names whose members will be created as Site Admins. |  [optional] |
|**provisionTimeZone** | **String** | Default time zone for auto provisioned users. |  [optional] |
|**provisionUsers** | **Boolean** | Auto-provision users? |  [optional] |
|**samlProviderCertFingerprint** | **String** | Identity provider sha256 cert fingerprint if saml_provider_metadata_url is not available. |  [optional] |
|**samlProviderIssuerUrl** | **String** | Identity provider issuer url |  [optional] |
|**samlProviderMetadataContent** | **String** | Custom identity provider metadata |  [optional] |
|**samlProviderMetadataUrl** | **String** | Metadata URL for the SAML identity provider |  [optional] |
|**samlProviderSloTargetUrl** | **String** | Identity provider SLO endpoint |  [optional] |
|**samlProviderSsoTargetUrl** | **String** | Identity provider SSO endpoint if saml_provider_metadata_url is not available. |  [optional] |
|**scimAuthenticationMethod** | [**ScimAuthenticationMethodEnum**](#ScimAuthenticationMethodEnum) | SCIM authentication type. |  [optional] |
|**scimOauthAccessToken** | **String** | SCIM OAuth Access Token. |  [optional] |
|**scimOauthAccessTokenExpiresAt** | **String** | SCIM OAuth Access Token Expiration Time. |  [optional] |
|**scimUsername** | **String** | SCIM username. |  [optional] |
|**subdomain** | **String** | Subdomain |  [optional] |



## Enum: DeprovisionBehaviorEnum

| Name | Value |
|---- | -----|
| DISABLE | &quot;disable&quot; |
| DELETE | &quot;delete&quot; |



## Enum: LdapUsernameFieldEnum

| Name | Value |
|---- | -----|
| S_AM_ACCOUNT_NAME | &quot;sAMAccountName&quot; |
| USER_PRINCIPAL_NAME | &quot;userPrincipalName&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| OAUTH2 | &quot;oauth2&quot; |
| _UNUSED_OPENID2 | &quot;_unused_openid2&quot; |
| SAML | &quot;saml&quot; |
| ACTIVE_DIRECTORY | &quot;active_directory&quot; |
| OPEN_LDAP | &quot;open_ldap&quot; |
| SCIM | &quot;scim&quot; |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| AUTH0 | &quot;auth0&quot; |
| OKTA | &quot;okta&quot; |
| ATLASSIAN | &quot;atlassian&quot; |
| AZURE | &quot;azure&quot; |
| BOX | &quot;box&quot; |
| DROPBOX | &quot;dropbox&quot; |
| SLACK | &quot;slack&quot; |
| _UNUSED_UBUNTU | &quot;_unused_ubuntu&quot; |
| ONELOGIN | &quot;onelogin&quot; |
| SAML | &quot;saml&quot; |
| IDAPTIVE | &quot;idaptive&quot; |
| LDAP | &quot;ldap&quot; |
| SCIM | &quot;scim&quot; |



## Enum: ScimAuthenticationMethodEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| BASIC | &quot;basic&quot; |
| TOKEN | &quot;token&quot; |



