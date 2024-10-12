# WarehousesApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWarehouse**](WarehousesApi.md#createWarehouse) | **POST** /v1/warehouses | Create Warehouse |
| [**deleteWarehouse**](WarehousesApi.md#deleteWarehouse) | **DELETE** /v1/warehouses/{warehouse_id} | Delete Warehouse By ID |
| [**getWarehouseById**](WarehousesApi.md#getWarehouseById) | **GET** /v1/warehouses/{warehouse_id} | Get Warehouse By Id |
| [**listWarehouses**](WarehousesApi.md#listWarehouses) | **GET** /v1/warehouses | List Warehouses |
| [**updateWarehouse**](WarehousesApi.md#updateWarehouse) | **PUT** /v1/warehouses/{warehouse_id} | Update Warehouse By Id |
| [**updateWarehouseSettings**](WarehousesApi.md#updateWarehouseSettings) | **PUT** /v1/warehouses/{warehouse_id}/settings | Update Warehouse Settings |


<a id="createWarehouse"></a>
# **createWarehouse**
> CreateWarehouseResponseBody createWarehouse(createWarehouseRequestBody)

Create Warehouse

Create a warehouse location that you can use to create shipping items by simply passing in the generated warehouse id. If the return address is not supplied in the request body then it is assumed that the origin address is the return address as well 

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    CreateWarehouseRequestBody createWarehouseRequestBody = new CreateWarehouseRequestBody(); // CreateWarehouseRequestBody | 
    try {
      CreateWarehouseResponseBody result = apiInstance.createWarehouse(createWarehouseRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#createWarehouse");
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
| **createWarehouseRequestBody** | [**CreateWarehouseRequestBody**](CreateWarehouseRequestBody.md)|  | |

### Return type

[**CreateWarehouseResponseBody**](CreateWarehouseResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="deleteWarehouse"></a>
# **deleteWarehouse**
> String deleteWarehouse(warehouseId)

Delete Warehouse By ID

Delete a warehouse by ID

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    try {
      String result = apiInstance.deleteWarehouse(warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#deleteWarehouse");
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
| **warehouseId** | **String**| Warehouse ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getWarehouseById"></a>
# **getWarehouseById**
> GetWarehouseByIdResponseBody getWarehouseById(warehouseId)

Get Warehouse By Id

Retrieve warehouse data based on the warehouse ID

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    try {
      GetWarehouseByIdResponseBody result = apiInstance.getWarehouseById(warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#getWarehouseById");
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
| **warehouseId** | **String**| Warehouse ID | |

### Return type

[**GetWarehouseByIdResponseBody**](GetWarehouseByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listWarehouses"></a>
# **listWarehouses**
> ListWarehousesResponseBody listWarehouses()

List Warehouses

Retrieve a list of warehouses associated with this account.

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    try {
      ListWarehousesResponseBody result = apiInstance.listWarehouses();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#listWarehouses");
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

[**ListWarehousesResponseBody**](ListWarehousesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updateWarehouse"></a>
# **updateWarehouse**
> String updateWarehouse(warehouseId, updateWarehouseRequestBody)

Update Warehouse By Id

Update Warehouse object information

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    UpdateWarehouseRequestBody updateWarehouseRequestBody = new UpdateWarehouseRequestBody(); // UpdateWarehouseRequestBody | 
    try {
      String result = apiInstance.updateWarehouse(warehouseId, updateWarehouseRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#updateWarehouse");
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
| **warehouseId** | **String**| Warehouse ID | |
| **updateWarehouseRequestBody** | [**UpdateWarehouseRequestBody**](UpdateWarehouseRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updateWarehouseSettings"></a>
# **updateWarehouseSettings**
> String updateWarehouseSettings(warehouseId, updateWarehouseSettingsRequestBody)

Update Warehouse Settings

Update Warehouse settings object information

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
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    WarehousesApi apiInstance = new WarehousesApi(defaultClient);
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    UpdateWarehouseSettingsRequestBody updateWarehouseSettingsRequestBody = new UpdateWarehouseSettingsRequestBody(); // UpdateWarehouseSettingsRequestBody | 
    try {
      String result = apiInstance.updateWarehouseSettings(warehouseId, updateWarehouseSettingsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarehousesApi#updateWarehouseSettings");
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
| **warehouseId** | **String**| Warehouse ID | |
| **updateWarehouseSettingsRequestBody** | [**UpdateWarehouseSettingsRequestBody**](UpdateWarehouseSettingsRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

