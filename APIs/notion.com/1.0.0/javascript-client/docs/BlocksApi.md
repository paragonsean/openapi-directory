# NotionApi.BlocksApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appendBlockChildren**](BlocksApi.md#appendBlockChildren) | **PATCH** /v1/blocks/{id}/children | Append block children
[**deleteABlock**](BlocksApi.md#deleteABlock) | **DELETE** /v1/blocks/{id} | Delete a block
[**retrieveABlock**](BlocksApi.md#retrieveABlock) | **GET** /v1/blocks/{id} | Retrieve a block
[**retrieveBlockChildren**](BlocksApi.md#retrieveBlockChildren) | **GET** /v1/blocks/{id}/children | Retrieve block children
[**updateABlock**](BlocksApi.md#updateABlock) | **PATCH** /v1/blocks/{id} | Update a block



## appendBlockChildren

> AppendBlockChildren200Response appendBlockChildren(id, opts)

Append block children

Append block children

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.BlocksApi();
let id = "{{PAGE_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  'appendBlockChildrenRequest': {"children":[{"heading_2":{"text":[{"text":{"content":"Lacinato kale"},"type":"text"}]},"object":"block","type":"heading_2"},{"object":"block","paragraph":{"rich_text":[{"text":{"content":"Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.","link":{"url":"https://en.wikipedia.org/wiki/Lacinato_kale"}},"type":"text"}]},"type":"paragraph"}]} // AppendBlockChildrenRequest | 
};
apiInstance.appendBlockChildren(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 
 **appendBlockChildrenRequest** | [**AppendBlockChildrenRequest**](AppendBlockChildrenRequest.md)|  | [optional] 

### Return type

[**AppendBlockChildren200Response**](AppendBlockChildren200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteABlock

> DeleteABlock200Response deleteABlock(id, opts)

Delete a block

Delete a block

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.BlocksApi();
let id = "{{BLOCK_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.deleteABlock(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 

### Return type

[**DeleteABlock200Response**](DeleteABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveABlock

> RetrieveABlock200Response retrieveABlock(id, opts)

Retrieve a block

Retrieve a block

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.BlocksApi();
let id = "{{BLOCK_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.retrieveABlock(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 

### Return type

[**RetrieveABlock200Response**](RetrieveABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveBlockChildren

> RetrieveBlockChildren200Response retrieveBlockChildren(id, opts)

Retrieve block children

Retrieve block children

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.BlocksApi();
let id = "{{PAGE_ID}}"; // String | 
let opts = {
  'pageSize': "100", // String | 
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.retrieveBlockChildren(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **pageSize** | **String**|  | [optional] 
 **notionVersion** | **String**|  | [optional] 

### Return type

[**RetrieveBlockChildren200Response**](RetrieveBlockChildren200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateABlock

> RetrieveABlock200Response updateABlock(id, opts)

Update a block

This endpoint allows you to update block content. [See Full Documentation](https://developers.notion.com/reference/update-a-block)

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.BlocksApi();
let id = "{{BLOCK_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  'updateABlockRequest': {"paragraph":{"rich_text":[{"text":{"content":"hello to you"},"type":"text"}]}} // UpdateABlockRequest | 
};
apiInstance.updateABlock(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 
 **updateABlockRequest** | [**UpdateABlockRequest**](UpdateABlockRequest.md)|  | [optional] 

### Return type

[**RetrieveABlock200Response**](RetrieveABlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

