

# SearchPosts200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endIndex** | **Integer** | The index of the last post being returned (an integer between start_index and num_posts). |  [optional] |
|**groupIds** | **List&lt;String&gt;** | The IDs of the groups that the posts were retrieved from (will be null when no group IDs were used). These IDs may be a subset of the requested group IDs when a request includes group IDs for groups that are not open archives and that the current user is not a member of.  If the open_archive_groups source is used, these IDs may include the IDs of open archive groups that weren&#39;t present in the group_ids parameter of the request.  |  [optional] |
|**numPages** | **Integer** | The total number of pages available. |  [optional] |
|**numPosts** | **Integer** | The total number of posts available. |  [optional] |
|**page** | **Integer** | The page number of the posts being returned. |  [optional] |
|**perPage** | **Integer** | The number of posts being returned per page. |  [optional] |
|**posts** | [**List&lt;PostSearchResult&gt;**](PostSearchResult.md) |  |  [optional] |
|**startIndex** | **Integer** | The index of the first post being returned (an integer between 1 and num_posts). |  [optional] |



