# PostsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPostsDepartmentsTypeGet**](PostsApi.md#apiPostsDepartmentsTypeGet) | **GET** /api/Posts/Departments/{type} | Returns a list of departments. |
| [**apiPostsGovernmentPostsGet**](PostsApi.md#apiPostsGovernmentPostsGet) | **GET** /api/Posts/GovernmentPosts | Returns a list of government posts. |
| [**apiPostsOppositionPostsGet**](PostsApi.md#apiPostsOppositionPostsGet) | **GET** /api/Posts/OppositionPosts | Returns a list of opposition posts. |
| [**apiPostsSpeakerAndDeputiesForDateGet**](PostsApi.md#apiPostsSpeakerAndDeputiesForDateGet) | **GET** /api/Posts/SpeakerAndDeputies/{forDate} | Returns a list containing the speaker and deputy speakers. |
| [**apiPostsSpokespersonsGet**](PostsApi.md#apiPostsSpokespersonsGet) | **GET** /api/Posts/Spokespersons | Returns a list of spokespersons. |


<a id="apiPostsDepartmentsTypeGet"></a>
# **apiPostsDepartmentsTypeGet**
> List&lt;GovernmentDepartment&gt; apiPostsDepartmentsTypeGet(type)

Returns a list of departments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PostsApi apiInstance = new PostsApi(defaultClient);
    PostType type = PostType.fromValue("0"); // PostType | Departments by type
    try {
      List<GovernmentDepartment> result = apiInstance.apiPostsDepartmentsTypeGet(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#apiPostsDepartmentsTypeGet");
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
| **type** | [**PostType**](.md)| Departments by type | [enum: 0, 1, 2] |

### Return type

[**List&lt;GovernmentDepartment&gt;**](GovernmentDepartment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="apiPostsGovernmentPostsGet"></a>
# **apiPostsGovernmentPostsGet**
> List&lt;GovernmentOppositionPostItem&gt; apiPostsGovernmentPostsGet(departmentId)

Returns a list of government posts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PostsApi apiInstance = new PostsApi(defaultClient);
    Integer departmentId = 56; // Integer | Government posts by department ID
    try {
      List<GovernmentOppositionPostItem> result = apiInstance.apiPostsGovernmentPostsGet(departmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#apiPostsGovernmentPostsGet");
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
| **departmentId** | **Integer**| Government posts by department ID | [optional] |

### Return type

[**List&lt;GovernmentOppositionPostItem&gt;**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiPostsOppositionPostsGet"></a>
# **apiPostsOppositionPostsGet**
> List&lt;GovernmentOppositionPostItem&gt; apiPostsOppositionPostsGet(departmentId)

Returns a list of opposition posts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PostsApi apiInstance = new PostsApi(defaultClient);
    Integer departmentId = 56; // Integer | Opposition posts by department ID
    try {
      List<GovernmentOppositionPostItem> result = apiInstance.apiPostsOppositionPostsGet(departmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#apiPostsOppositionPostsGet");
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
| **departmentId** | **Integer**| Opposition posts by department ID | [optional] |

### Return type

[**List&lt;GovernmentOppositionPostItem&gt;**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiPostsSpeakerAndDeputiesForDateGet"></a>
# **apiPostsSpeakerAndDeputiesForDateGet**
> List&lt;MemberItem&gt; apiPostsSpeakerAndDeputiesForDateGet(forDate)

Returns a list containing the speaker and deputy speakers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PostsApi apiInstance = new PostsApi(defaultClient);
    OffsetDateTime forDate = OffsetDateTime.now(); // OffsetDateTime | Speaker and deputy speakers for date specified
    try {
      List<MemberItem> result = apiInstance.apiPostsSpeakerAndDeputiesForDateGet(forDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#apiPostsSpeakerAndDeputiesForDateGet");
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
| **forDate** | **OffsetDateTime**| Speaker and deputy speakers for date specified | |

### Return type

[**List&lt;MemberItem&gt;**](MemberItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiPostsSpokespersonsGet"></a>
# **apiPostsSpokespersonsGet**
> List&lt;GovernmentOppositionPostItem&gt; apiPostsSpokespersonsGet(partyId)

Returns a list of spokespersons.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PostsApi apiInstance = new PostsApi(defaultClient);
    Integer partyId = 56; // Integer | Spokespersons by party ID
    try {
      List<GovernmentOppositionPostItem> result = apiInstance.apiPostsSpokespersonsGet(partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostsApi#apiPostsSpokespersonsGet");
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
| **partyId** | **Integer**| Spokespersons by party ID | [optional] |

### Return type

[**List&lt;GovernmentOppositionPostItem&gt;**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

