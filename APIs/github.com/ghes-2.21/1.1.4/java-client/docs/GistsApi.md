# GistsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gistsCheckIsStarred**](GistsApi.md#gistsCheckIsStarred) | **GET** /gists/{gist_id}/star | Check if a gist is starred |
| [**gistsCreate**](GistsApi.md#gistsCreate) | **POST** /gists | Create a gist |
| [**gistsCreateComment**](GistsApi.md#gistsCreateComment) | **POST** /gists/{gist_id}/comments | Create a gist comment |
| [**gistsDelete**](GistsApi.md#gistsDelete) | **DELETE** /gists/{gist_id} | Delete a gist |
| [**gistsDeleteComment**](GistsApi.md#gistsDeleteComment) | **DELETE** /gists/{gist_id}/comments/{comment_id} | Delete a gist comment |
| [**gistsFork**](GistsApi.md#gistsFork) | **POST** /gists/{gist_id}/forks | Fork a gist |
| [**gistsGet**](GistsApi.md#gistsGet) | **GET** /gists/{gist_id} | Get a gist |
| [**gistsGetComment**](GistsApi.md#gistsGetComment) | **GET** /gists/{gist_id}/comments/{comment_id} | Get a gist comment |
| [**gistsGetRevision**](GistsApi.md#gistsGetRevision) | **GET** /gists/{gist_id}/{sha} | Get a gist revision |
| [**gistsList**](GistsApi.md#gistsList) | **GET** /gists | List gists for the authenticated user |
| [**gistsListComments**](GistsApi.md#gistsListComments) | **GET** /gists/{gist_id}/comments | List gist comments |
| [**gistsListCommits**](GistsApi.md#gistsListCommits) | **GET** /gists/{gist_id}/commits | List gist commits |
| [**gistsListForUser**](GistsApi.md#gistsListForUser) | **GET** /users/{username}/gists | List gists for a user |
| [**gistsListForks**](GistsApi.md#gistsListForks) | **GET** /gists/{gist_id}/forks | List gist forks |
| [**gistsListPublic**](GistsApi.md#gistsListPublic) | **GET** /gists/public | List public gists |
| [**gistsListStarred**](GistsApi.md#gistsListStarred) | **GET** /gists/starred | List starred gists |
| [**gistsStar**](GistsApi.md#gistsStar) | **PUT** /gists/{gist_id}/star | Star a gist |
| [**gistsUnstar**](GistsApi.md#gistsUnstar) | **DELETE** /gists/{gist_id}/star | Unstar a gist |
| [**gistsUpdate**](GistsApi.md#gistsUpdate) | **PATCH** /gists/{gist_id} | Update a gist |
| [**gistsUpdateComment**](GistsApi.md#gistsUpdateComment) | **PATCH** /gists/{gist_id}/comments/{comment_id} | Update a gist comment |


<a id="gistsCheckIsStarred"></a>
# **gistsCheckIsStarred**
> gistsCheckIsStarred(gistId)

Check if a gist is starred



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      apiInstance.gistsCheckIsStarred(gistId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsCheckIsStarred");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response if gist is starred |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found if gist is not starred |  -  |

<a id="gistsCreate"></a>
# **gistsCreate**
> GistSimple gistsCreate(gistsCreateRequest)

Create a gist

Allows you to add a new gist with one or more files.  **Note:** Don&#39;t name your files \&quot;gistfile\&quot; with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    GistsCreateRequest gistsCreateRequest = new GistsCreateRequest(); // GistsCreateRequest | 
    try {
      GistSimple result = apiInstance.gistsCreate(gistsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsCreate");
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
| **gistsCreateRequest** | [**GistsCreateRequest**](GistsCreateRequest.md)|  | |

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="gistsCreateComment"></a>
# **gistsCreateComment**
> GistComment gistsCreateComment(gistId, gistsCreateCommentRequest)

Create a gist comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    GistsCreateCommentRequest gistsCreateCommentRequest = new GistsCreateCommentRequest(); // GistsCreateCommentRequest | 
    try {
      GistComment result = apiInstance.gistsCreateComment(gistId, gistsCreateCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsCreateComment");
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
| **gistId** | **String**| gist_id parameter | |
| **gistsCreateCommentRequest** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | |

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsDelete"></a>
# **gistsDelete**
> gistsDelete(gistId)

Delete a gist



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      apiInstance.gistsDelete(gistId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsDelete");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsDeleteComment"></a>
# **gistsDeleteComment**
> gistsDeleteComment(gistId, commentId)

Delete a gist comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      apiInstance.gistsDeleteComment(gistId, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsDeleteComment");
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
| **gistId** | **String**| gist_id parameter | |
| **commentId** | **Integer**| comment_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsFork"></a>
# **gistsFork**
> BaseGist gistsFork(gistId)

Fork a gist

**Note**: This was previously &#x60;/gists/:gist_id/fork&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      BaseGist result = apiInstance.gistsFork(gistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsFork");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

[**BaseGist**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="gistsGet"></a>
# **gistsGet**
> GistSimple gistsGet(gistId)

Get a gist



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      GistSimple result = apiInstance.gistsGet(gistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsGet");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden Gist |  -  |
| **404** | Resource not found |  -  |

<a id="gistsGetComment"></a>
# **gistsGetComment**
> GistComment gistsGetComment(gistId, commentId)

Get a gist comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      GistComment result = apiInstance.gistsGetComment(gistId, commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsGetComment");
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
| **gistId** | **String**| gist_id parameter | |
| **commentId** | **Integer**| comment_id parameter | |

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden Gist |  -  |
| **404** | Resource not found |  -  |

<a id="gistsGetRevision"></a>
# **gistsGetRevision**
> GistSimple gistsGetRevision(gistId, sha)

Get a gist revision



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    String sha = "sha_example"; // String | 
    try {
      GistSimple result = apiInstance.gistsGetRevision(gistId, sha);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsGetRevision");
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
| **gistId** | **String**| gist_id parameter | |
| **sha** | **String**|  | |

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="gistsList"></a>
# **gistsList**
> List&lt;BaseGist&gt; gistsList(since, perPage, page)

List gists for the authenticated user

Lists the authenticated user&#39;s gists or if called anonymously, this endpoint returns all public gists:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<BaseGist> result = apiInstance.gistsList(since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsList");
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
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;BaseGist&gt;**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |

<a id="gistsListComments"></a>
# **gistsListComments**
> List&lt;GistComment&gt; gistsListComments(gistId, perPage, page)

List gist comments



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<GistComment> result = apiInstance.gistsListComments(gistId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListComments");
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
| **gistId** | **String**| gist_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;GistComment&gt;**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsListCommits"></a>
# **gistsListCommits**
> List&lt;GistCommit&gt; gistsListCommits(gistId, perPage, page)

List gist commits



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<GistCommit> result = apiInstance.gistsListCommits(gistId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListCommits");
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
| **gistId** | **String**| gist_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;GistCommit&gt;**](GistCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsListForUser"></a>
# **gistsListForUser**
> List&lt;BaseGist&gt; gistsListForUser(username, since, perPage, page)

List gists for a user

Lists public gists for the specified user:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String username = "username_example"; // String | 
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<BaseGist> result = apiInstance.gistsListForUser(username, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListForUser");
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
| **username** | **String**|  | |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;BaseGist&gt;**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **422** | Validation failed |  -  |

<a id="gistsListForks"></a>
# **gistsListForks**
> List&lt;GistSimple&gt; gistsListForks(gistId, perPage, page)

List gist forks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<GistSimple> result = apiInstance.gistsListForks(gistId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListForks");
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
| **gistId** | **String**| gist_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;GistSimple&gt;**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsListPublic"></a>
# **gistsListPublic**
> List&lt;BaseGist&gt; gistsListPublic(since, perPage, page)

List public gists

List public gists sorted by most recently updated to least recently updated.  Note: With [pagination](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<BaseGist> result = apiInstance.gistsListPublic(since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListPublic");
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
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;BaseGist&gt;**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="gistsListStarred"></a>
# **gistsListStarred**
> List&lt;BaseGist&gt; gistsListStarred(since, perPage, page)

List starred gists

List the authenticated user&#39;s starred gists:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<BaseGist> result = apiInstance.gistsListStarred(since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsListStarred");
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
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;BaseGist&gt;**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="gistsStar"></a>
# **gistsStar**
> gistsStar(gistId)

Star a gist

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      apiInstance.gistsStar(gistId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsStar");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsUnstar"></a>
# **gistsUnstar**
> gistsUnstar(gistId)

Unstar a gist



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    try {
      apiInstance.gistsUnstar(gistId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsUnstar");
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
| **gistId** | **String**| gist_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="gistsUpdate"></a>
# **gistsUpdate**
> GistSimple gistsUpdate(gistId, gistsUpdateRequest)

Update a gist

Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren&#39;t explicitly changed during an edit are unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    GistsUpdateRequest gistsUpdateRequest = new GistsUpdateRequest(); // GistsUpdateRequest | 
    try {
      GistSimple result = apiInstance.gistsUpdate(gistId, gistsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsUpdate");
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
| **gistId** | **String**| gist_id parameter | |
| **gistsUpdateRequest** | [**GistsUpdateRequest**](GistsUpdateRequest.md)|  | |

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="gistsUpdateComment"></a>
# **gistsUpdateComment**
> GistComment gistsUpdateComment(gistId, commentId, gistsCreateCommentRequest)

Update a gist comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GistsApi apiInstance = new GistsApi(defaultClient);
    String gistId = "gistId_example"; // String | gist_id parameter
    Integer commentId = 56; // Integer | comment_id parameter
    GistsCreateCommentRequest gistsCreateCommentRequest = new GistsCreateCommentRequest(); // GistsCreateCommentRequest | 
    try {
      GistComment result = apiInstance.gistsUpdateComment(gistId, commentId, gistsCreateCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GistsApi#gistsUpdateComment");
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
| **gistId** | **String**| gist_id parameter | |
| **commentId** | **Integer**| comment_id parameter | |
| **gistsCreateCommentRequest** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | |

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

