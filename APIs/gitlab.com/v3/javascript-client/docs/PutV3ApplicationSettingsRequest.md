# Gitlab.PutV3ApplicationSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultBranchProtection** | **Number** | Determine if developers can push to master | [optional] 
**defaultProjectVisibility** | **Number** | The default project visibility | [optional] 
**defaultSnippetVisibility** | **Number** | The default snippet visibility | [optional] 
**defaultGroupVisibility** | **Number** | The default group visibility | [optional] 
**restrictedVisibilityLevels** | **[String]** | Selected levels cannot be used by non-admin users for projects or snippets. If the public level is restricted, user profiles are only visible to logged in users. | [optional] 
**importSources** | **[String]** | Enabled sources for code import during project creation. OmniAuth must be configured for GitHub, Bitbucket, and GitLab.com | [optional] 
**disabledOauthSignInSources** | **[String]** | Disable certain OAuth sign-in sources | [optional] 
**enabledGitAccessProtocol** | **String** | Allow only the selected protocols to be used for Git access. | [optional] 
**gravatarEnabled** | **Boolean** | Flag indicating if the Gravatar service is enabled | [optional] 
**defaultProjectsLimit** | **Number** | The maximum number of personal projects | [optional] 
**maxAttachmentSize** | **Number** | Maximum attachment size in MB | [optional] 
**sessionExpireDelay** | **Number** | Session duration in minutes. GitLab restart is required to apply changes. | [optional] 
**userOauthApplications** | **Boolean** | Allow users to register any application to use GitLab as an OAuth provider | [optional] 
**userDefaultExternal** | **Boolean** | Newly registered users will by default be external | [optional] 
**signupEnabled** | **Boolean** | Flag indicating if sign up is enabled | [optional] 
**sendUserConfirmationEmail** | **Boolean** | Send confirmation email on sign-up | [optional] 
**domainWhitelist** | **String** | ONLY users with e-mail addresses that match these domain(s) will be able to sign-up. Wildcards allowed. Use separate lines for multiple entries. Ex: domain.com, *.domain.com | [optional] 
**domainBlacklistEnabled** | **Boolean** | Enable domain blacklist for sign ups | [optional] 
**domainBlacklist** | **String** | Users with e-mail addresses that match these domain(s) will NOT be able to sign-up. Wildcards allowed. Use separate lines for multiple entries. Ex: domain.com, *.domain.com | 
**afterSignUpText** | **String** | Text shown after sign up | [optional] 
**signinEnabled** | **Boolean** | Flag indicating if sign in is enabled | [optional] 
**requireTwoFactorAuthentication** | **Boolean** | Require all users to setup Two-factor authentication | [optional] 
**twoFactorGracePeriod** | **Number** | Amount of time (in hours) that users are allowed to skip forced configuration of two-factor authentication | 
**homePageUrl** | **String** | We will redirect non-logged in users to this page | [optional] 
**afterSignOutPath** | **String** | We will redirect users to this page after they sign out | [optional] 
**signInText** | **String** | The sign in text of the GitLab application | [optional] 
**helpPageText** | **String** | Custom text displayed on the help page | [optional] 
**sharedRunnersEnabled** | **Boolean** | Enable shared runners for new projects | [optional] 
**sharedRunnersText** | **String** | Shared runners text  | 
**maxArtifactsSize** | **Number** | Set the maximum file size each build&#39;s artifacts can have | [optional] 
**containerRegistryTokenExpireDelay** | **Number** | Authorization token duration (minutes) | [optional] 
**metricsEnabled** | **Boolean** | Enable the InfluxDB metrics | [optional] 
**metricsHost** | **String** | The InfluxDB host | 
**metricsPort** | **Number** | The UDP port to use for connecting to InfluxDB | 
**metricsPoolSize** | **Number** | The amount of InfluxDB connections to open | 
**metricsTimeout** | **Number** | The amount of seconds after which an InfluxDB connection will time out | 
**metricsMethodCallThreshold** | **Number** | A method call is only tracked when it takes longer to complete than the given amount of milliseconds. | 
**metricsSampleInterval** | **Number** | The sampling interval in seconds | 
**metricsPacketSize** | **Number** | The amount of points to store in a single UDP packet | 
**sidekiqThrottlingEnabled** | **Boolean** | Enable Sidekiq Job Throttling | [optional] 
**sidekiqThrottlingQueus** | **[String]** | Choose which queues you wish to throttle | 
**sidekiqThrottlingFactor** | **Number** | The factor by which the queues should be throttled. A value between 0.0 and 1.0, exclusive. | 
**recaptchaEnabled** | **Boolean** | Helps prevent bots from creating accounts | [optional] 
**recaptchaSiteKey** | **String** | Generate site key at http://www.google.com/recaptcha | 
**recaptchaPrivateKey** | **String** | Generate private key at http://www.google.com/recaptcha | 
**akismetEnabled** | **Boolean** | Helps prevent bots from creating issues | [optional] 
**akismetApiKey** | **String** | Generate API key at http://www.akismet.com | 
**adminNotificationEmail** | **String** | Abuse reports will be sent to this address if it is set. Abuse reports are always available in the admin area. | [optional] 
**sentryEnabled** | **Boolean** | Sentry is an error reporting and logging tool which is currently not shipped with GitLab, get it here: https://getsentry.com | [optional] 
**sentryDsn** | **String** | Sentry Data Source Name | 
**repositoryStorage** | **String** | Storage paths for new projects | [optional] 
**repositoryChecksEnabled** | **Boolean** | GitLab will periodically run &#39;git fsck&#39; in all project and wiki repositories to look for silent disk corruption issues. | [optional] 
**kodingEnabled** | **Boolean** | Enable Koding | [optional] 
**kodingUrl** | **String** | The Koding team URL | 
**plantumlEnabled** | **Boolean** | Enable PlantUML | [optional] 
**plantumlUrl** | **String** | The PlantUML server URL | 
**versionCheckEnabled** | **Boolean** | Let GitLab inform you when an update is available. | [optional] 
**emailAuthorInBody** | **Boolean** | Some email servers do not support overriding the email sender name. Enable this option to include the name of the author of the issue, merge request or comment in the email body instead. | [optional] 
**htmlEmailsEnabled** | **Boolean** | By default GitLab sends emails in HTML and plain text formats so mail clients can choose what format to use. Disable this option if you only want to send emails in plain text format. | [optional] 
**housekeepingEnabled** | **Boolean** | Enable automatic repository housekeeping (git repack, git gc) | [optional] 
**housekeepingBitmapsEnabled** | **Boolean** | Creating pack file bitmaps makes housekeeping take a little longer but bitmaps should accelerate &#39;git clone&#39; performance. | 
**housekeepingIncrementalRepackPeriod** | **Number** | Number of Git pushes after which an incremental &#39;git repack&#39; is run. | 
**housekeepingFullRepackPeriod** | **Number** | Number of Git pushes after which a full &#39;git repack&#39; is run. | 
**housekeepingGcPeriod** | **Number** | Number of Git pushes after which &#39;git gc&#39; is run. | 



## Enum: DefaultBranchProtectionEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: DefaultProjectVisibilityEnum


* `0` (value: `0`)

* `10` (value: `10`)

* `20` (value: `20`)





## Enum: DefaultSnippetVisibilityEnum


* `0` (value: `0`)

* `10` (value: `10`)

* `20` (value: `20`)





## Enum: DefaultGroupVisibilityEnum


* `0` (value: `0`)

* `10` (value: `10`)

* `20` (value: `20`)





## Enum: ImportSourcesEnum






## Enum: EnabledGitAccessProtocolEnum


* `ssh` (value: `"ssh"`)

* `http` (value: `"http"`)

* `nil` (value: `"nil"`)




