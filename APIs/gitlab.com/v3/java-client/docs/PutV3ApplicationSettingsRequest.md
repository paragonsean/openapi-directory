

# PutV3ApplicationSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultBranchProtection** | [**DefaultBranchProtectionEnum**](#DefaultBranchProtectionEnum) | Determine if developers can push to master |  [optional] |
|**defaultProjectVisibility** | [**DefaultProjectVisibilityEnum**](#DefaultProjectVisibilityEnum) | The default project visibility |  [optional] |
|**defaultSnippetVisibility** | [**DefaultSnippetVisibilityEnum**](#DefaultSnippetVisibilityEnum) | The default snippet visibility |  [optional] |
|**defaultGroupVisibility** | [**DefaultGroupVisibilityEnum**](#DefaultGroupVisibilityEnum) | The default group visibility |  [optional] |
|**restrictedVisibilityLevels** | **List&lt;String&gt;** | Selected levels cannot be used by non-admin users for projects or snippets. If the public level is restricted, user profiles are only visible to logged in users. |  [optional] |
|**importSources** | [**ImportSourcesEnum**](#ImportSourcesEnum) | Enabled sources for code import during project creation. OmniAuth must be configured for GitHub, Bitbucket, and GitLab.com |  [optional] |
|**disabledOauthSignInSources** | **List&lt;String&gt;** | Disable certain OAuth sign-in sources |  [optional] |
|**enabledGitAccessProtocol** | [**EnabledGitAccessProtocolEnum**](#EnabledGitAccessProtocolEnum) | Allow only the selected protocols to be used for Git access. |  [optional] |
|**gravatarEnabled** | **Boolean** | Flag indicating if the Gravatar service is enabled |  [optional] |
|**defaultProjectsLimit** | **Integer** | The maximum number of personal projects |  [optional] |
|**maxAttachmentSize** | **Integer** | Maximum attachment size in MB |  [optional] |
|**sessionExpireDelay** | **Integer** | Session duration in minutes. GitLab restart is required to apply changes. |  [optional] |
|**userOauthApplications** | **Boolean** | Allow users to register any application to use GitLab as an OAuth provider |  [optional] |
|**userDefaultExternal** | **Boolean** | Newly registered users will by default be external |  [optional] |
|**signupEnabled** | **Boolean** | Flag indicating if sign up is enabled |  [optional] |
|**sendUserConfirmationEmail** | **Boolean** | Send confirmation email on sign-up |  [optional] |
|**domainWhitelist** | **String** | ONLY users with e-mail addresses that match these domain(s) will be able to sign-up. Wildcards allowed. Use separate lines for multiple entries. Ex: domain.com, *.domain.com |  [optional] |
|**domainBlacklistEnabled** | **Boolean** | Enable domain blacklist for sign ups |  [optional] |
|**domainBlacklist** | **String** | Users with e-mail addresses that match these domain(s) will NOT be able to sign-up. Wildcards allowed. Use separate lines for multiple entries. Ex: domain.com, *.domain.com |  |
|**afterSignUpText** | **String** | Text shown after sign up |  [optional] |
|**signinEnabled** | **Boolean** | Flag indicating if sign in is enabled |  [optional] |
|**requireTwoFactorAuthentication** | **Boolean** | Require all users to setup Two-factor authentication |  [optional] |
|**twoFactorGracePeriod** | **Integer** | Amount of time (in hours) that users are allowed to skip forced configuration of two-factor authentication |  |
|**homePageUrl** | **String** | We will redirect non-logged in users to this page |  [optional] |
|**afterSignOutPath** | **String** | We will redirect users to this page after they sign out |  [optional] |
|**signInText** | **String** | The sign in text of the GitLab application |  [optional] |
|**helpPageText** | **String** | Custom text displayed on the help page |  [optional] |
|**sharedRunnersEnabled** | **Boolean** | Enable shared runners for new projects |  [optional] |
|**sharedRunnersText** | **String** | Shared runners text  |  |
|**maxArtifactsSize** | **Integer** | Set the maximum file size each build&#39;s artifacts can have |  [optional] |
|**containerRegistryTokenExpireDelay** | **Integer** | Authorization token duration (minutes) |  [optional] |
|**metricsEnabled** | **Boolean** | Enable the InfluxDB metrics |  [optional] |
|**metricsHost** | **String** | The InfluxDB host |  |
|**metricsPort** | **Integer** | The UDP port to use for connecting to InfluxDB |  |
|**metricsPoolSize** | **Integer** | The amount of InfluxDB connections to open |  |
|**metricsTimeout** | **Integer** | The amount of seconds after which an InfluxDB connection will time out |  |
|**metricsMethodCallThreshold** | **Integer** | A method call is only tracked when it takes longer to complete than the given amount of milliseconds. |  |
|**metricsSampleInterval** | **Integer** | The sampling interval in seconds |  |
|**metricsPacketSize** | **Integer** | The amount of points to store in a single UDP packet |  |
|**sidekiqThrottlingEnabled** | **Boolean** | Enable Sidekiq Job Throttling |  [optional] |
|**sidekiqThrottlingQueus** | **List&lt;String&gt;** | Choose which queues you wish to throttle |  |
|**sidekiqThrottlingFactor** | **Float** | The factor by which the queues should be throttled. A value between 0.0 and 1.0, exclusive. |  |
|**recaptchaEnabled** | **Boolean** | Helps prevent bots from creating accounts |  [optional] |
|**recaptchaSiteKey** | **String** | Generate site key at http://www.google.com/recaptcha |  |
|**recaptchaPrivateKey** | **String** | Generate private key at http://www.google.com/recaptcha |  |
|**akismetEnabled** | **Boolean** | Helps prevent bots from creating issues |  [optional] |
|**akismetApiKey** | **String** | Generate API key at http://www.akismet.com |  |
|**adminNotificationEmail** | **String** | Abuse reports will be sent to this address if it is set. Abuse reports are always available in the admin area. |  [optional] |
|**sentryEnabled** | **Boolean** | Sentry is an error reporting and logging tool which is currently not shipped with GitLab, get it here: https://getsentry.com |  [optional] |
|**sentryDsn** | **String** | Sentry Data Source Name |  |
|**repositoryStorage** | **String** | Storage paths for new projects |  [optional] |
|**repositoryChecksEnabled** | **Boolean** | GitLab will periodically run &#39;git fsck&#39; in all project and wiki repositories to look for silent disk corruption issues. |  [optional] |
|**kodingEnabled** | **Boolean** | Enable Koding |  [optional] |
|**kodingUrl** | **String** | The Koding team URL |  |
|**plantumlEnabled** | **Boolean** | Enable PlantUML |  [optional] |
|**plantumlUrl** | **String** | The PlantUML server URL |  |
|**versionCheckEnabled** | **Boolean** | Let GitLab inform you when an update is available. |  [optional] |
|**emailAuthorInBody** | **Boolean** | Some email servers do not support overriding the email sender name. Enable this option to include the name of the author of the issue, merge request or comment in the email body instead. |  [optional] |
|**htmlEmailsEnabled** | **Boolean** | By default GitLab sends emails in HTML and plain text formats so mail clients can choose what format to use. Disable this option if you only want to send emails in plain text format. |  [optional] |
|**housekeepingEnabled** | **Boolean** | Enable automatic repository housekeeping (git repack, git gc) |  [optional] |
|**housekeepingBitmapsEnabled** | **Boolean** | Creating pack file bitmaps makes housekeeping take a little longer but bitmaps should accelerate &#39;git clone&#39; performance. |  |
|**housekeepingIncrementalRepackPeriod** | **Integer** | Number of Git pushes after which an incremental &#39;git repack&#39; is run. |  |
|**housekeepingFullRepackPeriod** | **Integer** | Number of Git pushes after which a full &#39;git repack&#39; is run. |  |
|**housekeepingGcPeriod** | **Integer** | Number of Git pushes after which &#39;git gc&#39; is run. |  |



## Enum: DefaultBranchProtectionEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: DefaultProjectVisibilityEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_10 | 10 |
| NUMBER_20 | 20 |



## Enum: DefaultSnippetVisibilityEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_10 | 10 |
| NUMBER_20 | 20 |



## Enum: DefaultGroupVisibilityEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_10 | 10 |
| NUMBER_20 | 20 |



## Enum: ImportSourcesEnum

| Name | Value |
|---- | -----|



## Enum: EnabledGitAccessProtocolEnum

| Name | Value |
|---- | -----|
| SSH | &quot;ssh&quot; |
| HTTP | &quot;http&quot; |
| NIL | &quot;nil&quot; |



