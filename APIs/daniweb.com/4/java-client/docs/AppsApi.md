# AppsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsGet**](AppsApi.md#appsGet) | **GET** /apps |  |
| [**appsIDGet**](AppsApi.md#appsIDGet) | **GET** /apps/{ID} |  |


<a id="appsGet"></a>
# **appsGet**
> EndpointGetApps appsGet(offset, limit)



Fetch all Daniapps that are currently in production mode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetApps result = apiInstance.appsGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGet");
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
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetApps**](EndpointGetApps.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="appsIDGet"></a>
# **appsIDGet**
> EndpointGetAppsID appsIDGet(ID)



Fetch an array of Daniapps that are currently in production mode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetAppsID result = apiInstance.appsIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsIDGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetAppsID**](EndpointGetAppsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

