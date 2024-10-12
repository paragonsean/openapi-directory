# StreamChatApi.UpdateAppRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agoraOptions** | [**ConfigRequest**](ConfigRequest.md) |  | [optional] 
**apnConfig** | [**APNConfigRequest**](APNConfigRequest.md) |  | [optional] 
**asyncModerationConfig** | [**AsyncModerationConfigurationRequest**](AsyncModerationConfigurationRequest.md) |  | [optional] 
**asyncUrlEnrichEnabled** | **Boolean** |  | [optional] 
**autoTranslationEnabled** | **Boolean** |  | [optional] 
**beforeMessageSendHookUrl** | **String** |  | [optional] 
**cdnExpirationSeconds** | **Number** |  | [optional] 
**channelHideMembersOnly** | **Boolean** |  | [optional] 
**customActionHandlerUrl** | **String** |  | [optional] 
**disableAuthChecks** | **Boolean** |  | [optional] 
**disablePermissionsChecks** | **Boolean** |  | [optional] 
**enforceUniqueUsernames** | **String** |  | [optional] 
**fileUploadConfig** | [**FileUploadConfigRequest**](FileUploadConfigRequest.md) |  | [optional] 
**firebaseConfig** | [**FirebaseConfigRequest**](FirebaseConfigRequest.md) |  | [optional] 
**grants** | **{String: [String]}** |  | [optional] 
**hmsOptions** | [**ConfigRequest**](ConfigRequest.md) |  | [optional] 
**huaweiConfig** | [**HuaweiConfigRequest**](HuaweiConfigRequest.md) |  | [optional] 
**imageModerationBlockLabels** | **[String]** |  | [optional] 
**imageModerationEnabled** | **Boolean** |  | [optional] 
**imageModerationLabels** | **[String]** |  | [optional] 
**imageUploadConfig** | [**FileUploadConfigRequest**](FileUploadConfigRequest.md) |  | [optional] 
**migratePermissionsToV2** | **Boolean** |  | [optional] 
**multiTenantEnabled** | **Boolean** |  | [optional] 
**permissionVersion** | **String** |  | [optional] 
**pushConfig** | [**PushConfigRequest**](PushConfigRequest.md) |  | [optional] 
**remindersInterval** | **Number** |  | [optional] 
**revokeTokensIssuedBefore** | **Date** |  | [optional] 
**sqsKey** | **String** |  | [optional] 
**sqsSecret** | **String** |  | [optional] 
**sqsUrl** | **String** |  | [optional] 
**userSearchDisallowedRoles** | **[String]** |  | [optional] 
**videoProvider** | **String** |  | [optional] 
**webhookEvents** | **[String]** |  | [optional] 
**webhookUrl** | **String** |  | [optional] 
**xiaomiConfig** | [**XiaomiConfigRequest**](XiaomiConfigRequest.md) |  | [optional] 



## Enum: EnforceUniqueUsernamesEnum


* `false` (value: `"false"`)

* `app` (value: `"app"`)

* `team` (value: `"team"`)





## Enum: PermissionVersionEnum


* `v1` (value: `"v1"`)

* `v2` (value: `"v2"`)





## Enum: VideoProviderEnum


* `agora` (value: `"agora"`)

* `hms` (value: `"hms"`)




