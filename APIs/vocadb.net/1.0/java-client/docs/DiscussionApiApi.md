# DiscussionApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDiscussionsCommentsCommentIdDelete**](DiscussionApiApi.md#apiDiscussionsCommentsCommentIdDelete) | **DELETE** /api/discussions/comments/{commentId} |  |
| [**apiDiscussionsCommentsCommentIdPost**](DiscussionApiApi.md#apiDiscussionsCommentsCommentIdPost) | **POST** /api/discussions/comments/{commentId} |  |
| [**apiDiscussionsFoldersFolderIdTopicsGet**](DiscussionApiApi.md#apiDiscussionsFoldersFolderIdTopicsGet) | **GET** /api/discussions/folders/{folderId}/topics |  |
| [**apiDiscussionsFoldersFolderIdTopicsPost**](DiscussionApiApi.md#apiDiscussionsFoldersFolderIdTopicsPost) | **POST** /api/discussions/folders/{folderId}/topics |  |
| [**apiDiscussionsFoldersGet**](DiscussionApiApi.md#apiDiscussionsFoldersGet) | **GET** /api/discussions/folders |  |
| [**apiDiscussionsFoldersPost**](DiscussionApiApi.md#apiDiscussionsFoldersPost) | **POST** /api/discussions/folders |  |
| [**apiDiscussionsTopicsGet**](DiscussionApiApi.md#apiDiscussionsTopicsGet) | **GET** /api/discussions/topics |  |
| [**apiDiscussionsTopicsTopicIdCommentsPost**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdCommentsPost) | **POST** /api/discussions/topics/{topicId}/comments |  |
| [**apiDiscussionsTopicsTopicIdDelete**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdDelete) | **DELETE** /api/discussions/topics/{topicId} |  |
| [**apiDiscussionsTopicsTopicIdGet**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdGet) | **GET** /api/discussions/topics/{topicId} |  |
| [**apiDiscussionsTopicsTopicIdPost**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdPost) | **POST** /api/discussions/topics/{topicId} |  |


<a id="apiDiscussionsCommentsCommentIdDelete"></a>
# **apiDiscussionsCommentsCommentIdDelete**
> apiDiscussionsCommentsCommentIdDelete(commentId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer commentId = 56; // Integer | 
    try {
      apiInstance.apiDiscussionsCommentsCommentIdDelete(commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsCommentsCommentIdDelete");
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
| **commentId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsCommentsCommentIdPost"></a>
# **apiDiscussionsCommentsCommentIdPost**
> apiDiscussionsCommentsCommentIdPost(commentId, commentForApiContract)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer commentId = 56; // Integer | 
    CommentForApiContract commentForApiContract = new CommentForApiContract(); // CommentForApiContract | 
    try {
      apiInstance.apiDiscussionsCommentsCommentIdPost(commentId, commentForApiContract);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsCommentsCommentIdPost");
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
| **commentId** | **Integer**|  | |
| **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsFoldersFolderIdTopicsGet"></a>
# **apiDiscussionsFoldersFolderIdTopicsGet**
> List&lt;DiscussionTopicContract&gt; apiDiscussionsFoldersFolderIdTopicsGet(folderId, fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer folderId = 56; // Integer | 
    DiscussionTopicOptionalFields fields = DiscussionTopicOptionalFields.fromValue("None"); // DiscussionTopicOptionalFields | 
    try {
      List<DiscussionTopicContract> result = apiInstance.apiDiscussionsFoldersFolderIdTopicsGet(folderId, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsFoldersFolderIdTopicsGet");
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
| **folderId** | **Integer**|  | |
| **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] [enum: None, Comments, CommentCount, Content, LastComment, All] |

### Return type

[**List&lt;DiscussionTopicContract&gt;**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsFoldersFolderIdTopicsPost"></a>
# **apiDiscussionsFoldersFolderIdTopicsPost**
> DiscussionTopicContract apiDiscussionsFoldersFolderIdTopicsPost(folderId, discussionTopicContract)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer folderId = 56; // Integer | 
    DiscussionTopicContract discussionTopicContract = new DiscussionTopicContract(); // DiscussionTopicContract | 
    try {
      DiscussionTopicContract result = apiInstance.apiDiscussionsFoldersFolderIdTopicsPost(folderId, discussionTopicContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsFoldersFolderIdTopicsPost");
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
| **folderId** | **Integer**|  | |
| **discussionTopicContract** | [**DiscussionTopicContract**](DiscussionTopicContract.md)|  | [optional] |

### Return type

[**DiscussionTopicContract**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsFoldersGet"></a>
# **apiDiscussionsFoldersGet**
> List&lt;DiscussionFolderContract&gt; apiDiscussionsFoldersGet(fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    DiscussionFolderOptionalFields fields = DiscussionFolderOptionalFields.fromValue("None"); // DiscussionFolderOptionalFields | 
    try {
      List<DiscussionFolderContract> result = apiInstance.apiDiscussionsFoldersGet(fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsFoldersGet");
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
| **fields** | [**DiscussionFolderOptionalFields**](.md)|  | [optional] [enum: None, LastTopic, TopicCount] |

### Return type

[**List&lt;DiscussionFolderContract&gt;**](DiscussionFolderContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsFoldersPost"></a>
# **apiDiscussionsFoldersPost**
> DiscussionFolderContract apiDiscussionsFoldersPost(discussionFolderContract)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    DiscussionFolderContract discussionFolderContract = new DiscussionFolderContract(); // DiscussionFolderContract | 
    try {
      DiscussionFolderContract result = apiInstance.apiDiscussionsFoldersPost(discussionFolderContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsFoldersPost");
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
| **discussionFolderContract** | [**DiscussionFolderContract**](DiscussionFolderContract.md)|  | [optional] |

### Return type

[**DiscussionFolderContract**](DiscussionFolderContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsTopicsGet"></a>
# **apiDiscussionsTopicsGet**
> DiscussionTopicContractPartialFindResult apiDiscussionsTopicsGet(folderId, start, maxResults, getTotalCount, sort, fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer folderId = 56; // Integer | 
    Integer start = 0; // Integer | 
    Integer maxResults = 10; // Integer | 
    Boolean getTotalCount = false; // Boolean | 
    DiscussionTopicSortRule sort = DiscussionTopicSortRule.fromValue("None"); // DiscussionTopicSortRule | 
    DiscussionTopicOptionalFields fields = DiscussionTopicOptionalFields.fromValue("None"); // DiscussionTopicOptionalFields | 
    try {
      DiscussionTopicContractPartialFindResult result = apiInstance.apiDiscussionsTopicsGet(folderId, start, maxResults, getTotalCount, sort, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsTopicsGet");
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
| **folderId** | **Integer**|  | [optional] |
| **start** | **Integer**|  | [optional] [default to 0] |
| **maxResults** | **Integer**|  | [optional] [default to 10] |
| **getTotalCount** | **Boolean**|  | [optional] [default to false] |
| **sort** | [**DiscussionTopicSortRule**](.md)|  | [optional] [enum: None, Name, DateCreated, LastCommentDate] |
| **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] [enum: None, Comments, CommentCount, Content, LastComment, All] |

### Return type

[**DiscussionTopicContractPartialFindResult**](DiscussionTopicContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsTopicsTopicIdCommentsPost"></a>
# **apiDiscussionsTopicsTopicIdCommentsPost**
> CommentForApiContract apiDiscussionsTopicsTopicIdCommentsPost(topicId, commentForApiContract)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer topicId = 56; // Integer | 
    CommentForApiContract commentForApiContract = new CommentForApiContract(); // CommentForApiContract | 
    try {
      CommentForApiContract result = apiInstance.apiDiscussionsTopicsTopicIdCommentsPost(topicId, commentForApiContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsTopicsTopicIdCommentsPost");
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
| **topicId** | **Integer**|  | |
| **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] |

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsTopicsTopicIdDelete"></a>
# **apiDiscussionsTopicsTopicIdDelete**
> apiDiscussionsTopicsTopicIdDelete(topicId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer topicId = 56; // Integer | 
    try {
      apiInstance.apiDiscussionsTopicsTopicIdDelete(topicId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsTopicsTopicIdDelete");
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
| **topicId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsTopicsTopicIdGet"></a>
# **apiDiscussionsTopicsTopicIdGet**
> DiscussionTopicContract apiDiscussionsTopicsTopicIdGet(topicId, fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer topicId = 56; // Integer | 
    DiscussionTopicOptionalFields fields = DiscussionTopicOptionalFields.fromValue("None"); // DiscussionTopicOptionalFields | 
    try {
      DiscussionTopicContract result = apiInstance.apiDiscussionsTopicsTopicIdGet(topicId, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsTopicsTopicIdGet");
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
| **topicId** | **Integer**|  | |
| **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] [enum: None, Comments, CommentCount, Content, LastComment, All] |

### Return type

[**DiscussionTopicContract**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiDiscussionsTopicsTopicIdPost"></a>
# **apiDiscussionsTopicsTopicIdPost**
> apiDiscussionsTopicsTopicIdPost(topicId, discussionTopicContract)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscussionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DiscussionApiApi apiInstance = new DiscussionApiApi(defaultClient);
    Integer topicId = 56; // Integer | 
    DiscussionTopicContract discussionTopicContract = new DiscussionTopicContract(); // DiscussionTopicContract | 
    try {
      apiInstance.apiDiscussionsTopicsTopicIdPost(topicId, discussionTopicContract);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscussionApiApi#apiDiscussionsTopicsTopicIdPost");
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
| **topicId** | **Integer**|  | |
| **discussionTopicContract** | [**DiscussionTopicContract**](DiscussionTopicContract.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

