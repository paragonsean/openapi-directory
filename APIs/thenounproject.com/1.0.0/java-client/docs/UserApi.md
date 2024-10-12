# UserApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserCollection**](UserApi.md#getUserCollection) | **GET** /user/{user_id}/collections/{slug} | Get user collection |
| [**getUserCollections**](UserApi.md#getUserCollections) | **GET** /user/{user_id}/collections | Get user collections |
| [**getUserUploadsWithUser**](UserApi.md#getUserUploadsWithUser) | **GET** /user/{username}/uploads | Get user uploads with user |


<a id="getUserCollection"></a>
# **getUserCollection**
> getUserCollection(userId, slug)

Get user collection

Returns a single collection associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | User id
    String slug = "slug_example"; // String | Collection slug
    try {
      apiInstance.getUserCollection(userId, slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserCollection");
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
| **userId** | **Integer**| User id | |
| **slug** | **String**| Collection slug | |

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
| **200** | No response was specified |  -  |

<a id="getUserCollections"></a>
# **getUserCollections**
> getUserCollections(userId)

Get user collections

Returns a list of collections associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | User id
    try {
      apiInstance.getUserCollections(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserCollections");
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
| **userId** | **Integer**| User id | |

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
| **200** | No response was specified |  -  |

<a id="getUserUploadsWithUser"></a>
# **getUserUploadsWithUser**
> getUserUploadsWithUser(username, limit, offset, page)

Get user uploads with user

Returns a list of uploads associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    UserApi apiInstance = new UserApi(defaultClient);
    String username = "username_example"; // String | Username
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getUserUploadsWithUser(username, limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserUploadsWithUser");
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
| **username** | **String**| Username | |
| **limit** | **Integer**| Maximum number of results | [optional] |
| **offset** | **Integer**| Number of results to displace or skip over | [optional] |
| **page** | **Integer**| Number of results of limit length to displace or skip over | [optional] |

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
| **200** | No response was specified |  -  |

