# StreamChatApi.App

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agoraOptions** | [**Config**](Config.md) |  | [optional] 
**asyncUrlEnrichEnabled** | **Boolean** |  | 
**autoTranslationEnabled** | **Boolean** |  | [optional] 
**beforeMessageSendHookUrl** | **String** |  | [optional] 
**callTypes** | [**{String: CallType}**](CallType.md) |  | 
**campaignEnabled** | **Boolean** |  | 
**cdnExpirationSeconds** | **Number** |  | 
**channelConfigs** | [**{String: ChannelConfig}**](ChannelConfig.md) | Object with channel configs | 
**customActionHandlerUrl** | **String** |  | 
**disableAuthChecks** | **Boolean** |  | 
**disablePermissionsChecks** | **Boolean** |  | 
**enforceUniqueUsernames** | **String** |  | 
**fileUploadConfig** | [**FileUploadConfig**](FileUploadConfig.md) |  | 
**grants** | **{String: [String]}** |  | 
**hmsOptions** | [**Config**](Config.md) |  | [optional] 
**imageModerationEnabled** | **Boolean** |  | 
**imageModerationLabels** | **[String]** |  | [optional] 
**imageUploadConfig** | [**FileUploadConfig**](FileUploadConfig.md) |  | 
**multiTenantEnabled** | **Boolean** |  | 
**name** | **String** |  | 
**organization** | **String** |  | 
**permissionVersion** | **String** |  | 
**policies** | **{String: [Policy]}** |  | 
**pushNotifications** | [**PushNotificationFields**](PushNotificationFields.md) |  | 
**remindersInterval** | **Number** |  | 
**revokeTokensIssuedBefore** | **Date** |  | [optional] 
**searchBackend** | **String** | Backend implementation used for search | 
**sqsKey** | **String** |  | 
**sqsSecret** | **String** |  | 
**sqsUrl** | **String** |  | 
**suspended** | **Boolean** |  | 
**suspendedExplanation** | **String** |  | 
**userSearchDisallowedRoles** | **[String]** |  | 
**videoProvider** | **String** |  | 
**webhookEvents** | **[String]** |  | 
**webhookUrl** | **String** |  | 



## Enum: SearchBackendEnum


* `elasticsearch` (value: `"elasticsearch"`)

* `postgres` (value: `"postgres"`)

* `disabled` (value: `"disabled"`)




