

# App


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agoraOptions** | [**Config**](Config.md) |  |  [optional] |
|**asyncUrlEnrichEnabled** | **Boolean** |  |  |
|**autoTranslationEnabled** | **Boolean** |  |  [optional] |
|**beforeMessageSendHookUrl** | **String** |  |  [optional] |
|**callTypes** | [**Map&lt;String, CallType&gt;**](CallType.md) |  |  |
|**campaignEnabled** | **Boolean** |  |  |
|**cdnExpirationSeconds** | **Integer** |  |  |
|**channelConfigs** | [**Map&lt;String, ChannelConfig&gt;**](ChannelConfig.md) | Object with channel configs |  |
|**customActionHandlerUrl** | **String** |  |  |
|**disableAuthChecks** | **Boolean** |  |  |
|**disablePermissionsChecks** | **Boolean** |  |  |
|**enforceUniqueUsernames** | **String** |  |  |
|**fileUploadConfig** | [**FileUploadConfig**](FileUploadConfig.md) |  |  |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  |
|**hmsOptions** | [**Config**](Config.md) |  |  [optional] |
|**imageModerationEnabled** | **Boolean** |  |  |
|**imageModerationLabels** | **List&lt;String&gt;** |  |  [optional] |
|**imageUploadConfig** | [**FileUploadConfig**](FileUploadConfig.md) |  |  |
|**multiTenantEnabled** | **Boolean** |  |  |
|**name** | **String** |  |  |
|**organization** | **String** |  |  |
|**permissionVersion** | **String** |  |  |
|**policies** | **Map&lt;String, List&lt;Policy&gt;&gt;** |  |  |
|**pushNotifications** | [**PushNotificationFields**](PushNotificationFields.md) |  |  |
|**remindersInterval** | **Integer** |  |  |
|**revokeTokensIssuedBefore** | **OffsetDateTime** |  |  [optional] |
|**searchBackend** | [**SearchBackendEnum**](#SearchBackendEnum) | Backend implementation used for search |  |
|**sqsKey** | **String** |  |  |
|**sqsSecret** | **String** |  |  |
|**sqsUrl** | **String** |  |  |
|**suspended** | **Boolean** |  |  |
|**suspendedExplanation** | **String** |  |  |
|**userSearchDisallowedRoles** | **List&lt;String&gt;** |  |  |
|**videoProvider** | **String** |  |  |
|**webhookEvents** | **List&lt;String&gt;** |  |  |
|**webhookUrl** | **String** |  |  |



## Enum: SearchBackendEnum

| Name | Value |
|---- | -----|
| ELASTICSEARCH | &quot;elasticsearch&quot; |
| POSTGRES | &quot;postgres&quot; |
| DISABLED | &quot;disabled&quot; |



