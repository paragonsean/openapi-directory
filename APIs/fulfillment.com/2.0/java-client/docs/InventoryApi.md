# InventoryApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInventory**](InventoryApi.md#getInventory) | **GET** /inventory | List of Item Inventories |


<a id="getInventory"></a>
# **getInventory**
> ItemInventoryArrayV2 getInventory(page, limit, merchantIds, warehouseIds, externalSkuNames)

List of Item Inventories

Retrieve inventory for one or more items. This API requires elevated permissions, please speak to your success manager.

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    Integer page = 1; // Integer | A multiplier of the number of items (limit parameter) to skip before returning results
    Integer limit = 80; // Integer | The numbers of items to return
    List<Integer> merchantIds = Arrays.asList(); // List<Integer> | A CSV of merchant id, '123' or '1,2,3'
    List<Integer> warehouseIds = Arrays.asList(); // List<Integer> | A CSV of warehouse id, '123' or '1,2,3'
    List<String> externalSkuNames = Arrays.asList(); // List<String> | A CSV of sku reference names, 'skuName1' or 'skuName1,skuName2,skuName3'
    try {
      ItemInventoryArrayV2 result = apiInstance.getInventory(page, limit, merchantIds, warehouseIds, externalSkuNames);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getInventory");
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
| **page** | **Integer**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1] |
| **limit** | **Integer**| The numbers of items to return | [optional] [default to 80] |
| **merchantIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of merchant id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |
| **warehouseIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |
| **externalSkuNames** | [**List&lt;String&gt;**](String.md)| A CSV of sku reference names, &#39;skuName1&#39; or &#39;skuName1,skuName2,skuName3&#39; | [optional] |

### Return type

[**ItemInventoryArrayV2**](ItemInventoryArrayV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Found Inventory |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Access Denied |  -  |
| **404** | No Inventory Found |  -  |

