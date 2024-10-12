

# DeleteUsersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversations** | [**ConversationsEnum**](#ConversationsEnum) | Conversation channels delete mode. Conversation channel is any channel which only has two members one of which is the user being deleted.  * null or empty string - doesn&#39;t delete any conversation channels * soft - marks all conversation channels as deleted (same effect as Delete Channels with &#39;hard&#39; option disabled) * hard - deletes channel and all its data completely including messages (same effect as Delete Channels with &#39;hard&#39; option enabled)  |  [optional] |
|**messages** | [**MessagesEnum**](#MessagesEnum) | Message delete mode.  * null or empty string - doesn&#39;t delete user messages * soft - marks all user messages as deleted without removing any related message data * pruning - marks all user messages as deleted, nullifies message information and removes some message data such as reactions and flags * hard - deletes messages completely with all related information  |  [optional] |
|**newChannelOwnerId** | **String** |  |  [optional] |
|**user** | [**UserEnum**](#UserEnum) | User delete mode.  * soft - marks user as deleted and retains all user data * pruning - marks user as deleted and nullifies user information * hard - deletes user completely. Requires &#39;hard&#39; option for messages and conversations as well  |  [optional] |
|**userIds** | **List&lt;String&gt;** | IDs of users to delete |  |



## Enum: ConversationsEnum

| Name | Value |
|---- | -----|
| SOFT | &quot;soft&quot; |
| HARD | &quot;hard&quot; |



## Enum: MessagesEnum

| Name | Value |
|---- | -----|
| SOFT | &quot;soft&quot; |
| PRUNING | &quot;pruning&quot; |
| HARD | &quot;hard&quot; |



## Enum: UserEnum

| Name | Value |
|---- | -----|
| SOFT | &quot;soft&quot; |
| PRUNING | &quot;pruning&quot; |
| HARD | &quot;hard&quot; |



