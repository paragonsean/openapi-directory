# BungieNetApi.ForumApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forumGetCoreTopicsPaged**](ForumApi.md#forumGetCoreTopicsPaged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ | 
[**forumGetForumTagSuggestions**](ForumApi.md#forumGetForumTagSuggestions) | **GET** /Forum/GetForumTagSuggestions/ | 
[**forumGetPoll**](ForumApi.md#forumGetPoll) | **GET** /Forum/Poll/{topicId}/ | 
[**forumGetPostAndParent**](ForumApi.md#forumGetPostAndParent) | **GET** /Forum/GetPostAndParent/{childPostId}/ | 
[**forumGetPostAndParentAwaitingApproval**](ForumApi.md#forumGetPostAndParentAwaitingApproval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ | 
[**forumGetPostsThreadedPaged**](ForumApi.md#forumGetPostsThreadedPaged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ | 
[**forumGetPostsThreadedPagedFromChild**](ForumApi.md#forumGetPostsThreadedPagedFromChild) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ | 
[**forumGetRecruitmentThreadSummaries**](ForumApi.md#forumGetRecruitmentThreadSummaries) | **POST** /Forum/Recruit/Summaries/ | 
[**forumGetTopicForContent**](ForumApi.md#forumGetTopicForContent) | **GET** /Forum/GetTopicForContent/{contentId}/ | 
[**forumGetTopicsPaged**](ForumApi.md#forumGetTopicsPaged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ | 



## forumGetCoreTopicsPaged

> CommunityContentGetCommunityContent200Response forumGetCoreTopicsPaged(categoryFilter, page, quickDate, sort, opts)



Gets a listing of all topics marked as part of the core group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let categoryFilter = 56; // Number | The category filter.
let page = 56; // Number | Zero base page
let quickDate = 56; // Number | The date filter.
let sort = 56; // Number | The sort mode.
let opts = {
  'locales': "locales_example" // String | Comma seperated list of locales posts must match to return in the result list. Default 'en'
};
apiInstance.forumGetCoreTopicsPaged(categoryFilter, page, quickDate, sort, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryFilter** | **Number**| The category filter. | 
 **page** | **Number**| Zero base page | 
 **quickDate** | **Number**| The date filter. | 
 **sort** | **Number**| The sort mode. | 
 **locales** | **String**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetForumTagSuggestions

> ForumGetForumTagSuggestions200Response forumGetForumTagSuggestions(opts)



Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let opts = {
  'partialtag': "partialtag_example" // String | The partial tag input to generate suggestions from.
};
apiInstance.forumGetForumTagSuggestions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partialtag** | **String**| The partial tag input to generate suggestions from. | [optional] 

### Return type

[**ForumGetForumTagSuggestions200Response**](ForumGetForumTagSuggestions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetPoll

> CommunityContentGetCommunityContent200Response forumGetPoll(topicId)



Gets the specified forum poll.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let topicId = 789; // Number | The post id of the topic that has the poll.
apiInstance.forumGetPoll(topicId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topicId** | **Number**| The post id of the topic that has the poll. | 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetPostAndParent

> CommunityContentGetCommunityContent200Response forumGetPostAndParent(childPostId, opts)



Returns the post specified and its immediate parent.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let childPostId = 789; // Number | 
let opts = {
  'showbanned': "showbanned_example" // String | If this value is not null or empty, banned posts are requested to be returned
};
apiInstance.forumGetPostAndParent(childPostId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **childPostId** | **Number**|  | 
 **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetPostAndParentAwaitingApproval

> CommunityContentGetCommunityContent200Response forumGetPostAndParentAwaitingApproval(childPostId, opts)



Returns the post specified and its immediate parent of posts that are awaiting approval.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let childPostId = 789; // Number | 
let opts = {
  'showbanned': "showbanned_example" // String | If this value is not null or empty, banned posts are requested to be returned
};
apiInstance.forumGetPostAndParentAwaitingApproval(childPostId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **childPostId** | **Number**|  | 
 **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetPostsThreadedPaged

> CommunityContentGetCommunityContent200Response forumGetPostsThreadedPaged(getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, sortMode, opts)



Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let getParentPost = true; // Boolean | 
let page = 56; // Number | 
let pageSize = 56; // Number | 
let parentPostId = 789; // Number | 
let replySize = 56; // Number | 
let rootThreadMode = true; // Boolean | 
let sortMode = 56; // Number | 
let opts = {
  'showbanned': "showbanned_example" // String | If this value is not null or empty, banned posts are requested to be returned
};
apiInstance.forumGetPostsThreadedPaged(getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, sortMode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getParentPost** | **Boolean**|  | 
 **page** | **Number**|  | 
 **pageSize** | **Number**|  | 
 **parentPostId** | **Number**|  | 
 **replySize** | **Number**|  | 
 **rootThreadMode** | **Boolean**|  | 
 **sortMode** | **Number**|  | 
 **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetPostsThreadedPagedFromChild

> CommunityContentGetCommunityContent200Response forumGetPostsThreadedPagedFromChild(childPostId, page, pageSize, replySize, rootThreadMode, sortMode, opts)



Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let childPostId = 789; // Number | 
let page = 56; // Number | 
let pageSize = 56; // Number | 
let replySize = 56; // Number | 
let rootThreadMode = true; // Boolean | 
let sortMode = 56; // Number | 
let opts = {
  'showbanned': "showbanned_example" // String | If this value is not null or empty, banned posts are requested to be returned
};
apiInstance.forumGetPostsThreadedPagedFromChild(childPostId, page, pageSize, replySize, rootThreadMode, sortMode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **childPostId** | **Number**|  | 
 **page** | **Number**|  | 
 **pageSize** | **Number**|  | 
 **replySize** | **Number**|  | 
 **rootThreadMode** | **Boolean**|  | 
 **sortMode** | **Number**|  | 
 **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetRecruitmentThreadSummaries

> ForumGetRecruitmentThreadSummaries200Response forumGetRecruitmentThreadSummaries()



Allows the caller to get a list of to 25 recruitment thread summary information objects.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
apiInstance.forumGetRecruitmentThreadSummaries((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ForumGetRecruitmentThreadSummaries200Response**](ForumGetRecruitmentThreadSummaries200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetTopicForContent

> ForumGetTopicForContent200Response forumGetTopicForContent(contentId)



Gets the post Id for the given content item&#39;s comments, if it exists.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let contentId = 789; // Number | 
apiInstance.forumGetTopicForContent(contentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentId** | **Number**|  | 

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## forumGetTopicsPaged

> CommunityContentGetCommunityContent200Response forumGetTopicsPaged(categoryFilter, group, page, pageSize, quickDate, sort, opts)



Get topics from any forum.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ForumApi();
let categoryFilter = 56; // Number | A category filter
let group = 789; // Number | The group, if any.
let page = 56; // Number | Zero paged page number
let pageSize = 56; // Number | Unused
let quickDate = 56; // Number | A date filter.
let sort = 56; // Number | The sort mode.
let opts = {
  'locales': "locales_example", // String | Comma seperated list of locales posts must match to return in the result list. Default 'en'
  'tagstring': "tagstring_example" // String | The tags to search, if any.
};
apiInstance.forumGetTopicsPaged(categoryFilter, group, page, pageSize, quickDate, sort, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryFilter** | **Number**| A category filter | 
 **group** | **Number**| The group, if any. | 
 **page** | **Number**| Zero paged page number | 
 **pageSize** | **Number**| Unused | 
 **quickDate** | **Number**| A date filter. | 
 **sort** | **Number**| The sort mode. | 
 **locales** | **String**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 
 **tagstring** | **String**| The tags to search, if any. | [optional] 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

