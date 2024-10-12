# TrashNothing.SearchPosts200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endIndex** | **Number** | The index of the last post being returned (an integer between start_index and num_posts). | [optional] 
**groupIds** | **[String]** | The IDs of the groups that the posts were retrieved from (will be null when no group IDs were used). These IDs may be a subset of the requested group IDs when a request includes group IDs for groups that are not open archives and that the current user is not a member of.  If the open_archive_groups source is used, these IDs may include the IDs of open archive groups that weren&#39;t present in the group_ids parameter of the request.  | [optional] 
**numPages** | **Number** | The total number of pages available. | [optional] 
**numPosts** | **Number** | The total number of posts available. | [optional] 
**page** | **Number** | The page number of the posts being returned. | [optional] 
**perPage** | **Number** | The number of posts being returned per page. | [optional] 
**posts** | [**[PostSearchResult]**](PostSearchResult.md) |  | [optional] 
**startIndex** | **Number** | The index of the first post being returned (an integer between 1 and num_posts). | [optional] 


