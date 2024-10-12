

# UpdateAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agoraOptions** | [**ConfigRequest**](ConfigRequest.md) |  |  [optional] |
|**apnConfig** | [**APNConfigRequest**](APNConfigRequest.md) |  |  [optional] |
|**asyncModerationConfig** | [**AsyncModerationConfigurationRequest**](AsyncModerationConfigurationRequest.md) |  |  [optional] |
|**asyncUrlEnrichEnabled** | **Boolean** |  |  [optional] |
|**autoTranslationEnabled** | **Boolean** |  |  [optional] |
|**beforeMessageSendHookUrl** | **String** |  |  [optional] |
|**cdnExpirationSeconds** | **Integer** |  |  [optional] |
|**channelHideMembersOnly** | **Boolean** |  |  [optional] |
|**customActionHandlerUrl** | **String** |  |  [optional] |
|**disableAuthChecks** | **Boolean** |  |  [optional] |
|**disablePermissionsChecks** | **Boolean** |  |  [optional] |
|**enforceUniqueUsernames** | [**EnforceUniqueUsernamesEnum**](#EnforceUniqueUsernamesEnum) |  |  [optional] |
|**fileUploadConfig** | [**FileUploadConfigRequest**](FileUploadConfigRequest.md) |  |  [optional] |
|**firebaseConfig** | [**FirebaseConfigRequest**](FirebaseConfigRequest.md) |  |  [optional] |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**hmsOptions** | [**ConfigRequest**](ConfigRequest.md) |  |  [optional] |
|**huaweiConfig** | [**HuaweiConfigRequest**](HuaweiConfigRequest.md) |  |  [optional] |
|**imageModerationBlockLabels** | **List&lt;String&gt;** |  |  [optional] |
|**imageModerationEnabled** | **Boolean** |  |  [optional] |
|**imageModerationLabels** | **List&lt;String&gt;** |  |  [optional] |
|**imageUploadConfig** | [**FileUploadConfigRequest**](FileUploadConfigRequest.md) |  |  [optional] |
|**migratePermissionsToV2** | **Boolean** |  |  [optional] |
|**multiTenantEnabled** | **Boolean** |  |  [optional] |
|**permissionVersion** | [**PermissionVersionEnum**](#PermissionVersionEnum) |  |  [optional] |
|**pushConfig** | [**PushConfigRequest**](PushConfigRequest.md) |  |  [optional] |
|**remindersInterval** | **Integer** |  |  [optional] |
|**revokeTokensIssuedBefore** | **OffsetDateTime** |  |  [optional] |
|**sqsKey** | **String** |  |  [optional] |
|**sqsSecret** | **String** |  |  [optional] |
|**sqsUrl** | **String** |  |  [optional] |
|**userSearchDisallowedRoles** | **List&lt;String&gt;** |  |  [optional] |
|**videoProvider** | [**VideoProviderEnum**](#VideoProviderEnum) |  |  [optional] |
|**webhookEvents** | **List&lt;String&gt;** |  |  [optional] |
|**webhookUrl** | **String** |  |  [optional] |
|**xiaomiConfig** | [**XiaomiConfigRequest**](XiaomiConfigRequest.md) |  |  [optional] |



## Enum: EnforceUniqueUsernamesEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;false&quot; |
| APP | &quot;app&quot; |
| TEAM | &quot;team&quot; |



## Enum: PermissionVersionEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |
| V2 | &quot;v2&quot; |



## Enum: VideoProviderEnum

| Name | Value |
|---- | -----|
| AGORA | &quot;agora&quot; |
| HMS | &quot;hms&quot; |



