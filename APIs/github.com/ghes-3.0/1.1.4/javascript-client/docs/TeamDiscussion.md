# GitHubV3RestApi.TeamDiscussion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **String** | The main text of the discussion. | 
**bodyHtml** | **String** |  | 
**bodyVersion** | **String** | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. | 
**commentsCount** | **Number** |  | 
**commentsUrl** | **String** |  | 
**createdAt** | **Date** |  | 
**htmlUrl** | **String** |  | 
**lastEditedAt** | **Date** |  | 
**nodeId** | **String** |  | 
**number** | **Number** | The unique sequence number of a team discussion. | 
**pinned** | **Boolean** | Whether or not this discussion should be pinned for easy retrieval. | 
**_private** | **Boolean** | Whether or not this discussion should be restricted to team members and organization administrators. | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**teamUrl** | **String** |  | 
**title** | **String** | The title of the discussion. | 
**updatedAt** | **Date** |  | 
**url** | **String** |  | 


