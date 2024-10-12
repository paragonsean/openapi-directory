# BundleIdCapabilitiesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleIdCapabilitiesCreateInstance**](BundleIdCapabilitiesApi.md#bundleIdCapabilitiesCreateInstance) | **POST** /v1/bundleIdCapabilities |  |
| [**bundleIdCapabilitiesDeleteInstance**](BundleIdCapabilitiesApi.md#bundleIdCapabilitiesDeleteInstance) | **DELETE** /v1/bundleIdCapabilities/{id} |  |
| [**bundleIdCapabilitiesUpdateInstance**](BundleIdCapabilitiesApi.md#bundleIdCapabilitiesUpdateInstance) | **PATCH** /v1/bundleIdCapabilities/{id} |  |


<a id="bundleIdCapabilitiesCreateInstance"></a>
# **bundleIdCapabilitiesCreateInstance**
> BundleIdCapabilityResponse bundleIdCapabilitiesCreateInstance(bundleIdCapabilityCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleIdCapabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BundleIdCapabilitiesApi apiInstance = new BundleIdCapabilitiesApi(defaultClient);
    BundleIdCapabilityCreateRequest bundleIdCapabilityCreateRequest = new BundleIdCapabilityCreateRequest(); // BundleIdCapabilityCreateRequest | BundleIdCapability representation
    try {
      BundleIdCapabilityResponse result = apiInstance.bundleIdCapabilitiesCreateInstance(bundleIdCapabilityCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleIdCapabilitiesApi#bundleIdCapabilitiesCreateInstance");
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
| **bundleIdCapabilityCreateRequest** | [**BundleIdCapabilityCreateRequest**](BundleIdCapabilityCreateRequest.md)| BundleIdCapability representation | |

### Return type

[**BundleIdCapabilityResponse**](BundleIdCapabilityResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BundleIdCapability |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="bundleIdCapabilitiesDeleteInstance"></a>
# **bundleIdCapabilitiesDeleteInstance**
> bundleIdCapabilitiesDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleIdCapabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BundleIdCapabilitiesApi apiInstance = new BundleIdCapabilitiesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.bundleIdCapabilitiesDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleIdCapabilitiesApi#bundleIdCapabilitiesDeleteInstance");
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

<a id="bundleIdCapabilitiesUpdateInstance"></a>
# **bundleIdCapabilitiesUpdateInstance**
> BundleIdCapabilityResponse bundleIdCapabilitiesUpdateInstance(id, bundleIdCapabilityUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleIdCapabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BundleIdCapabilitiesApi apiInstance = new BundleIdCapabilitiesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BundleIdCapabilityUpdateRequest bundleIdCapabilityUpdateRequest = new BundleIdCapabilityUpdateRequest(); // BundleIdCapabilityUpdateRequest | BundleIdCapability representation
    try {
      BundleIdCapabilityResponse result = apiInstance.bundleIdCapabilitiesUpdateInstance(id, bundleIdCapabilityUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleIdCapabilitiesApi#bundleIdCapabilitiesUpdateInstance");
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
| **bundleIdCapabilityUpdateRequest** | [**BundleIdCapabilityUpdateRequest**](BundleIdCapabilityUpdateRequest.md)| BundleIdCapability representation | |

### Return type

[**BundleIdCapabilityResponse**](BundleIdCapabilityResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BundleIdCapability |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

