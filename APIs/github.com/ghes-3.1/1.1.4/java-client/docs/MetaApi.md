# MetaApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metaGet**](MetaApi.md#metaGet) | **GET** /meta | Get GitHub Enterprise Server meta information |
| [**metaGetOctocat**](MetaApi.md#metaGetOctocat) | **GET** /octocat | Get Octocat |
| [**metaGetZen**](MetaApi.md#metaGetZen) | **GET** /zen | Get the Zen of GitHub |
| [**metaRoot**](MetaApi.md#metaRoot) | **GET** / | GitHub API Root |


<a id="metaGet"></a>
# **metaGet**
> ApiOverview metaGet()

Get GitHub Enterprise Server meta information



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    MetaApi apiInstance = new MetaApi(defaultClient);
    try {
      ApiOverview result = apiInstance.metaGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaApi#metaGet");
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

[**ApiOverview**](ApiOverview.md)

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

<a id="metaGetOctocat"></a>
# **metaGetOctocat**
> String metaGetOctocat(s)

Get Octocat

Get the octocat as ASCII art

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    MetaApi apiInstance = new MetaApi(defaultClient);
    String s = "s_example"; // String | The words to show in Octocat's speech bubble
    try {
      String result = apiInstance.metaGetOctocat(s);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaApi#metaGetOctocat");
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
| **s** | **String**| The words to show in Octocat&#39;s speech bubble | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octocat-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="metaGetZen"></a>
# **metaGetZen**
> String metaGetZen()

Get the Zen of GitHub

Get a random sentence from the Zen of GitHub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    MetaApi apiInstance = new MetaApi(defaultClient);
    try {
      String result = apiInstance.metaGetZen();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaApi#metaGetZen");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="metaRoot"></a>
# **metaRoot**
> Root metaRoot()

GitHub API Root

Get Hypermedia links to resources accessible in GitHub&#39;s REST API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    MetaApi apiInstance = new MetaApi(defaultClient);
    try {
      Root result = apiInstance.metaRoot();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaApi#metaRoot");
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

[**Root**](Root.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

