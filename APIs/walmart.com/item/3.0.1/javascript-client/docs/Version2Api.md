# ItemApi.Version2Api

All URIs are relative to *https://developer.walmart.com/proxy/item-api-doc-app/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2doPostMultiPart**](Version2Api.md#v2doPostMultiPart) | **POST** /v2/feeds | Upload an item feed
[**v2getAllItemsStatus**](Version2Api.md#v2getAllItemsStatus) | **GET** /v2/feeds/{feedId} | Get status of an item within a feed
[**v2getFeedItemStatus**](Version2Api.md#v2getFeedItemStatus) | **GET** /v2/feeds | Get status of an item feed



## v2doPostMultiPart

> v2doPostMultiPart(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, file, opts)

Upload an item feed

You can upload an item feed. If the feed successfully processed, it returns a feed ID. Use the returned feed ID to retrieve a feed status. You need your Consumer ID and the Private Key to upload an item.

### Example

```javascript
import ItemApi from 'item_api';

let apiInstance = new ItemApi.Version2Api();
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let file = "/path/to/file"; // File | Feed File to upload
let opts = {
  'feedType': "'item'" // String | Feed Type
};
apiInstance.v2doPostMultiPart(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, file, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **file** | **File**| Feed File to upload | 
 **feedType** | **String**| Feed Type | [optional] [default to &#39;item&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## v2getAllItemsStatus

> v2getAllItemsStatus(feedId, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Get status of an item within a feed

You can display the status of all items within a feed. Use the feed ID returned from the upload an item API.

### Example

```javascript
import ItemApi from 'item_api';

let apiInstance = new ItemApi.Version2Api();
let feedId = "feedId_example"; // String | The feed ID
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'includeDetails': "'false'", // String | Includes details of each entity in the feed. Do not set this parameter to true.
  'offset': "'0'", // String | The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
  'limit': "'50'" // String | The number of entities to be returned. It cannot be more than 50 entities. Use it only when the includeDetails is set to true.
};
apiInstance.v2getAllItemsStatus(feedId, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedId** | **String**| The feed ID | 
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **includeDetails** | **String**| Includes details of each entity in the feed. Do not set this parameter to true. | [optional] [default to &#39;false&#39;]
 **offset** | **String**| The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true. | [optional] [default to &#39;0&#39;]
 **limit** | **String**| The number of entities to be returned. It cannot be more than 50 entities. Use it only when the includeDetails is set to true. | [optional] [default to &#39;50&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2getFeedItemStatus

> v2getFeedItemStatus(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts)

Get status of an item feed

You can display the status of an item within a feed. Use the feed ID returned from the upload an item API.

### Example

```javascript
import ItemApi from 'item_api';

let apiInstance = new ItemApi.Version2Api();
let WM_CONSUMER_CHANNEL_TYPE = "'SWAGGER_CHANNEL_TYPE'"; // String | Channel Type
let WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
let WM_SEC_TIMESTAMP = "'Auto populated'"; // String | Epoch timestamp
let WM_SEC_AUTH_SIGNATURE = "'Auto populated'"; // String | Authentication signature
let WM_SVC_NAME = "'Walmart Marketplace'"; // String | The Service name
let WM_QOS_CORRELATION_ID = "'123456abcdef'"; // String | A Transaction ID
let opts = {
  'feedId': "feedId_example", // String | The feed ID.
  'includeDetails': "'false'", // String | Includes the status details for each item in the feed. Do not set this parameter to true as discrepancies may appear between the header and the item details (the item details may be incorrect). Instead, use the Get a feedItems status.
  'offset': "'0'", // String | The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
  'limit': "'50'" // String | The number of items to be returned. Cannot be more than 50 items. Use it only when the includeDetails is set to true.
};
apiInstance.v2getFeedItemStatus(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to &#39;SWAGGER_CHANNEL_TYPE&#39;]
 **WM_CONSUMER_ID** | **String**| Your Consumer ID | 
 **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to &#39;Auto populated&#39;]
 **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to &#39;Auto populated&#39;]
 **WM_SVC_NAME** | **String**| The Service name | [default to &#39;Walmart Marketplace&#39;]
 **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to &#39;123456abcdef&#39;]
 **feedId** | **String**| The feed ID. | [optional] 
 **includeDetails** | **String**| Includes the status details for each item in the feed. Do not set this parameter to true as discrepancies may appear between the header and the item details (the item details may be incorrect). Instead, use the Get a feedItems status. | [optional] [default to &#39;false&#39;]
 **offset** | **String**| The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true. | [optional] [default to &#39;0&#39;]
 **limit** | **String**| The number of items to be returned. Cannot be more than 50 items. Use it only when the includeDetails is set to true. | [optional] [default to &#39;50&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

