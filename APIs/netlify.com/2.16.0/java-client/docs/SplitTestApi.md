# SplitTestApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSplitTest**](SplitTestApi.md#createSplitTest) | **POST** /sites/{site_id}/traffic_splits |  |
| [**disableSplitTest**](SplitTestApi.md#disableSplitTest) | **POST** /sites/{site_id}/traffic_splits/{split_test_id}/unpublish |  |
| [**enableSplitTest**](SplitTestApi.md#enableSplitTest) | **POST** /sites/{site_id}/traffic_splits/{split_test_id}/publish |  |
| [**getSplitTest**](SplitTestApi.md#getSplitTest) | **GET** /sites/{site_id}/traffic_splits/{split_test_id} |  |
| [**getSplitTests**](SplitTestApi.md#getSplitTests) | **GET** /sites/{site_id}/traffic_splits |  |
| [**updateSplitTest**](SplitTestApi.md#updateSplitTest) | **PUT** /sites/{site_id}/traffic_splits/{split_test_id} |  |


<a id="createSplitTest"></a>
# **createSplitTest**
> SplitTest createSplitTest(siteId, branchTests)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    SplitTestSetup branchTests = new SplitTestSetup(); // SplitTestSetup | 
    try {
      SplitTest result = apiInstance.createSplitTest(siteId, branchTests);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#createSplitTest");
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
| **siteId** | **String**|  | |
| **branchTests** | [**SplitTestSetup**](SplitTestSetup.md)|  | |

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="disableSplitTest"></a>
# **disableSplitTest**
> disableSplitTest(siteId, splitTestId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String splitTestId = "splitTestId_example"; // String | 
    try {
      apiInstance.disableSplitTest(siteId, splitTestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#disableSplitTest");
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
| **siteId** | **String**|  | |
| **splitTestId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | disabled |  -  |
| **0** | error |  -  |

<a id="enableSplitTest"></a>
# **enableSplitTest**
> enableSplitTest(siteId, splitTestId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String splitTestId = "splitTestId_example"; // String | 
    try {
      apiInstance.enableSplitTest(siteId, splitTestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#enableSplitTest");
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
| **siteId** | **String**|  | |
| **splitTestId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | enable |  -  |
| **0** | error |  -  |

<a id="getSplitTest"></a>
# **getSplitTest**
> SplitTest getSplitTest(siteId, splitTestId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String splitTestId = "splitTestId_example"; // String | 
    try {
      SplitTest result = apiInstance.getSplitTest(siteId, splitTestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#getSplitTest");
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
| **siteId** | **String**|  | |
| **splitTestId** | **String**|  | |

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | split_test |  -  |
| **0** | error |  -  |

<a id="getSplitTests"></a>
# **getSplitTests**
> List&lt;SplitTest&gt; getSplitTests(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<SplitTest> result = apiInstance.getSplitTests(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#getSplitTests");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;SplitTest&gt;**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | split_tests |  -  |
| **0** | error |  -  |

<a id="updateSplitTest"></a>
# **updateSplitTest**
> SplitTest updateSplitTest(siteId, splitTestId, branchTests)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SplitTestApi apiInstance = new SplitTestApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String splitTestId = "splitTestId_example"; // String | 
    SplitTestSetup branchTests = new SplitTestSetup(); // SplitTestSetup | 
    try {
      SplitTest result = apiInstance.updateSplitTest(siteId, splitTestId, branchTests);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitTestApi#updateSplitTest");
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
| **siteId** | **String**|  | |
| **splitTestId** | **String**|  | |
| **branchTests** | [**SplitTestSetup**](SplitTestSetup.md)|  | |

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

