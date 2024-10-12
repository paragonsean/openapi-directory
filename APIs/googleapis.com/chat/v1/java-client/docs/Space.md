

# Space

A space in Google Chat. Spaces are conversations between two or more users or 1:1 messages between a user and a Chat app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminInstalled** | **Boolean** | Output only. Whether the Chat app was installed by a Google Workspace administrator. Administrators can install a Chat app for their domain, organizational unit, or a group of users. Administrators can only install Chat apps for direct messaging between users and the app. To support admin install, your app must feature direct messaging. |  [optional] [readonly] |
|**createTime** | **String** | Optional. Immutable. For spaces created in Chat, the time the space was created. This field is output only, except when used in import mode spaces. For import mode spaces, set this field to the historical timestamp at which the space was created in the source in order to preserve the original creation time. Only populated in the output when &#x60;spaceType&#x60; is &#x60;GROUP_CHAT&#x60; or &#x60;SPACE&#x60;. |  [optional] |
|**displayName** | **String** | The space&#39;s display name. Required when [creating a space](https://developers.google.com/chat/api/reference/rest/v1/spaces/create). If you receive the error message &#x60;ALREADY_EXISTS&#x60; when creating a space or updating the &#x60;displayName&#x60;, try a different &#x60;displayName&#x60;. An existing space within the Google Workspace organization might already use this display name. For direct messages, this field might be empty. Supports up to 128 characters. |  [optional] |
|**externalUserAllowed** | **Boolean** | Immutable. Whether this space permits any Google Chat user as a member. Input when creating a space in a Google Workspace organization. Omit this field when creating spaces in the following conditions: * The authenticated user uses a Google Account. By default, the space permits any Google Chat user. * The space is used to [import data to Google Chat] (https://developers.google.com/chat/api/guides/import-data-overview). Import mode spaces must only permit members from the same Google Workspace organization. For existing spaces, this field is output only. |  [optional] |
|**importMode** | **Boolean** | Optional. Whether this space is created in &#x60;Import Mode&#x60; as part of a data migration into Google Workspace. While spaces are being imported, they aren&#39;t visible to users until the import is complete. |  [optional] |
|**name** | **String** | Resource name of the space. Format: &#x60;spaces/{space}&#x60; |  [optional] |
|**singleUserBotDm** | **Boolean** | Optional. Whether the space is a DM between a Chat app and a single human. |  [optional] |
|**spaceDetails** | [**SpaceDetails**](SpaceDetails.md) |  |  [optional] |
|**spaceHistoryState** | [**SpaceHistoryStateEnum**](#SpaceHistoryStateEnum) | The message history state for messages and threads in this space. |  [optional] |
|**spaceThreadingState** | [**SpaceThreadingStateEnum**](#SpaceThreadingStateEnum) | Output only. The threading state in the Chat space. |  [optional] [readonly] |
|**spaceType** | [**SpaceTypeEnum**](#SpaceTypeEnum) | The type of space. Required when creating a space or updating the space type of a space. Output only for other usage. |  [optional] |
|**threaded** | **Boolean** | Output only. Deprecated: Use &#x60;spaceThreadingState&#x60; instead. Whether messages are threaded in this space. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Deprecated: Use &#x60;space_type&#x60; instead. The type of a space. |  [optional] [readonly] |



## Enum: SpaceHistoryStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;HISTORY_STATE_UNSPECIFIED&quot; |
| OFF | &quot;HISTORY_OFF&quot; |
| ON | &quot;HISTORY_ON&quot; |



## Enum: SpaceThreadingStateEnum

| Name | Value |
|---- | -----|
| SPACE_THREADING_STATE_UNSPECIFIED | &quot;SPACE_THREADING_STATE_UNSPECIFIED&quot; |
| THREADED_MESSAGES | &quot;THREADED_MESSAGES&quot; |
| GROUPED_MESSAGES | &quot;GROUPED_MESSAGES&quot; |
| UNTHREADED_MESSAGES | &quot;UNTHREADED_MESSAGES&quot; |



## Enum: SpaceTypeEnum

| Name | Value |
|---- | -----|
| SPACE_TYPE_UNSPECIFIED | &quot;SPACE_TYPE_UNSPECIFIED&quot; |
| SPACE | &quot;SPACE&quot; |
| GROUP_CHAT | &quot;GROUP_CHAT&quot; |
| DIRECT_MESSAGE | &quot;DIRECT_MESSAGE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ROOM | &quot;ROOM&quot; |
| DM | &quot;DM&quot; |



