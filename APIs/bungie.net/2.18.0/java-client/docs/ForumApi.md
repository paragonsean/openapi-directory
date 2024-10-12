# ForumApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forumGetCoreTopicsPaged**](ForumApi.md#forumGetCoreTopicsPaged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ |  |
| [**forumGetForumTagSuggestions**](ForumApi.md#forumGetForumTagSuggestions) | **GET** /Forum/GetForumTagSuggestions/ |  |
| [**forumGetPoll**](ForumApi.md#forumGetPoll) | **GET** /Forum/Poll/{topicId}/ |  |
| [**forumGetPostAndParent**](ForumApi.md#forumGetPostAndParent) | **GET** /Forum/GetPostAndParent/{childPostId}/ |  |
| [**forumGetPostAndParentAwaitingApproval**](ForumApi.md#forumGetPostAndParentAwaitingApproval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ |  |
| [**forumGetPostsThreadedPaged**](ForumApi.md#forumGetPostsThreadedPaged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ |  |
| [**forumGetPostsThreadedPagedFromChild**](ForumApi.md#forumGetPostsThreadedPagedFromChild) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ |  |
| [**forumGetRecruitmentThreadSummaries**](ForumApi.md#forumGetRecruitmentThreadSummaries) | **POST** /Forum/Recruit/Summaries/ |  |
| [**forumGetTopicForContent**](ForumApi.md#forumGetTopicForContent) | **GET** /Forum/GetTopicForContent/{contentId}/ |  |
| [**forumGetTopicsPaged**](ForumApi.md#forumGetTopicsPaged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ |  |


<a id="forumGetCoreTopicsPaged"></a>
# **forumGetCoreTopicsPaged**
> CommunityContentGetCommunityContent200Response forumGetCoreTopicsPaged(categoryFilter, page, quickDate, sort, locales)



Gets a listing of all topics marked as part of the core group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Integer categoryFilter = 56; // Integer | The category filter.
    Integer page = 56; // Integer | Zero base page
    Integer quickDate = 56; // Integer | The date filter.
    Integer sort = 56; // Integer | The sort mode.
    String locales = "locales_example"; // String | Comma seperated list of locales posts must match to return in the result list. Default 'en'
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetCoreTopicsPaged(categoryFilter, page, quickDate, sort, locales);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetCoreTopicsPaged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **categoryFilter** | **Integer**| The category filter. | |
| **page** | **Integer**| Zero base page | |
| **quickDate** | **Integer**| The date filter. | |
| **sort** | **Integer**| The sort mode. | |
| **locales** | **String**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetForumTagSuggestions"></a>
# **forumGetForumTagSuggestions**
> ForumGetForumTagSuggestions200Response forumGetForumTagSuggestions(partialtag)



Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    String partialtag = "partialtag_example"; // String | The partial tag input to generate suggestions from.
    try {
      ForumGetForumTagSuggestions200Response result = apiInstance.forumGetForumTagSuggestions(partialtag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetForumTagSuggestions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **partialtag** | **String**| The partial tag input to generate suggestions from. | [optional] |

### Return type

[**ForumGetForumTagSuggestions200Response**](ForumGetForumTagSuggestions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetPoll"></a>
# **forumGetPoll**
> CommunityContentGetCommunityContent200Response forumGetPoll(topicId)



Gets the specified forum poll.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Long topicId = 56L; // Long | The post id of the topic that has the poll.
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetPoll(topicId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetPoll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **topicId** | **Long**| The post id of the topic that has the poll. | |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetPostAndParent"></a>
# **forumGetPostAndParent**
> CommunityContentGetCommunityContent200Response forumGetPostAndParent(childPostId, showbanned)



Returns the post specified and its immediate parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Long childPostId = 56L; // Long | 
    String showbanned = "showbanned_example"; // String | If this value is not null or empty, banned posts are requested to be returned
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetPostAndParent(childPostId, showbanned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetPostAndParent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **childPostId** | **Long**|  | |
| **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetPostAndParentAwaitingApproval"></a>
# **forumGetPostAndParentAwaitingApproval**
> CommunityContentGetCommunityContent200Response forumGetPostAndParentAwaitingApproval(childPostId, showbanned)



Returns the post specified and its immediate parent of posts that are awaiting approval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Long childPostId = 56L; // Long | 
    String showbanned = "showbanned_example"; // String | If this value is not null or empty, banned posts are requested to be returned
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetPostAndParentAwaitingApproval(childPostId, showbanned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetPostAndParentAwaitingApproval");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **childPostId** | **Long**|  | |
| **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetPostsThreadedPaged"></a>
# **forumGetPostsThreadedPaged**
> CommunityContentGetCommunityContent200Response forumGetPostsThreadedPaged(getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, sortMode, showbanned)



Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Boolean getParentPost = true; // Boolean | 
    Integer page = 56; // Integer | 
    Integer pageSize = 56; // Integer | 
    Long parentPostId = 56L; // Long | 
    Integer replySize = 56; // Integer | 
    Boolean rootThreadMode = true; // Boolean | 
    Integer sortMode = 56; // Integer | 
    String showbanned = "showbanned_example"; // String | If this value is not null or empty, banned posts are requested to be returned
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetPostsThreadedPaged(getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, sortMode, showbanned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetPostsThreadedPaged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getParentPost** | **Boolean**|  | |
| **page** | **Integer**|  | |
| **pageSize** | **Integer**|  | |
| **parentPostId** | **Long**|  | |
| **replySize** | **Integer**|  | |
| **rootThreadMode** | **Boolean**|  | |
| **sortMode** | **Integer**|  | |
| **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetPostsThreadedPagedFromChild"></a>
# **forumGetPostsThreadedPagedFromChild**
> CommunityContentGetCommunityContent200Response forumGetPostsThreadedPagedFromChild(childPostId, page, pageSize, replySize, rootThreadMode, sortMode, showbanned)



Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Long childPostId = 56L; // Long | 
    Integer page = 56; // Integer | 
    Integer pageSize = 56; // Integer | 
    Integer replySize = 56; // Integer | 
    Boolean rootThreadMode = true; // Boolean | 
    Integer sortMode = 56; // Integer | 
    String showbanned = "showbanned_example"; // String | If this value is not null or empty, banned posts are requested to be returned
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetPostsThreadedPagedFromChild(childPostId, page, pageSize, replySize, rootThreadMode, sortMode, showbanned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetPostsThreadedPagedFromChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **childPostId** | **Long**|  | |
| **page** | **Integer**|  | |
| **pageSize** | **Integer**|  | |
| **replySize** | **Integer**|  | |
| **rootThreadMode** | **Boolean**|  | |
| **sortMode** | **Integer**|  | |
| **showbanned** | **String**| If this value is not null or empty, banned posts are requested to be returned | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetRecruitmentThreadSummaries"></a>
# **forumGetRecruitmentThreadSummaries**
> ForumGetRecruitmentThreadSummaries200Response forumGetRecruitmentThreadSummaries()



Allows the caller to get a list of to 25 recruitment thread summary information objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    try {
      ForumGetRecruitmentThreadSummaries200Response result = apiInstance.forumGetRecruitmentThreadSummaries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetRecruitmentThreadSummaries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetTopicForContent"></a>
# **forumGetTopicForContent**
> ForumGetTopicForContent200Response forumGetTopicForContent(contentId)



Gets the post Id for the given content item&#39;s comments, if it exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Long contentId = 56L; // Long | 
    try {
      ForumGetTopicForContent200Response result = apiInstance.forumGetTopicForContent(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetTopicForContent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentId** | **Long**|  | |

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="forumGetTopicsPaged"></a>
# **forumGetTopicsPaged**
> CommunityContentGetCommunityContent200Response forumGetTopicsPaged(categoryFilter, group, page, pageSize, quickDate, sort, locales, tagstring)



Get topics from any forum.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ForumApi apiInstance = new ForumApi(defaultClient);
    Integer categoryFilter = 56; // Integer | A category filter
    Long group = 56L; // Long | The group, if any.
    Integer page = 56; // Integer | Zero paged page number
    Integer pageSize = 56; // Integer | Unused
    Integer quickDate = 56; // Integer | A date filter.
    Integer sort = 56; // Integer | The sort mode.
    String locales = "locales_example"; // String | Comma seperated list of locales posts must match to return in the result list. Default 'en'
    String tagstring = "tagstring_example"; // String | The tags to search, if any.
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.forumGetTopicsPaged(categoryFilter, group, page, pageSize, quickDate, sort, locales, tagstring);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForumApi#forumGetTopicsPaged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **categoryFilter** | **Integer**| A category filter | |
| **group** | **Long**| The group, if any. | |
| **page** | **Integer**| Zero paged page number | |
| **pageSize** | **Integer**| Unused | |
| **quickDate** | **Integer**| A date filter. | |
| **sort** | **Integer**| The sort mode. | |
| **locales** | **String**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] |
| **tagstring** | **String**| The tags to search, if any. | [optional] |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

