

# ForumPostSearchResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authors** | [**List&lt;UserGeneralUser&gt;**](UserGeneralUser.md) |  |  [optional] |
|**availablePages** | **Integer** |  |  [optional] |
|**groups** | [**List&lt;GroupsV2GroupResponse&gt;**](GroupsV2GroupResponse.md) |  |  [optional] |
|**hasMore** | **Boolean** |  |  [optional] |
|**polls** | [**List&lt;ForumPollResponse&gt;**](ForumPollResponse.md) |  |  [optional] |
|**query** | [**QueriesPagedQuery**](QueriesPagedQuery.md) |  |  [optional] |
|**recruitmentDetails** | [**List&lt;ForumForumRecruitmentDetail&gt;**](ForumForumRecruitmentDetail.md) |  |  [optional] |
|**relatedPosts** | [**List&lt;ForumPostResponse&gt;**](ForumPostResponse.md) |  |  [optional] |
|**replacementContinuationToken** | **String** |  |  [optional] |
|**results** | [**List&lt;ForumPostResponse&gt;**](ForumPostResponse.md) |  |  [optional] |
|**searchedTags** | [**List&lt;TagsModelsContractsTagResponse&gt;**](TagsModelsContractsTagResponse.md) |  |  [optional] |
|**totalResults** | **Integer** |  |  [optional] |
|**useTotalResults** | **Boolean** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. |  [optional] |



