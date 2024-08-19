# GitHubV3RestApi.TeamDiscussionComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **String** | The main text of the comment. | 
**bodyHtml** | **String** |  | 
**bodyVersion** | **String** | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. | 
**createdAt** | **Date** |  | 
**discussionUrl** | **String** |  | 
**htmlUrl** | **String** |  | 
**lastEditedAt** | **Date** |  | 
**nodeId** | **String** |  | 
**number** | **Number** | The unique sequence number of a team discussion comment. | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**updatedAt** | **Date** |  | 
**url** | **String** |  | 


