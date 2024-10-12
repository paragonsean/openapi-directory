

# TeamDiscussion

A team discussion is a persistent record of a free-form conversation within a team.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**body** | **String** | The main text of the discussion. |  |
|**bodyHtml** | **String** |  |  |
|**bodyVersion** | **String** | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |  |
|**commentsCount** | **Integer** |  |  |
|**commentsUrl** | **URI** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**htmlUrl** | **URI** |  |  |
|**lastEditedAt** | **OffsetDateTime** |  |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** | The unique sequence number of a team discussion. |  |
|**pinned** | **Boolean** | Whether or not this discussion should be pinned for easy retrieval. |  |
|**_private** | **Boolean** | Whether or not this discussion should be restricted to team members and organization administrators. |  |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**teamUrl** | **URI** |  |  |
|**title** | **String** | The title of the discussion. |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



