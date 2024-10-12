# CommentsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**commentsIdDelete**](CommentsApi.md#commentsIdDelete) | **DELETE** /comments/{id} | Delete comment |
| [**commentsIdPatch**](CommentsApi.md#commentsIdPatch) | **PATCH** /comments/{id} | Update comment |
| [**mapsIdCommentsGet**](CommentsApi.md#mapsIdCommentsGet) | **GET** /maps/{id}/comments | List comments for a given map |
| [**mapsIdCommentsPost**](CommentsApi.md#mapsIdCommentsPost) | **POST** /maps/{id}/comments | Create map comment |
| [**spotsIdCommentsGet**](CommentsApi.md#spotsIdCommentsGet) | **GET** /spots/{id}/comments | List comments for a given spot |
| [**spotsIdCommentsPost**](CommentsApi.md#spotsIdCommentsPost) | **POST** /spots/{id}/comments | Create spot comment |


<a id="commentsIdDelete"></a>
# **commentsIdDelete**
> Comment commentsIdDelete(id)

Delete comment

Delete comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | Comment id
    try {
      Comment result = apiInstance.commentsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#commentsIdDelete");
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
| **id** | **Integer**| Comment id | |

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted comment. |  -  |

<a id="commentsIdPatch"></a>
# **commentsIdPatch**
> Comment commentsIdPatch(id, comment)

Update comment

Update comment. Wrap comment parameters in [comment].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | Comment id
    CommentEditable comment = new CommentEditable(); // CommentEditable | Comment attributes
    try {
      Comment result = apiInstance.commentsIdPatch(id, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#commentsIdPatch");
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
| **id** | **Integer**| Comment id | |
| **comment** | [**CommentEditable**](CommentEditable.md)| Comment attributes | [optional] |

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains comment data |  -  |

<a id="mapsIdCommentsGet"></a>
# **mapsIdCommentsGet**
> List&lt;Comment&gt; mapsIdCommentsGet(id)

List comments for a given map

List comments for a given map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    try {
      List<Comment> result = apiInstance.mapsIdCommentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#mapsIdCommentsGet");
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
| **id** | **Integer**| Id of map | |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of comments. |  -  |

<a id="mapsIdCommentsPost"></a>
# **mapsIdCommentsPost**
> Comment mapsIdCommentsPost(id, comment)

Create map comment

Create map comment. Wrap comment parameters in [comment].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | map id
    CommentEditable comment = new CommentEditable(); // CommentEditable | comment attributes
    try {
      Comment result = apiInstance.mapsIdCommentsPost(id, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#mapsIdCommentsPost");
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
| **id** | **Integer**| map id | |
| **comment** | [**CommentEditable**](CommentEditable.md)| comment attributes | [optional] |

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains comment data |  -  |

<a id="spotsIdCommentsGet"></a>
# **spotsIdCommentsGet**
> List&lt;Comment&gt; spotsIdCommentsGet(id)

List comments for a given spot

List comments for a given spot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | Id of spot
    try {
      List<Comment> result = apiInstance.spotsIdCommentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#spotsIdCommentsGet");
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
| **id** | **Integer**| Id of spot | |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of comments. |  -  |

<a id="spotsIdCommentsPost"></a>
# **spotsIdCommentsPost**
> Comment spotsIdCommentsPost(id, comment)

Create spot comment

Create spot comment. Wrap comment parameters in [comment].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 56; // Integer | spot id
    CommentEditable comment = new CommentEditable(); // CommentEditable | comment attributes
    try {
      Comment result = apiInstance.spotsIdCommentsPost(id, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#spotsIdCommentsPost");
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
| **id** | **Integer**| spot id | |
| **comment** | [**CommentEditable**](CommentEditable.md)| comment attributes | [optional] |

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains comment data |  -  |

