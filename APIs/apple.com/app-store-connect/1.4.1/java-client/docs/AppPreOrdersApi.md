# AppPreOrdersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appPreOrdersCreateInstance**](AppPreOrdersApi.md#appPreOrdersCreateInstance) | **POST** /v1/appPreOrders |  |
| [**appPreOrdersDeleteInstance**](AppPreOrdersApi.md#appPreOrdersDeleteInstance) | **DELETE** /v1/appPreOrders/{id} |  |
| [**appPreOrdersGetInstance**](AppPreOrdersApi.md#appPreOrdersGetInstance) | **GET** /v1/appPreOrders/{id} |  |
| [**appPreOrdersUpdateInstance**](AppPreOrdersApi.md#appPreOrdersUpdateInstance) | **PATCH** /v1/appPreOrders/{id} |  |


<a id="appPreOrdersCreateInstance"></a>
# **appPreOrdersCreateInstance**
> AppPreOrderResponse appPreOrdersCreateInstance(appPreOrderCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPreOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPreOrdersApi apiInstance = new AppPreOrdersApi(defaultClient);
    AppPreOrderCreateRequest appPreOrderCreateRequest = new AppPreOrderCreateRequest(); // AppPreOrderCreateRequest | AppPreOrder representation
    try {
      AppPreOrderResponse result = apiInstance.appPreOrdersCreateInstance(appPreOrderCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPreOrdersApi#appPreOrdersCreateInstance");
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
| **appPreOrderCreateRequest** | [**AppPreOrderCreateRequest**](AppPreOrderCreateRequest.md)| AppPreOrder representation | |

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppPreOrder |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appPreOrdersDeleteInstance"></a>
# **appPreOrdersDeleteInstance**
> appPreOrdersDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPreOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPreOrdersApi apiInstance = new AppPreOrdersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appPreOrdersDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPreOrdersApi#appPreOrdersDeleteInstance");
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

<a id="appPreOrdersGetInstance"></a>
# **appPreOrdersGetInstance**
> AppPreOrderResponse appPreOrdersGetInstance(id, fieldsAppPreOrders, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPreOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPreOrdersApi apiInstance = new AppPreOrdersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPreOrders = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreOrders
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppPreOrderResponse result = apiInstance.appPreOrdersGetInstance(id, fieldsAppPreOrders, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPreOrdersApi#appPreOrdersGetInstance");
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
| **fieldsAppPreOrders** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] [enum: app, appReleaseDate, preOrderAvailableDate] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app] |

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppPreOrder |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appPreOrdersUpdateInstance"></a>
# **appPreOrdersUpdateInstance**
> AppPreOrderResponse appPreOrdersUpdateInstance(id, appPreOrderUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPreOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPreOrdersApi apiInstance = new AppPreOrdersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppPreOrderUpdateRequest appPreOrderUpdateRequest = new AppPreOrderUpdateRequest(); // AppPreOrderUpdateRequest | AppPreOrder representation
    try {
      AppPreOrderResponse result = apiInstance.appPreOrdersUpdateInstance(id, appPreOrderUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPreOrdersApi#appPreOrdersUpdateInstance");
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
| **appPreOrderUpdateRequest** | [**AppPreOrderUpdateRequest**](AppPreOrderUpdateRequest.md)| AppPreOrder representation | |

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppPreOrder |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

