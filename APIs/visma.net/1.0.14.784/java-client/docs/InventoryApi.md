# InventoryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inventoryGetList**](InventoryApi.md#inventoryGetList) | **GET** /api/v3/Inventory | Gets an inventory summary for inventory items. |


<a id="inventoryGetList"></a>
# **inventoryGetList**
> InventoryItemAvailabilityDtoPagedResult inventoryGetList(inventoryId, warehouseId, locationId, expand, modifiedSince, attributeFilter, pageSize, pageIndex)

Gets an inventory summary for inventory items.

Sample request:                GET /inventory?inventoryId&#x3D;Item1                GET /inventory?warehouseId&#x3D;MAIN&amp;modifiedSince&#x3D;2021-08-01T12:00:00&amp;pageSize&#x3D;1000                GET /inventory?inventoryId&#x3D;Item1&amp;InventoryId&#x3D;Item2&amp;expand&#x3D;location,attribute                GET /inventory?expand&#x3D;location&amp;attributeFilter&#x3D;WEBSHOP:1

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    List<String> inventoryId = Arrays.asList(); // List<String> | A list of zero or more inventory items to get a summary for. If no inventoryId is passed, all inventory items will be included in the response.
    List<String> warehouseId = Arrays.asList(); // List<String> | A list of zero or more warehouses to get a summary for. If no warehouse is supplied, all warehouses will be included in the response.
    List<String> locationId = Arrays.asList(); // List<String> | A list of zero or more locations to get a summary for. If no location is supplied, all locations will be included in the response.
    List<InventoryAvailabilityExpansions> expand = Arrays.asList(); // List<InventoryAvailabilityExpansions> | An additional option to include location detail information with the warehouse summary, or attribute details for the inventory item. If this is not supplied, location information or attributes will not be included in the response.
    OffsetDateTime modifiedSince = OffsetDateTime.now(); // OffsetDateTime | A date/time value for filtering when an inventory item's warehouse or location availability last changed  Unless a specific time zone offset is included (e.g. '2012-12-24T12:15:14+02:00'), the date is considered to be in the UTC time zone.
    List<String> attributeFilter = Arrays.asList(); // List<String> | One or more attribute filter values specified as attribute-id:attribute-value. For example \"attributeFilter=WEBSHOP:1&attributeFilter=AnotherAttribute:someValue\"  If two attributeFilter values have the same attribute-Id either one need to match.
    Integer pageSize = 56; // Integer | The number of inventory items retrieved per page. If not specified the default pagesize is 10000 items per page
    Integer pageIndex = 56; // Integer | Gets or sets the zero based page index to get
    try {
      InventoryItemAvailabilityDtoPagedResult result = apiInstance.inventoryGetList(inventoryId, warehouseId, locationId, expand, modifiedSince, attributeFilter, pageSize, pageIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#inventoryGetList");
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
| **inventoryId** | [**List&lt;String&gt;**](String.md)| A list of zero or more inventory items to get a summary for. If no inventoryId is passed, all inventory items will be included in the response. | [optional] |
| **warehouseId** | [**List&lt;String&gt;**](String.md)| A list of zero or more warehouses to get a summary for. If no warehouse is supplied, all warehouses will be included in the response. | [optional] |
| **locationId** | [**List&lt;String&gt;**](String.md)| A list of zero or more locations to get a summary for. If no location is supplied, all locations will be included in the response. | [optional] |
| **expand** | [**List&lt;InventoryAvailabilityExpansions&gt;**](InventoryAvailabilityExpansions.md)| An additional option to include location detail information with the warehouse summary, or attribute details for the inventory item. If this is not supplied, location information or attributes will not be included in the response. | [optional] |
| **modifiedSince** | **OffsetDateTime**| A date/time value for filtering when an inventory item&#39;s warehouse or location availability last changed  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone. | [optional] |
| **attributeFilter** | [**List&lt;String&gt;**](String.md)| One or more attribute filter values specified as attribute-id:attribute-value. For example \&quot;attributeFilter&#x3D;WEBSHOP:1&amp;attributeFilter&#x3D;AnotherAttribute:someValue\&quot;  If two attributeFilter values have the same attribute-Id either one need to match. | [optional] |
| **pageSize** | **Integer**| The number of inventory items retrieved per page. If not specified the default pagesize is 10000 items per page | [optional] |
| **pageIndex** | **Integer**| Gets or sets the zero based page index to get | [optional] |

### Return type

[**InventoryItemAvailabilityDtoPagedResult**](InventoryItemAvailabilityDtoPagedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of inventory items found |  -  |
| **400** | If modifiedSince is an invalid date, if expand contains an invalid value, or if any of the supplied attributeFilter(s) are invalid |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

