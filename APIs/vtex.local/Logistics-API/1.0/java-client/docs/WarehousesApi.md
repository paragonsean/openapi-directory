# WarehousesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateWarehouse**](WarehousesApi.md#activateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses/{warehouseId}/activation | Activate warehouse |
| [**allWarehouses**](WarehousesApi.md#allWarehouses) | **GET** /api/logistics/pvt/configuration/warehouses | List all warehouses |
| [**createUpdateWarehouse**](WarehousesApi.md#createUpdateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses | Create/update warehouse |
| [**deactivateWarehouse**](WarehousesApi.md#deactivateWarehouse) | **POST** /api/logistics/pvt/configuration/warehouses/{warehouseId}/deactivation | Deactivate warehouse |
| [**removeWarehouse**](WarehousesApi.md#removeWarehouse) | **DELETE** /api/logistics/pvt/configuration/warehouses/{warehouseId} | Remove warehouse |
| [**warehouseById**](WarehousesApi.md#warehouseById) | **GET** /api/logistics/pvt/configuration/warehouses/{warehouseId} | List warehouse by ID |


<a id="activateWarehouse"></a>
# **activateWarehouse**
> activateWarehouse(contentType, accept, warehouseId)

Activate warehouse

Activates a given warehouse, by warehouse ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String warehouseId = "warehouseId_example"; // String | 
    try {
      apiInstance.activateWarehouse(contentType, accept, warehouseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#activateWarehouse");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **warehouseId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="allWarehouses"></a>
# **allWarehouses**
> List&lt;AllWarehouses200ResponseInner&gt; allWarehouses(contentType, accept)

List all warehouses

Lists information about all warehouses set up in your store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    try {
      List<AllWarehouses200ResponseInner> result = apiInstance.allWarehouses(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#allWarehouses");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |

### Return type

[**List&lt;AllWarehouses200ResponseInner&gt;**](AllWarehouses200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Powered-by-VTEX-Janus-Router -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * x-vtex-operation-id -  <br>  |

<a id="createUpdateWarehouse"></a>
# **createUpdateWarehouse**
> createUpdateWarehouse(accept, contentType, createUpdateWarehouseRequest)

Create/update warehouse

Creates or updates your store&#39;s warehouses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    CreateUpdateWarehouseRequest createUpdateWarehouseRequest = new CreateUpdateWarehouseRequest(); // CreateUpdateWarehouseRequest | 
    try {
      apiInstance.createUpdateWarehouse(accept, contentType, createUpdateWarehouseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#createUpdateWarehouse");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **createUpdateWarehouseRequest** | [**CreateUpdateWarehouseRequest**](CreateUpdateWarehouseRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deactivateWarehouse"></a>
# **deactivateWarehouse**
> deactivateWarehouse(contentType, accept, warehouseId)

Deactivate warehouse

Deactivates a given warehouse by warehouse ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String warehouseId = "warehouseId_example"; // String | 
    try {
      apiInstance.deactivateWarehouse(contentType, accept, warehouseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#deactivateWarehouse");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **warehouseId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeWarehouse"></a>
# **removeWarehouse**
> removeWarehouse(contentType, accept, warehouseId)

Remove warehouse

Deletes given warehouse by warehouse ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String warehouseId = "warehouseId_example"; // String | 
    try {
      apiInstance.removeWarehouse(contentType, accept, warehouseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#removeWarehouse");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **warehouseId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="warehouseById"></a>
# **warehouseById**
> WarehouseById200Response warehouseById(contentType, accept, warehouseId)

List warehouse by ID

Lists the information of a given warehouse, searching by warehouse ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarehousesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String warehouseId = "warehouseId_example"; // String | 
    try {
      WarehouseById200Response result = apiInstance.warehouseById(contentType, accept, warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#warehouseById");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **warehouseId** | **String**|  | |

### Return type

[**WarehouseById200Response**](WarehouseById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Janus-Processado -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * X-VTEX-Janus-SO -  <br>  * x-vtex-operation-id -  <br>  |

