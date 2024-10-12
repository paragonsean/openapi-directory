# BungieNetApi.ForumPostSearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | [**[UserGeneralUser]**](UserGeneralUser.md) |  | [optional] 
**availablePages** | **Number** |  | [optional] 
**groups** | [**[GroupsV2GroupResponse]**](GroupsV2GroupResponse.md) |  | [optional] 
**hasMore** | **Boolean** |  | [optional] 
**polls** | [**[ForumPollResponse]**](ForumPollResponse.md) |  | [optional] 
**query** | [**QueriesPagedQuery**](QueriesPagedQuery.md) |  | [optional] 
**recruitmentDetails** | [**[ForumForumRecruitmentDetail]**](ForumForumRecruitmentDetail.md) |  | [optional] 
**relatedPosts** | [**[ForumPostResponse]**](ForumPostResponse.md) |  | [optional] 
**replacementContinuationToken** | **String** |  | [optional] 
**results** | [**[ForumPostResponse]**](ForumPostResponse.md) |  | [optional] 
**searchedTags** | [**[TagsModelsContractsTagResponse]**](TagsModelsContractsTagResponse.md) |  | [optional] 
**totalResults** | **Number** |  | [optional] 
**useTotalResults** | **Boolean** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. | [optional] 


