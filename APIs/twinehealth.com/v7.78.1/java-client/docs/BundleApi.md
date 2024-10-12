# BundleApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBundle**](BundleApi.md#createBundle) | **POST** /bundle | Create bundle |
| [**fetchBundle**](BundleApi.md#fetchBundle) | **GET** /bundle/{id} | Get a bundle |
| [**updateBundle**](BundleApi.md#updateBundle) | **PATCH** /bundle/{id} | Update a bundle |


<a id="createBundle"></a>
# **createBundle**
> CreateBundleResponse createBundle(createBundleRequest)

Create bundle

Create a bundle in a patient&#39;s plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    BundleApi apiInstance = new BundleApi(defaultClient);
    CreateBundleRequest createBundleRequest = new CreateBundleRequest(); // CreateBundleRequest | 
    try {
      CreateBundleResponse result = apiInstance.createBundle(createBundleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleApi#createBundle");
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
| **createBundleRequest** | [**CreateBundleRequest**](CreateBundleRequest.md)|  | |

### Return type

[**CreateBundleResponse**](CreateBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchBundle"></a>
# **fetchBundle**
> FetchBundleResponse fetchBundle(id)

Get a bundle

Get a bundle from a patient&#39;s plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    BundleApi apiInstance = new BundleApi(defaultClient);
    String id = "id_example"; // String | Bundle identifier
    try {
      FetchBundleResponse result = apiInstance.fetchBundle(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleApi#fetchBundle");
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
| **id** | **String**| Bundle identifier | |

### Return type

[**FetchBundleResponse**](FetchBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="updateBundle"></a>
# **updateBundle**
> UpdateBundleResponse updateBundle(id, updateBundleRequest)

Update a bundle

Updte a bundle from a patient&#39;s plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    BundleApi apiInstance = new BundleApi(defaultClient);
    String id = "id_example"; // String | Bundle identifier
    UpdateBundleRequest updateBundleRequest = new UpdateBundleRequest(); // UpdateBundleRequest | 
    try {
      UpdateBundleResponse result = apiInstance.updateBundle(id, updateBundleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleApi#updateBundle");
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
| **id** | **String**| Bundle identifier | |
| **updateBundleRequest** | [**UpdateBundleRequest**](UpdateBundleRequest.md)|  | |

### Return type

[**UpdateBundleResponse**](UpdateBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

