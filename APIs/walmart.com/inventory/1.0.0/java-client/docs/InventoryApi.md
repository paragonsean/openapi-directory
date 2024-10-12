# InventoryApi

All URIs are relative to *https://marketplace.walmartapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInventory**](InventoryApi.md#getInventory) | **GET** /v3/inventory | Inventory |
| [**getMultiNodeInventoryForAllSkuAndAllShipNodes**](InventoryApi.md#getMultiNodeInventoryForAllSkuAndAllShipNodes) | **GET** /v3/inventories | Multiple Item Inventory for All Ship Nodes |
| [**getMultiNodeInventoryForSkuAndAllShipnodes**](InventoryApi.md#getMultiNodeInventoryForSkuAndAllShipnodes) | **GET** /v3/inventories/{sku} | Single Item Inventory by Ship Node |
| [**getWFSInventory**](InventoryApi.md#getWFSInventory) | **GET** /v3/fulfillment/inventory | WFS Inventory |
| [**updateBulkInventory**](InventoryApi.md#updateBulkInventory) | **POST** /v3/feeds | Bulk Item Inventory Update |
| [**updateInventoryForAnItem**](InventoryApi.md#updateInventoryForAnItem) | **PUT** /v3/inventory | Update inventory |
| [**updateMultiNodeInventory**](InventoryApi.md#updateMultiNodeInventory) | **PUT** /v3/inventories/{sku} | Update Item Inventory per Ship Node |


<a id="getInventory"></a>
# **getInventory**
> GetInventory200Response getInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, shipNode, WM_CONSUMER_CHANNEL_TYPE)

Inventory

You can use this API to get the inventory for a given item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String shipNode = "shipNode_example"; // String | The shipNode for which the inventory is requested
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetInventory200Response result = apiInstance.getInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, shipNode, WM_CONSUMER_CHANNEL_TYPE);
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
| **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **shipNode** | **String**| The shipNode for which the inventory is requested | [optional] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetInventory200Response**](GetInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getMultiNodeInventoryForAllSkuAndAllShipNodes"></a>
# **getMultiNodeInventoryForAllSkuAndAllShipNodes**
> GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response getMultiNodeInventoryForAllSkuAndAllShipNodes(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, limit, nextCursor, WM_CONSUMER_CHANNEL_TYPE)

Multiple Item Inventory for All Ship Nodes

This API will retrieve the inventory count for all of a seller&#39;s items across all ship nodes by item to ship node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be passed on from the previous call to next call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String limit = "10"; // String | The number of items returned. Cannot be more than 50.
    String nextCursor = "nextCursor_example"; // String | String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items.
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response result = apiInstance.getMultiNodeInventoryForAllSkuAndAllShipNodes(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, limit, nextCursor, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getMultiNodeInventoryForAllSkuAndAllShipNodes");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **limit** | **String**| The number of items returned. Cannot be more than 50. | [optional] [default to 10] |
| **nextCursor** | **String**| String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items. | [optional] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response**](GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getMultiNodeInventoryForSkuAndAllShipnodes"></a>
# **getMultiNodeInventoryForSkuAndAllShipnodes**
> GetMultiNodeInventoryForSkuAndAllShipnodes200Response getMultiNodeInventoryForSkuAndAllShipnodes(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, shipNode, WM_CONSUMER_CHANNEL_TYPE)

Single Item Inventory by Ship Node

This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You can specify the ship node for which you want to fetch the inventory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String shipNode = "shipNode_example"; // String | ShipNode Id of the ship node for which the inventory is requested
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetMultiNodeInventoryForSkuAndAllShipnodes200Response result = apiInstance.getMultiNodeInventoryForSkuAndAllShipnodes(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, shipNode, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getMultiNodeInventoryForSkuAndAllShipnodes");
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
| **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **shipNode** | **String**| ShipNode Id of the ship node for which the inventory is requested | [optional] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetMultiNodeInventoryForSkuAndAllShipnodes200Response**](GetMultiNodeInventoryForSkuAndAllShipnodes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getWFSInventory"></a>
# **getWFSInventory**
> GetWFSInventory200Response getWFSInventory(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, sku, fromModifiedDate, toModifiedDate, limit, offset, WM_CONSUMER_CHANNEL_TYPE)

WFS Inventory

You can use this API to get the current Available to Sell inventory quantities for all WFS items in your catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to reduce the response size.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
    String fromModifiedDate = "fromModifiedDate_example"; // String | last inventory modified date - starting range.
    String toModifiedDate = "toModifiedDate_example"; // String | last inventory modified date - starting range.
    String limit = "10"; // String | Number of Sku to be returned. Cannot be larger than 300.
    String offset = "0"; // String | Offset is the number of records you wish to skip before selecting records.
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetWFSInventory200Response result = apiInstance.getWFSInventory(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, sku, fromModifiedDate, toModifiedDate, limit, offset, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getWFSInventory");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | [optional] |
| **fromModifiedDate** | **String**| last inventory modified date - starting range. | [optional] |
| **toModifiedDate** | **String**| last inventory modified date - starting range. | [optional] |
| **limit** | **String**| Number of Sku to be returned. Cannot be larger than 300. | [optional] [default to 10] |
| **offset** | **String**| Offset is the number of records you wish to skip before selecting records. | [optional] [default to 0] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetWFSInventory200Response**](GetWFSInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateBulkInventory"></a>
# **updateBulkInventory**
> UpdateBulkInventory200Response updateBulkInventory(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, _file, shipNode, WM_CONSUMER_CHANNEL_TYPE)

Bulk Item Inventory Update

Updates inventory for items in bulk.  Seller Can either use feed type \&quot;inventory\&quot; or \&quot;MP_INVENTORY\&quot;  * Inventory spec 1.4 feed type: inventory  * Inventory spec 1.5 feed type: MP_INVENTORY   Please Note: Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY) only supports JSON Request and Responses. Refer to \&quot;MultiNode_Bulk_Inventory_Update_Request.json\&quot; for the corresponding request sample    Refer to the &lt;a href&#x3D;\&quot;https://developer.walmart.com/doc/us/us-mp/us-mp-inventory/\&quot;&gt;guide section&lt;/a&gt; for more detailed guide around each of the feed types    Refer to the throttling limits before uploading the Feed Files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String feedType = "inventory"; // String | The feed Type
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    File _file = new File("/path/to/file"); // File | Feed file to upload
    String shipNode = "shipNode_example"; // String | The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType=MP_INVENTORY)
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      UpdateBulkInventory200Response result = apiInstance.updateBulkInventory(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, _file, shipNode, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#updateBulkInventory");
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
| **feedType** | **String**| The feed Type | [enum: inventory, MP_INVENTORY] |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **_file** | **File**| Feed file to upload | |
| **shipNode** | **String**| The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY) | [optional] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**UpdateBulkInventory200Response**](UpdateBulkInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateInventoryForAnItem"></a>
# **updateInventoryForAnItem**
> GetInventory200Response updateInventoryForAnItem(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getInventory200Response, shipNode, WM_CONSUMER_CHANNEL_TYPE)

Update inventory

Updates the inventory for a given item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    GetInventory200Response getInventory200Response = new GetInventory200Response(); // GetInventory200Response | File fields
    String shipNode = "shipNode_example"; // String | The shipNode for which the inventory is to be updated.
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetInventory200Response result = apiInstance.updateInventoryForAnItem(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getInventory200Response, shipNode, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#updateInventoryForAnItem");
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
| **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **getInventory200Response** | [**GetInventory200Response**](GetInventory200Response.md)| File fields | |
| **shipNode** | **String**| The shipNode for which the inventory is to be updated. | [optional] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetInventory200Response**](GetInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateMultiNodeInventory"></a>
# **updateMultiNodeInventory**
> UpdateMultiNodeInventory200Response updateMultiNodeInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updateMultiNodeInventoryRequest, WM_CONSUMER_CHANNEL_TYPE)

Update Item Inventory per Ship Node

This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    UpdateMultiNodeInventoryRequest updateMultiNodeInventoryRequest = new UpdateMultiNodeInventoryRequest(); // UpdateMultiNodeInventoryRequest | Request fields
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      UpdateMultiNodeInventory200Response result = apiInstance.updateMultiNodeInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updateMultiNodeInventoryRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#updateMultiNodeInventory");
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
| **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **updateMultiNodeInventoryRequest** | [**UpdateMultiNodeInventoryRequest**](UpdateMultiNodeInventoryRequest.md)| Request fields | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**UpdateMultiNodeInventory200Response**](UpdateMultiNodeInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

