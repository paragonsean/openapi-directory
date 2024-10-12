# RoutingAppCoveragesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**routingAppCoveragesCreateInstance**](RoutingAppCoveragesApi.md#routingAppCoveragesCreateInstance) | **POST** /v1/routingAppCoverages |  |
| [**routingAppCoveragesDeleteInstance**](RoutingAppCoveragesApi.md#routingAppCoveragesDeleteInstance) | **DELETE** /v1/routingAppCoverages/{id} |  |
| [**routingAppCoveragesGetInstance**](RoutingAppCoveragesApi.md#routingAppCoveragesGetInstance) | **GET** /v1/routingAppCoverages/{id} |  |
| [**routingAppCoveragesUpdateInstance**](RoutingAppCoveragesApi.md#routingAppCoveragesUpdateInstance) | **PATCH** /v1/routingAppCoverages/{id} |  |


<a id="routingAppCoveragesCreateInstance"></a>
# **routingAppCoveragesCreateInstance**
> RoutingAppCoverageResponse routingAppCoveragesCreateInstance(routingAppCoverageCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingAppCoveragesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    RoutingAppCoveragesApi apiInstance = new RoutingAppCoveragesApi(defaultClient);
    RoutingAppCoverageCreateRequest routingAppCoverageCreateRequest = new RoutingAppCoverageCreateRequest(); // RoutingAppCoverageCreateRequest | RoutingAppCoverage representation
    try {
      RoutingAppCoverageResponse result = apiInstance.routingAppCoveragesCreateInstance(routingAppCoverageCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingAppCoveragesApi#routingAppCoveragesCreateInstance");
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
| **routingAppCoverageCreateRequest** | [**RoutingAppCoverageCreateRequest**](RoutingAppCoverageCreateRequest.md)| RoutingAppCoverage representation | |

### Return type

[**RoutingAppCoverageResponse**](RoutingAppCoverageResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single RoutingAppCoverage |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="routingAppCoveragesDeleteInstance"></a>
# **routingAppCoveragesDeleteInstance**
> routingAppCoveragesDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingAppCoveragesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    RoutingAppCoveragesApi apiInstance = new RoutingAppCoveragesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.routingAppCoveragesDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingAppCoveragesApi#routingAppCoveragesDeleteInstance");
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

<a id="routingAppCoveragesGetInstance"></a>
# **routingAppCoveragesGetInstance**
> RoutingAppCoverageResponse routingAppCoveragesGetInstance(id, fieldsRoutingAppCoverages, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingAppCoveragesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    RoutingAppCoveragesApi apiInstance = new RoutingAppCoveragesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsRoutingAppCoverages = Arrays.asList(); // List<String> | the fields to include for returned resources of type routingAppCoverages
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      RoutingAppCoverageResponse result = apiInstance.routingAppCoveragesGetInstance(id, fieldsRoutingAppCoverages, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingAppCoveragesApi#routingAppCoveragesGetInstance");
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
| **fieldsRoutingAppCoverages** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type routingAppCoverages | [optional] [enum: appStoreVersion, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreVersion] |

### Return type

[**RoutingAppCoverageResponse**](RoutingAppCoverageResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single RoutingAppCoverage |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="routingAppCoveragesUpdateInstance"></a>
# **routingAppCoveragesUpdateInstance**
> RoutingAppCoverageResponse routingAppCoveragesUpdateInstance(id, routingAppCoverageUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingAppCoveragesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    RoutingAppCoveragesApi apiInstance = new RoutingAppCoveragesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    RoutingAppCoverageUpdateRequest routingAppCoverageUpdateRequest = new RoutingAppCoverageUpdateRequest(); // RoutingAppCoverageUpdateRequest | RoutingAppCoverage representation
    try {
      RoutingAppCoverageResponse result = apiInstance.routingAppCoveragesUpdateInstance(id, routingAppCoverageUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingAppCoveragesApi#routingAppCoveragesUpdateInstance");
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
| **routingAppCoverageUpdateRequest** | [**RoutingAppCoverageUpdateRequest**](RoutingAppCoverageUpdateRequest.md)| RoutingAppCoverage representation | |

### Return type

[**RoutingAppCoverageResponse**](RoutingAppCoverageResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single RoutingAppCoverage |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

