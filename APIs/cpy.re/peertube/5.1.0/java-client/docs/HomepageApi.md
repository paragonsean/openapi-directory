# HomepageApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1CustomPagesHomepageInstanceGet**](HomepageApi.md#apiV1CustomPagesHomepageInstanceGet) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage |
| [**apiV1CustomPagesHomepageInstancePut**](HomepageApi.md#apiV1CustomPagesHomepageInstancePut) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage |


<a id="apiV1CustomPagesHomepageInstanceGet"></a>
# **apiV1CustomPagesHomepageInstanceGet**
> CustomHomepage apiV1CustomPagesHomepageInstanceGet()

Get instance custom homepage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HomepageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    HomepageApi apiInstance = new HomepageApi(defaultClient);
    try {
      CustomHomepage result = apiInstance.apiV1CustomPagesHomepageInstanceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HomepageApi#apiV1CustomPagesHomepageInstanceGet");
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

[**CustomHomepage**](CustomHomepage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | No homepage set |  -  |

<a id="apiV1CustomPagesHomepageInstancePut"></a>
# **apiV1CustomPagesHomepageInstancePut**
> apiV1CustomPagesHomepageInstancePut(apiV1CustomPagesHomepageInstancePutRequest)

Set instance custom homepage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HomepageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HomepageApi apiInstance = new HomepageApi(defaultClient);
    ApiV1CustomPagesHomepageInstancePutRequest apiV1CustomPagesHomepageInstancePutRequest = new ApiV1CustomPagesHomepageInstancePutRequest(); // ApiV1CustomPagesHomepageInstancePutRequest | 
    try {
      apiInstance.apiV1CustomPagesHomepageInstancePut(apiV1CustomPagesHomepageInstancePutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HomepageApi#apiV1CustomPagesHomepageInstancePut");
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
| **apiV1CustomPagesHomepageInstancePutRequest** | [**ApiV1CustomPagesHomepageInstancePutRequest**](ApiV1CustomPagesHomepageInstancePutRequest.md)|  | [optional] |

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

