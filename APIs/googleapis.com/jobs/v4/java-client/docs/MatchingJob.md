

# MatchingJob

Job entry with metadata inside SearchJobsResponse.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commuteInfo** | [**CommuteInfo**](CommuteInfo.md) |  |  [optional] |
|**job** | [**Job**](Job.md) |  |  [optional] |
|**jobSummary** | **String** | A summary of the job with core information that&#39;s displayed on the search results listing page. |  [optional] |
|**jobTitleSnippet** | **String** | Contains snippets of text from the Job.title field most closely matching a search query&#39;s keywords, if available. The matching query keywords are enclosed in HTML bold tags. |  [optional] |
|**searchTextSnippet** | **String** | Contains snippets of text from the Job.description and similar fields that most closely match a search query&#39;s keywords, if available. All HTML tags in the original fields are stripped when returned in this field, and matching query keywords are enclosed in HTML bold tags. |  [optional] |



