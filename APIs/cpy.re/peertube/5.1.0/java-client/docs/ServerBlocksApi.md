# ServerBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1BlocklistStatusGet_0**](ServerBlocksApi.md#apiV1BlocklistStatusGet_0) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts |
| [**apiV1ServerBlocklistServersGet**](ServerBlocksApi.md#apiV1ServerBlocklistServersGet) | **GET** /api/v1/server/blocklist/servers | List server blocks |
| [**apiV1ServerBlocklistServersHostDelete**](ServerBlocksApi.md#apiV1ServerBlocklistServersHostDelete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain |
| [**apiV1ServerBlocklistServersPost**](ServerBlocksApi.md#apiV1ServerBlocklistServersPost) | **POST** /api/v1/server/blocklist/servers | Block a server |


<a id="apiV1BlocklistStatusGet_0"></a>
# **apiV1BlocklistStatusGet_0**
> BlockStatus apiV1BlocklistStatusGet_0(accounts, hosts)

Get block status of accounts/hosts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    ServerBlocksApi apiInstance = new ServerBlocksApi(defaultClient);
    List<String> accounts = Arrays.asList(); // List<String> | Check if these accounts are blocked
    List<String> hosts = Arrays.asList(); // List<String> | Check if these hosts are blocked
    try {
      BlockStatus result = apiInstance.apiV1BlocklistStatusGet_0(accounts, hosts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerBlocksApi#apiV1BlocklistStatusGet_0");
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
| **accounts** | [**List&lt;String&gt;**](String.md)| Check if these accounts are blocked | [optional] |
| **hosts** | [**List&lt;String&gt;**](String.md)| Check if these hosts are blocked | [optional] |

### Return type

[**BlockStatus**](BlockStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerBlocklistServersGet"></a>
# **apiV1ServerBlocklistServersGet**
> apiV1ServerBlocklistServersGet(start, count, sort)

List server blocks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ServerBlocksApi apiInstance = new ServerBlocksApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      apiInstance.apiV1ServerBlocklistServersGet(start, count, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerBlocksApi#apiV1ServerBlocklistServersGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerBlocklistServersHostDelete"></a>
# **apiV1ServerBlocklistServersHostDelete**
> apiV1ServerBlocklistServersHostDelete(host)

Unblock a server by its domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ServerBlocksApi apiInstance = new ServerBlocksApi(defaultClient);
    String host = "host_example"; // String | server domain to unblock
    try {
      apiInstance.apiV1ServerBlocklistServersHostDelete(host);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerBlocksApi#apiV1ServerBlocklistServersHostDelete");
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
| **host** | **String**| server domain to unblock | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | account block does not exist |  -  |

<a id="apiV1ServerBlocklistServersPost"></a>
# **apiV1ServerBlocklistServersPost**
> apiV1ServerBlocklistServersPost(apiV1ServerBlocklistServersPostRequest)

Block a server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ServerBlocksApi apiInstance = new ServerBlocksApi(defaultClient);
    ApiV1ServerBlocklistServersPostRequest apiV1ServerBlocklistServersPostRequest = new ApiV1ServerBlocklistServersPostRequest(); // ApiV1ServerBlocklistServersPostRequest | 
    try {
      apiInstance.apiV1ServerBlocklistServersPost(apiV1ServerBlocklistServersPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerBlocksApi#apiV1ServerBlocklistServersPost");
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
| **apiV1ServerBlocklistServersPostRequest** | [**ApiV1ServerBlocklistServersPostRequest**](ApiV1ServerBlocklistServersPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **409** | self-blocking forbidden |  -  |

