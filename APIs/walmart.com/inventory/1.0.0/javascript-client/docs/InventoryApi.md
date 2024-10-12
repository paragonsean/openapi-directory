# InventoryManagement.InventoryApi

All URIs are relative to *https://marketplace.walmartapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInventory**](InventoryApi.md#getInventory) | **GET** /v3/inventory | Inventory
[**getMultiNodeInventoryForAllSkuAndAllShipNodes**](InventoryApi.md#getMultiNodeInventoryForAllSkuAndAllShipNodes) | **GET** /v3/inventories | Multiple Item Inventory for All Ship Nodes
[**getMultiNodeInventoryForSkuAndAllShipnodes**](InventoryApi.md#getMultiNodeInventoryForSkuAndAllShipnodes) | **GET** /v3/inventories/{sku} | Single Item Inventory by Ship Node
[**getWFSInventory**](InventoryApi.md#getWFSInventory) | **GET** /v3/fulfillment/inventory | WFS Inventory
[**updateBulkInventory**](InventoryApi.md#updateBulkInventory) | **POST** /v3/feeds | Bulk Item Inventory Update
[**updateInventoryForAnItem**](InventoryApi.md#updateInventoryForAnItem) | **PUT** /v3/inventory | Update inventory
[**updateMultiNodeInventory**](InventoryApi.md#updateMultiNodeInventory) | **PUT** /v3/inventories/{sku} | Update Item Inventory per Ship Node



## getInventory

> GetInventory200Response getInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts)

Inventory

You can use this API to get the inventory for a given item.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let opts = {
  'shipNode': "shipNode_example", // String | The shipNode for which the inventory is requested
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.getInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | 
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **shipNode** | **String**| The shipNode for which the inventory is requested | [optional] 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**GetInventory200Response**](GetInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getMultiNodeInventoryForAllSkuAndAllShipNodes

> GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response getMultiNodeInventoryForAllSkuAndAllShipNodes(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts)

Multiple Item Inventory for All Ship Nodes

This API will retrieve the inventory count for all of a seller&#39;s items across all ship nodes by item to ship node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be passed on from the previous call to next call.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let opts = {
  'limit': "'10'", // String | The number of items returned. Cannot be more than 50.
  'nextCursor': "nextCursor_example", // String | String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items.
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.getMultiNodeInventoryForAllSkuAndAllShipNodes(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **limit** | **String**| The number of items returned. Cannot be more than 50. | [optional] [default to &#39;10&#39;]
 **nextCursor** | **String**| String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items. | [optional] 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response**](GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMultiNodeInventoryForSkuAndAllShipnodes

> GetMultiNodeInventoryForSkuAndAllShipnodes200Response getMultiNodeInventoryForSkuAndAllShipnodes(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts)

Single Item Inventory by Ship Node

This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You can specify the ship node for which you want to fetch the inventory

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let opts = {
  'shipNode': "shipNode_example", // String | ShipNode Id of the ship node for which the inventory is requested
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.getMultiNodeInventoryForSkuAndAllShipnodes(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | 
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **shipNode** | **String**| ShipNode Id of the ship node for which the inventory is requested | [optional] 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**GetMultiNodeInventoryForSkuAndAllShipnodes200Response**](GetMultiNodeInventoryForSkuAndAllShipnodes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWFSInventory

> GetWFSInventory200Response getWFSInventory(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts)

WFS Inventory

You can use this API to get the current Available to Sell inventory quantities for all WFS items in your catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to reduce the response size.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let opts = {
  'sku': "sku_example", // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
  'fromModifiedDate': "fromModifiedDate_example", // String | last inventory modified date - starting range.
  'toModifiedDate': "toModifiedDate_example", // String | last inventory modified date - starting range.
  'limit': "'10'", // String | Number of Sku to be returned. Cannot be larger than 300.
  'offset': "'0'", // String | Offset is the number of records you wish to skip before selecting records.
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.getWFSInventory(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | [optional] 
 **fromModifiedDate** | **String**| last inventory modified date - starting range. | [optional] 
 **toModifiedDate** | **String**| last inventory modified date - starting range. | [optional] 
 **limit** | **String**| Number of Sku to be returned. Cannot be larger than 300. | [optional] [default to &#39;10&#39;]
 **offset** | **String**| Offset is the number of records you wish to skip before selecting records. | [optional] [default to &#39;0&#39;]
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**GetWFSInventory200Response**](GetWFSInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBulkInventory

> UpdateBulkInventory200Response updateBulkInventory(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, file, opts)

Bulk Item Inventory Update

Updates inventory for items in bulk.  Seller Can either use feed type \&quot;inventory\&quot; or \&quot;MP_INVENTORY\&quot;  * Inventory spec 1.4 feed type: inventory  * Inventory spec 1.5 feed type: MP_INVENTORY   Please Note: Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY) only supports JSON Request and Responses. Refer to \&quot;MultiNode_Bulk_Inventory_Update_Request.json\&quot; for the corresponding request sample    Refer to the &lt;a href&#x3D;\&quot;https://developer.walmart.com/doc/us/us-mp/us-mp-inventory/\&quot;&gt;guide section&lt;/a&gt; for more detailed guide around each of the feed types    Refer to the throttling limits before uploading the Feed Files.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let feedType = "feedType_example"; // String | The feed Type
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let file = "/path/to/file"; // File | Feed file to upload
let opts = {
  'shipNode': "shipNode_example", // String | The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType=MP_INVENTORY)
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.updateBulkInventory(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, file, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedType** | **String**| The feed Type | 
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **file** | **File**| Feed file to upload | 
 **shipNode** | **String**| The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY) | [optional] 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**UpdateBulkInventory200Response**](UpdateBulkInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml


## updateInventoryForAnItem

> GetInventory200Response updateInventoryForAnItem(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getInventory200Response, opts)

Update inventory

Updates the inventory for a given item.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{', '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let getInventory200Response = {"quantity":{"amount":10,"unit":"EACH"},"sku":"97964_KFTest"}; // GetInventory200Response | File fields
let opts = {
  'shipNode': "shipNode_example", // String | The shipNode for which the inventory is to be updated.
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.updateInventoryForAnItem(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getInventory200Response, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | 
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **getInventory200Response** | [**GetInventory200Response**](GetInventory200Response.md)| File fields | 
 **shipNode** | **String**| The shipNode for which the inventory is to be updated. | [optional] 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**GetInventory200Response**](GetInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## updateMultiNodeInventory

> UpdateMultiNodeInventory200Response updateMultiNodeInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updateMultiNodeInventoryRequest, opts)

Update Item Inventory per Ship Node

This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.

### Example

```javascript
import InventoryManagement from 'inventory_management';

let apiInstance = new InventoryManagement.InventoryApi();
let sku = "sku_example"; // String | An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', \"'\", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't need to be encoded.
let WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
let WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
let WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
let updateMultiNodeInventoryRequest = {"inventories":{"nodes":[{"inputQty":{"amount":88,"unit":"EACH"},"shipNode":"1000005050"},{"inputQty":{"amount":55,"unit":"EACH"},"shipNode":"79897837271126017"}]}}; // UpdateMultiNodeInventoryRequest | Request fields
let opts = {
  'WM_CONSUMER_CHANNEL_TYPE': "WM_CONSUMER_CHANNEL_TYPE_example" // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
};
apiInstance.updateMultiNodeInventory(sku, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updateMultiNodeInventoryRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **String**| An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded. | 
 **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | 
 **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | 
 **WM_SVC_NAME** | **String**| Walmart Service Name | 
 **updateMultiNodeInventoryRequest** | [**UpdateMultiNodeInventoryRequest**](UpdateMultiNodeInventoryRequest.md)| Request fields | 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] 

### Return type

[**UpdateMultiNodeInventory200Response**](UpdateMultiNodeInventory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

