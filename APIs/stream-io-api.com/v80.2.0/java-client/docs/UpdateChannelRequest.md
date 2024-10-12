

# UpdateChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptInvite** | **Boolean** | Set to &#x60;true&#x60; to accept the invite |  [optional] |
|**addMembers** | [**List&lt;ChannelMemberRequest&gt;**](ChannelMemberRequest.md) | List of user IDs to add to the channel |  [optional] |
|**addModerators** | **List&lt;String&gt;** | List of user IDs to make channel moderators |  |
|**assignRoles** | [**List&lt;ChannelMemberRequest&gt;**](ChannelMemberRequest.md) | List of channel member role assignments. If any specified user is not part of the channel, the request will fail |  [optional] |
|**cooldown** | **Integer** | Sets cool down period for the channel in seconds |  [optional] |
|**data** | **ChannelRequest** |  |  [optional] |
|**demoteModerators** | **List&lt;String&gt;** | List of user IDs to take away moderators status from |  |
|**hideHistory** | **Boolean** | Set to &#x60;true&#x60; to hide channel&#39;s history when adding new members |  [optional] |
|**invites** | [**List&lt;ChannelMemberRequest&gt;**](ChannelMemberRequest.md) | List of user IDs to invite to the channel |  [optional] |
|**message** | **MessageRequest** |  |  [optional] |
|**rejectInvite** | **Boolean** | Set to &#x60;true&#x60; to reject the invite |  [optional] |
|**removeMembers** | **List&lt;String&gt;** | List of user IDs to remove from the channel |  |
|**skipPush** | **Boolean** | When &#x60;message&#x60; is set disables all push notifications for it |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



