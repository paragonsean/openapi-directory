

# SiteEntity

Show site settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeSftpHostKeyId** | **Integer** | Id of the currently selected custom SFTP Host Key |  [optional] |
|**adminUserId** | **Integer** | User ID for the main site administrator |  [optional] |
|**allowBundleNames** | **Boolean** | Are manual Bundle names allowed? |  [optional] |
|**allowed2faMethodBypassForFtpSftpDav** | **Boolean** | Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV? |  [optional] |
|**allowed2faMethodSms** | **Boolean** | Is SMS two factor authentication allowed? |  [optional] |
|**allowed2faMethodTotp** | **Boolean** | Is TOTP two factor authentication allowed? |  [optional] |
|**allowed2faMethodU2f** | **Boolean** | Is U2F two factor authentication allowed? |  [optional] |
|**allowed2faMethodWebauthn** | **Boolean** | Is WebAuthn two factor authentication allowed? |  [optional] |
|**allowed2faMethodYubi** | **Boolean** | Is yubikey two factor authentication allowed? |  [optional] |
|**allowedCountries** | **String** | Comma seperated list of allowed Country codes |  [optional] |
|**allowedIps** | **String** | List of allowed IP addresses |  [optional] |
|**askAboutOverwrites** | **Boolean** | If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface. |  [optional] |
|**bundleActivityNotifications** | [**BundleActivityNotificationsEnum**](#BundleActivityNotificationsEnum) | Do Bundle owners receive activity notifications? |  [optional] |
|**bundleExpiration** | **Integer** | Site-wide Bundle expiration in days |  [optional] |
|**bundlePasswordRequired** | **Boolean** | Do Bundles require password protection? |  [optional] |
|**bundleRegistrationNotifications** | [**BundleRegistrationNotificationsEnum**](#BundleRegistrationNotificationsEnum) | Do Bundle owners receive registration notification? |  [optional] |
|**bundleRequireShareRecipient** | **Boolean** | Do Bundles require recipients for sharing? |  [optional] |
|**bundleUploadReceiptNotifications** | [**BundleUploadReceiptNotificationsEnum**](#BundleUploadReceiptNotificationsEnum) | Do Bundle uploaders receive upload confirmation notifications? |  [optional] |
|**bundleWatermarkAttachment** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**bundleWatermarkValue** | **Object** | Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value |  [optional] |
|**color2Left** | **String** | Page link and button color |  [optional] |
|**color2Link** | **String** | Top bar link color |  [optional] |
|**color2Text** | **String** | Page link and button color |  [optional] |
|**color2Top** | **String** | Top bar background color |  [optional] |
|**color2TopText** | **String** | Top bar text color |  [optional] |
|**contactName** | **String** | Site main contact name |  [optional] |
|**createdAt** | **OffsetDateTime** | Time this site was created |  [optional] |
|**currency** | **String** | Preferred currency |  [optional] |
|**customNamespace** | **Boolean** | Is this site using a custom namespace for users? |  [optional] |
|**daysToRetainBackups** | **Integer** | Number of days to keep deleted files |  [optional] |
|**defaultTimeZone** | **String** | Site default time zone |  [optional] |
|**desktopApp** | **Boolean** | Is the desktop app enabled? |  [optional] |
|**desktopAppSessionIpPinning** | **Boolean** | Is desktop app session IP pinning enabled? |  [optional] |
|**desktopAppSessionLifetime** | **Integer** | Desktop app session lifetime (in hours) |  [optional] |
|**disableFilesCertificateGeneration** | **Boolean** | If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain. |  [optional] |
|**disableNotifications** | **Boolean** | Are notifications disabled? |  [optional] |
|**disablePasswordReset** | **Boolean** | Is password reset disabled? |  [optional] |
|**disableUsersFromInactivityPeriodDays** | **Integer** | If greater than zero, users will unable to login if they do not show activity within this number of days. |  [optional] |
|**disallowedCountries** | **String** | Comma seperated list of disallowed Country codes |  [optional] |
|**domain** | **String** | Custom domain |  [optional] |
|**domainHstsHeader** | **Boolean** | Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain? |  [optional] |
|**domainLetsencryptChain** | [**DomainLetsencryptChainEnum**](#DomainLetsencryptChainEnum) | Letsencrypt chain to use when registering SSL Certificate for domain. |  [optional] |
|**email** | **String** | Main email for this site |  [optional] |
|**folderPermissionsGroupsOnly** | **Boolean** | If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user. |  [optional] |
|**ftpEnabled** | **Boolean** | Is FTP enabled? |  [optional] |
|**hipaa** | **Boolean** | Is there a signed HIPAA BAA between Files.com and this site? |  [optional] |
|**icon128** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**icon16** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**icon32** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**icon48** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**immutableFilesSetAt** | **OffsetDateTime** | Can files be modified? |  [optional] |
|**includePasswordInWelcomeEmail** | **Boolean** | Include password in emails to new users? |  [optional] |
|**language** | **String** | Site default language |  [optional] |
|**ldapBaseDn** | **String** | Base DN for looking up users in LDAP server |  [optional] |
|**ldapDomain** | **String** | Domain name that will be appended to usernames |  [optional] |
|**ldapEnabled** | **Boolean** | Main LDAP setting: is LDAP enabled? |  [optional] |
|**ldapGroupAction** | **String** | Should we sync groups from LDAP server? |  [optional] |
|**ldapGroupExclusion** | **String** | Comma or newline separated list of group names (with optional wildcards) to exclude when syncing. |  [optional] |
|**ldapGroupInclusion** | **String** | Comma or newline separated list of group names (with optional wildcards) to include when syncing. |  [optional] |
|**ldapHost** | **String** | LDAP host |  [optional] |
|**ldapHost2** | **String** | LDAP backup host |  [optional] |
|**ldapHost3** | **String** | LDAP backup host |  [optional] |
|**ldapPort** | **Integer** | LDAP port |  [optional] |
|**ldapSecure** | **Boolean** | Use secure LDAP? |  [optional] |
|**ldapType** | **String** | LDAP type |  [optional] |
|**ldapUserAction** | **String** | Should we sync users from LDAP server? |  [optional] |
|**ldapUserIncludeGroups** | **String** | Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced. |  [optional] |
|**ldapUsername** | **String** | Username for signing in to LDAP server. |  [optional] |
|**ldapUsernameField** | **String** | LDAP username field |  [optional] |
|**loginHelpText** | **String** | Login help text |  [optional] |
|**logo** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**maxPriorPasswords** | **Integer** | Number of prior passwords to disallow |  [optional] |
|**mobileApp** | **Boolean** | Is the mobile app enabled? |  [optional] |
|**mobileAppSessionIpPinning** | **Boolean** | Is mobile app session IP pinning enabled? |  [optional] |
|**mobileAppSessionLifetime** | **Integer** | Mobile app session lifetime (in hours) |  [optional] |
|**motdText** | **String** | A message to show users when they connect via FTP or SFTP. |  [optional] |
|**motdUseForFtp** | **Boolean** | Show message to users connecting via FTP |  [optional] |
|**motdUseForSftp** | **Boolean** | Show message to users connecting via SFTP |  [optional] |
|**name** | **String** | Site name |  [optional] |
|**nextBillingAmount** | **Double** | Next billing amount |  [optional] |
|**nextBillingDate** | **String** | Next billing date |  [optional] |
|**nonSsoGroupsAllowed** | **Boolean** | If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider. |  [optional] |
|**nonSsoUsersAllowed** | **Boolean** | If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider. |  [optional] |
|**officeIntegrationAvailable** | **Boolean** | Allow users to use Office for the web? |  [optional] |
|**officeIntegrationType** | [**OfficeIntegrationTypeEnum**](#OfficeIntegrationTypeEnum) | Office integration application used to edit and view the MS Office documents |  [optional] |
|**oncehubLink** | **String** | Link to scheduling a meeting with our Sales team |  [optional] |
|**optOutGlobal** | **Boolean** | Use servers in the USA only? |  [optional] |
|**overdue** | **Boolean** | Is this site&#39;s billing overdue? |  [optional] |
|**passwordMinLength** | **Integer** | Shortest password length for users |  [optional] |
|**passwordRequireLetter** | **Boolean** | Require a letter in passwords? |  [optional] |
|**passwordRequireMixed** | **Boolean** | Require lower and upper case letters in passwords? |  [optional] |
|**passwordRequireNumber** | **Boolean** | Require a number in passwords? |  [optional] |
|**passwordRequireSpecial** | **Boolean** | Require special characters in password? |  [optional] |
|**passwordRequireUnbreached** | **Boolean** | Require passwords that have not been previously breached? (see https://haveibeenpwned.com/) |  [optional] |
|**passwordRequirementsApplyToBundles** | **Boolean** | Require bundles&#39; passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users&#39; passwords? |  [optional] |
|**passwordValidityDays** | **Integer** | Number of days password is valid |  [optional] |
|**phone** | **String** | Site phone number |  [optional] |
|**pinAllRemoteServersToSiteRegion** | **Boolean** | If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings. |  [optional] |
|**replyToEmail** | **String** | Reply-to email for this site |  [optional] |
|**require2fa** | **Boolean** | Require two-factor authentication for all users? |  [optional] |
|**require2faStopTime** | **OffsetDateTime** | If set, requirement for two-factor authentication has been scheduled to end on this date-time. |  [optional] |
|**require2faUserType** | [**Require2faUserTypeEnum**](#Require2faUserTypeEnum) | What type of user is required to use two-factor authentication (when require_2fa is set to &#x60;true&#x60; for this site)? |  [optional] |
|**session** | [**SessionEntity**](SessionEntity.md) |  |  [optional] |
|**sessionExpiry** | **Double** | Session expiry in hours |  [optional] |
|**sessionExpiryMinutes** | **Integer** | Session expiry in minutes |  [optional] |
|**sessionPinnedByIp** | **Boolean** | Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?) |  [optional] |
|**sftpEnabled** | **Boolean** | Is SFTP enabled? |  [optional] |
|**sftpHostKeyType** | [**SftpHostKeyTypeEnum**](#SftpHostKeyTypeEnum) | Sftp Host Key Type |  [optional] |
|**sftpInsecureCiphers** | **Boolean** | Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -&gt; True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure. |  [optional] |
|**sftpUserRootEnabled** | **Boolean** | Use user FTP roots also for SFTP? |  [optional] |
|**sharingEnabled** | **Boolean** | Allow bundle creation |  [optional] |
|**showRequestAccessLink** | **Boolean** | Show request access link for users without access?  Currently unused. |  [optional] |
|**siteFooter** | **String** | Custom site footer text |  [optional] |
|**siteHeader** | **String** | Custom site header text |  [optional] |
|**smtpAddress** | **String** | SMTP server hostname or IP |  [optional] |
|**smtpAuthentication** | **String** | SMTP server authentication type |  [optional] |
|**smtpFrom** | **String** | From address to use when mailing through custom SMTP |  [optional] |
|**smtpPort** | **Integer** | SMTP server port |  [optional] |
|**smtpUsername** | **String** | SMTP server username |  [optional] |
|**sslRequired** | **Boolean** | Is SSL required?  Disabling this is insecure. |  [optional] |
|**subdomain** | **String** | Site subdomain |  [optional] |
|**switchToPlanDate** | **OffsetDateTime** | If switching plans, when does the new plan take effect? |  [optional] |
|**tlsDisabled** | **Boolean** | Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure. |  [optional] |
|**trialDaysLeft** | **Integer** | Number of days left in trial |  [optional] |
|**trialUntil** | **OffsetDateTime** | When does this Site trial expire? |  [optional] |
|**updatedAt** | **OffsetDateTime** | Last time this Site was updated |  [optional] |
|**uploadsViaEmailAuthentication** | **Boolean** | Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC? |  [optional] |
|**useProvidedModifiedAt** | **Boolean** | Allow uploaders to set &#x60;provided_modified_at&#x60; for uploaded files? |  [optional] |
|**user** | [**UserEntity**](UserEntity.md) |  |  [optional] |
|**userLockout** | **Boolean** | Will users be locked out after incorrect login attempts? |  [optional] |
|**userLockoutLockPeriod** | **Integer** | How many hours to lock user out for failed password? |  [optional] |
|**userLockoutTries** | **Integer** | Number of login tries within &#x60;user_lockout_within&#x60; hours before users are locked out |  [optional] |
|**userLockoutWithin** | **Integer** | Number of hours for user lockout window |  [optional] |
|**userRequestsEnabled** | **Boolean** | Enable User Requests feature |  [optional] |
|**userRequestsNotifyAdmins** | **Boolean** | Send email to site admins when a user request is received? |  [optional] |
|**welcomeCustomText** | **String** | Custom text send in user welcome email |  [optional] |
|**welcomeEmailCc** | **String** | Include this email in welcome emails if enabled |  [optional] |
|**welcomeEmailEnabled** | **Boolean** | Will the welcome email be sent to new users? |  [optional] |
|**welcomeEmailSubject** | **String** | Include this email subject in welcome emails if enabled |  [optional] |
|**welcomeScreen** | [**WelcomeScreenEnum**](#WelcomeScreenEnum) | Does the welcome screen appear? |  [optional] |
|**windowsModeFtp** | **Boolean** | Does FTP user Windows emulation mode? |  [optional] |



## Enum: BundleActivityNotificationsEnum

| Name | Value |
|---- | -----|
| NEVER | &quot;never&quot; |
| ALWAYS | &quot;always&quot; |
| PER_BUNDLE_SETTING | &quot;per_bundle_setting&quot; |



## Enum: BundleRegistrationNotificationsEnum

| Name | Value |
|---- | -----|
| NEVER | &quot;never&quot; |
| ALWAYS | &quot;always&quot; |
| PER_BUNDLE_SETTING | &quot;per_bundle_setting&quot; |



## Enum: BundleUploadReceiptNotificationsEnum

| Name | Value |
|---- | -----|
| NEVER | &quot;never&quot; |
| ALWAYS | &quot;always&quot; |
| PER_BUNDLE_SETTING | &quot;per_bundle_setting&quot; |



## Enum: DomainLetsencryptChainEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| ISRG_ROOT_X1 | &quot;isrg_root_x1&quot; |
| DST_ROOT_CA_X3 | &quot;dst_root_ca_x3&quot; |



## Enum: OfficeIntegrationTypeEnum

| Name | Value |
|---- | -----|
| ONLY_OFFICE | &quot;only_office&quot; |
| OFFICE_365 | &quot;office_365&quot; |
| DISABLED | &quot;disabled&quot; |



## Enum: Require2faUserTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| FOLDER_AND_SITE_ADMINS | &quot;folder_and_site_admins&quot; |
| SITE_ADMINS | &quot;site_admins&quot; |



## Enum: SftpHostKeyTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| EXAVAULT | &quot;exavault&quot; |
| CUSTOM | &quot;custom&quot; |



## Enum: WelcomeScreenEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| HIDDEN | &quot;hidden&quot; |
| DISABLED | &quot;disabled&quot; |



