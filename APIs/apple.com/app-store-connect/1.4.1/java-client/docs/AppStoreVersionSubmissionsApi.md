# AppStoreVersionSubmissionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreVersionSubmissionsCreateInstance**](AppStoreVersionSubmissionsApi.md#appStoreVersionSubmissionsCreateInstance) | **POST** /v1/appStoreVersionSubmissions |  |
| [**appStoreVersionSubmissionsDeleteInstance**](AppStoreVersionSubmissionsApi.md#appStoreVersionSubmissionsDeleteInstance) | **DELETE** /v1/appStoreVersionSubmissions/{id} |  |


<a id="appStoreVersionSubmissionsCreateInstance"></a>
# **appStoreVersionSubmissionsCreateInstance**
> AppStoreVersionSubmissionResponse appStoreVersionSubmissionsCreateInstance(appStoreVersionSubmissionCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionSubmissionsApi apiInstance = new AppStoreVersionSubmissionsApi(defaultClient);
    AppStoreVersionSubmissionCreateRequest appStoreVersionSubmissionCreateRequest = new AppStoreVersionSubmissionCreateRequest(); // AppStoreVersionSubmissionCreateRequest | AppStoreVersionSubmission representation
    try {
      AppStoreVersionSubmissionResponse result = apiInstance.appStoreVersionSubmissionsCreateInstance(appStoreVersionSubmissionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionSubmissionsApi#appStoreVersionSubmissionsCreateInstance");
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
| **appStoreVersionSubmissionCreateRequest** | [**AppStoreVersionSubmissionCreateRequest**](AppStoreVersionSubmissionCreateRequest.md)| AppStoreVersionSubmission representation | |

### Return type

[**AppStoreVersionSubmissionResponse**](AppStoreVersionSubmissionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreVersionSubmission |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionSubmissionsDeleteInstance"></a>
# **appStoreVersionSubmissionsDeleteInstance**
> appStoreVersionSubmissionsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionSubmissionsApi apiInstance = new AppStoreVersionSubmissionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appStoreVersionSubmissionsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionSubmissionsApi#appStoreVersionSubmissionsDeleteInstance");
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

