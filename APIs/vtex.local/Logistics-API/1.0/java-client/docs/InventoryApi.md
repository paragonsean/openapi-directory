# InventoryApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSupplyLots**](InventoryApi.md#getSupplyLots) | **GET** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots | List supply lots |
| [**getinventorywithdispatchedreservations**](InventoryApi.md#getinventorywithdispatchedreservations) | **GET** /api/logistics/pvt/inventory/items/{itemId}/warehouses/{warehouseId}/dispatched | List inventory with dispatched reservations |
| [**inventoryBySku**](InventoryApi.md#inventoryBySku) | **GET** /api/logistics/pvt/inventory/skus/{skuId} | List inventory by SKU |
| [**inventoryperdock**](InventoryApi.md#inventoryperdock) | **GET** /api/logistics/pvt/inventory/items/{skuId}/docks/{dockId} | List inventory per dock |
| [**inventoryperdockandwarehouse**](InventoryApi.md#inventoryperdockandwarehouse) | **GET** /api/logistics/pvt/inventory/items/{skuId}/docks/{dockId}/warehouses/{warehouseId} | List inventory per dock and warehouse |
| [**inventoryperwarehouse**](InventoryApi.md#inventoryperwarehouse) | **GET** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId} | List inventory per warehouse |
| [**saveSupplyLot**](InventoryApi.md#saveSupplyLot) | **PUT** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots/{supplyLotId} | Save supply lot |
| [**transferSupplyLot**](InventoryApi.md#transferSupplyLot) | **POST** /api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}/supplyLots/{supplyLotId}/transfer | Transfer supply lot |
| [**updateInventoryBySkuandWarehouse**](InventoryApi.md#updateInventoryBySkuandWarehouse) | **PUT** /api/logistics/pvt/inventory/skus/{skuId}/warehouses/{warehouseId} | Update inventory by SKU and warehouse |


<a id="getSupplyLots"></a>
# **getSupplyLots**
> getSupplyLots(accept, contentType, skuId, warehouseId)

List supply lots

Returns a list of the supply lots of an SKU in a specific warehouse.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent.
    String skuId = "skuId_example"; // String | ID of the SKU.
    String warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU is located.
    try {
      apiInstance.getSupplyLots(accept, contentType, skuId, warehouseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getSupplyLots");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Type of the content being sent. | |
| **skuId** | **String**| ID of the SKU. | |
| **warehouseId** | **String**| ID of the warehouse where the SKU is located. | |

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

<a id="getinventorywithdispatchedreservations"></a>
# **getinventorywithdispatchedreservations**
> List&lt;Getinventorywithdispatchedreservations200ResponseInner&gt; getinventorywithdispatchedreservations(contentType, accept, itemId, warehouseId)

List inventory with dispatched reservations

Lists inventory with dispatched reservations. When the number of active reservations is more than 2000 the return is an error with status code 400 (BadRequest) and the message: Too many active reservations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String itemId = "itemId_example"; // String | 
    String warehouseId = "warehouseId_example"; // String | 
    try {
      List<Getinventorywithdispatchedreservations200ResponseInner> result = apiInstance.getinventorywithdispatchedreservations(contentType, accept, itemId, warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getinventorywithdispatchedreservations");
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
| **itemId** | **String**|  | |
| **warehouseId** | **String**|  | |

### Return type

[**List&lt;Getinventorywithdispatchedreservations200ResponseInner&gt;**](Getinventorywithdispatchedreservations200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inventoryBySku"></a>
# **inventoryBySku**
> InventoryBySku200Response inventoryBySku(contentType, accept, skuId)

List inventory by SKU

Lists your store&#39;s inventory by SKU ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String skuId = "skuId_example"; // String | 
    try {
      InventoryBySku200Response result = apiInstance.inventoryBySku(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#inventoryBySku");
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
| **skuId** | **String**|  | |

### Return type

[**InventoryBySku200Response**](InventoryBySku200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |

<a id="inventoryperdock"></a>
# **inventoryperdock**
> List&lt;Inventoryperdock200ResponseInner&gt; inventoryperdock(contentType, accept, skuId, dockId)

List inventory per dock

Lists inventory information per dock set up in your store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String skuId = "skuId_example"; // String | 
    String dockId = "dockId_example"; // String | 
    try {
      List<Inventoryperdock200ResponseInner> result = apiInstance.inventoryperdock(contentType, accept, skuId, dockId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#inventoryperdock");
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
| **skuId** | **String**|  | |
| **dockId** | **String**|  | |

### Return type

[**List&lt;Inventoryperdock200ResponseInner&gt;**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inventoryperdockandwarehouse"></a>
# **inventoryperdockandwarehouse**
> List&lt;Inventoryperdock200ResponseInner&gt; inventoryperdockandwarehouse(contentType, accept, skuId, dockId, warehouseId)

List inventory per dock and warehouse

Lists information of inventory per dock and warehouse.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String skuId = "skuId_example"; // String | 
    String dockId = "dockId_example"; // String | 
    String warehouseId = "warehouseId_example"; // String | 
    try {
      List<Inventoryperdock200ResponseInner> result = apiInstance.inventoryperdockandwarehouse(contentType, accept, skuId, dockId, warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#inventoryperdockandwarehouse");
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
| **skuId** | **String**|  | |
| **dockId** | **String**|  | |
| **warehouseId** | **String**|  | |

### Return type

[**List&lt;Inventoryperdock200ResponseInner&gt;**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inventoryperwarehouse"></a>
# **inventoryperwarehouse**
> List&lt;Inventoryperdock200ResponseInner&gt; inventoryperwarehouse(contentType, accept, skuId, warehouseId)

List inventory per warehouse

Lists inventory information per warehouse on your store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String skuId = "skuId_example"; // String | 
    String warehouseId = "warehouseId_example"; // String | 
    try {
      List<Inventoryperdock200ResponseInner> result = apiInstance.inventoryperwarehouse(contentType, accept, skuId, warehouseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#inventoryperwarehouse");
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
| **skuId** | **String**|  | |
| **warehouseId** | **String**|  | |

### Return type

[**List&lt;Inventoryperdock200ResponseInner&gt;**](Inventoryperdock200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveSupplyLot"></a>
# **saveSupplyLot**
> saveSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId, saveSupplyLot)

Save supply lot

Creates a new Supply Lot. A Supply Lot lets the store sell products that are not currently available in stock but whose arrival is already scheduled.  Check out our [documentation](https://help.vtex.com/en/tutorial/setting-up-future-inventory--UMSGjooqRfkRbeoh94kS4) about this feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String skuId = "skuId_example"; // String | ID of the SKU whose availability is being scheduled.
    String warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU will arrive.
    String supplyLotId = "supplyLotId_example"; // String | ID of the Supply Lot in which the SKU's scheduling should be considered.
    SaveSupplyLot saveSupplyLot = new SaveSupplyLot(); // SaveSupplyLot | 
    try {
      apiInstance.saveSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId, saveSupplyLot);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#saveSupplyLot");
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
| **skuId** | **String**| ID of the SKU whose availability is being scheduled. | |
| **warehouseId** | **String**| ID of the warehouse where the SKU will arrive. | |
| **supplyLotId** | **String**| ID of the Supply Lot in which the SKU&#39;s scheduling should be considered. | |
| **saveSupplyLot** | [**SaveSupplyLot**](SaveSupplyLot.md)|  | |

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

<a id="transferSupplyLot"></a>
# **transferSupplyLot**
> transferSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId)

Transfer supply lot

Transfers an SKU from a Supply Lot to the currently available inventory.  Check out how this transfer works in further detail by reading our [documentation](https://help.vtex.com/pt/tutorial/configurar-estoque-futuro--UMSGjooqRfkRbeoh94kS4) about this feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String skuId = "skuId_example"; // String | ID of the SKU.
    String warehouseId = "warehouseId_example"; // String | ID of the warehouse where the SKU is located.
    String supplyLotId = "supplyLotId_example"; // String | ID of the Supply Lot in which the SKU is currently located and from where it will be transfered.
    try {
      apiInstance.transferSupplyLot(accept, contentType, skuId, warehouseId, supplyLotId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#transferSupplyLot");
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
| **skuId** | **String**| ID of the SKU. | |
| **warehouseId** | **String**| ID of the warehouse where the SKU is located. | |
| **supplyLotId** | **String**| ID of the Supply Lot in which the SKU is currently located and from where it will be transfered. | |

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

<a id="updateInventoryBySkuandWarehouse"></a>
# **updateInventoryBySkuandWarehouse**
> updateInventoryBySkuandWarehouse(accept, contentType, skuId, warehouseId, updateInventoryBySkuandWarehouseRequest1)

Update inventory by SKU and warehouse

Updates inventory for a given SKU and warehouse.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

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

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent.
    String skuId = "skuId_example"; // String | 
    String warehouseId = "warehouseId_example"; // String | 
    UpdateInventoryBySkuandWarehouseRequest1 updateInventoryBySkuandWarehouseRequest1 = new UpdateInventoryBySkuandWarehouseRequest1(); // UpdateInventoryBySkuandWarehouseRequest1 | 
    try {
      apiInstance.updateInventoryBySkuandWarehouse(accept, contentType, skuId, warehouseId, updateInventoryBySkuandWarehouseRequest1);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#updateInventoryBySkuandWarehouse");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json; charset&#x3D;utf-8] |
| **skuId** | **String**|  | |
| **warehouseId** | **String**|  | |
| **updateInventoryBySkuandWarehouseRequest1** | [**UpdateInventoryBySkuandWarehouseRequest1**](UpdateInventoryBySkuandWarehouseRequest1.md)|  | |

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

