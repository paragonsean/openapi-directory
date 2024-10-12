# AppStoreVersionPhasedReleasesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreVersionPhasedReleasesCreateInstance**](AppStoreVersionPhasedReleasesApi.md#appStoreVersionPhasedReleasesCreateInstance) | **POST** /v1/appStoreVersionPhasedReleases |  |
| [**appStoreVersionPhasedReleasesDeleteInstance**](AppStoreVersionPhasedReleasesApi.md#appStoreVersionPhasedReleasesDeleteInstance) | **DELETE** /v1/appStoreVersionPhasedReleases/{id} |  |
| [**appStoreVersionPhasedReleasesUpdateInstance**](AppStoreVersionPhasedReleasesApi.md#appStoreVersionPhasedReleasesUpdateInstance) | **PATCH** /v1/appStoreVersionPhasedReleases/{id} |  |


<a id="appStoreVersionPhasedReleasesCreateInstance"></a>
# **appStoreVersionPhasedReleasesCreateInstance**
> AppStoreVersionPhasedReleaseResponse appStoreVersionPhasedReleasesCreateInstance(appStoreVersionPhasedReleaseCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionPhasedReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionPhasedReleasesApi apiInstance = new AppStoreVersionPhasedReleasesApi(defaultClient);
    AppStoreVersionPhasedReleaseCreateRequest appStoreVersionPhasedReleaseCreateRequest = new AppStoreVersionPhasedReleaseCreateRequest(); // AppStoreVersionPhasedReleaseCreateRequest | AppStoreVersionPhasedRelease representation
    try {
      AppStoreVersionPhasedReleaseResponse result = apiInstance.appStoreVersionPhasedReleasesCreateInstance(appStoreVersionPhasedReleaseCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionPhasedReleasesApi#appStoreVersionPhasedReleasesCreateInstance");
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
| **appStoreVersionPhasedReleaseCreateRequest** | [**AppStoreVersionPhasedReleaseCreateRequest**](AppStoreVersionPhasedReleaseCreateRequest.md)| AppStoreVersionPhasedRelease representation | |

### Return type

[**AppStoreVersionPhasedReleaseResponse**](AppStoreVersionPhasedReleaseResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreVersionPhasedRelease |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionPhasedReleasesDeleteInstance"></a>
# **appStoreVersionPhasedReleasesDeleteInstance**
> appStoreVersionPhasedReleasesDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionPhasedReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionPhasedReleasesApi apiInstance = new AppStoreVersionPhasedReleasesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appStoreVersionPhasedReleasesDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionPhasedReleasesApi#appStoreVersionPhasedReleasesDeleteInstance");
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
| **id** | **String**| the id of the requested resource | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionPhasedReleasesUpdateInstance"></a>
# **appStoreVersionPhasedReleasesUpdateInstance**
> AppStoreVersionPhasedReleaseResponse appStoreVersionPhasedReleasesUpdateInstance(id, appStoreVersionPhasedReleaseUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionPhasedReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionPhasedReleasesApi apiInstance = new AppStoreVersionPhasedReleasesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreVersionPhasedReleaseUpdateRequest appStoreVersionPhasedReleaseUpdateRequest = new AppStoreVersionPhasedReleaseUpdateRequest(); // AppStoreVersionPhasedReleaseUpdateRequest | AppStoreVersionPhasedRelease representation
    try {
      AppStoreVersionPhasedReleaseResponse result = apiInstance.appStoreVersionPhasedReleasesUpdateInstance(id, appStoreVersionPhasedReleaseUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionPhasedReleasesApi#appStoreVersionPhasedReleasesUpdateInstance");
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
| **id** | **String**| the id of the requested resource | |
| **appStoreVersionPhasedReleaseUpdateRequest** | [**AppStoreVersionPhasedReleaseUpdateRequest**](AppStoreVersionPhasedReleaseUpdateRequest.md)| AppStoreVersionPhasedRelease representation | |

### Return type

[**AppStoreVersionPhasedReleaseResponse**](AppStoreVersionPhasedReleaseResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreVersionPhasedRelease |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

