# NotionApi.DatabasesApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryADatabase**](DatabasesApi.md#queryADatabase) | **POST** /v1/databases/{id}/query | Query a database
[**retrieveADatabase**](DatabasesApi.md#retrieveADatabase) | **GET** /v1/databases/{id} | Retrieve a database
[**updateADatabase**](DatabasesApi.md#updateADatabase) | **PATCH** /v1/databases/{id} | Update a database



## queryADatabase

> QueryADatabase200Response queryADatabase(id, opts)

Query a database

Query a database

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.DatabasesApi();
let id = "{{DATABASE_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  'queryADatabaseRequest': {"filter":{"property":"Status","select":{"equals":"Reading"}}} // QueryADatabaseRequest | 
};
apiInstance.queryADatabase(id, opts, (error, data, response) => {
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
 **queryADatabaseRequest** | [**QueryADatabaseRequest**](QueryADatabaseRequest.md)|  | [optional] 

### Return type

[**QueryADatabase200Response**](QueryADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveADatabase

> RetrieveADatabase200Response retrieveADatabase(id, opts)

Retrieve a database

Retrieves a database object using the ID specified in the request path. 

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.DatabasesApi();
let id = "id_example"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.retrieveADatabase(id, opts, (error, data, response) => {
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

[**RetrieveADatabase200Response**](RetrieveADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateADatabase

> UpdateADatabase200Response updateADatabase(id, opts)

Update a database

Update a database

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.DatabasesApi();
let id = "id_example"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  'updateADatabaseRequest': {"properties":{"Wine Pairing":{"rich_text":{}}},"title":[{"text":{"content":"Ever Better Reading List Title"}}]} // UpdateADatabaseRequest | 
};
apiInstance.updateADatabase(id, opts, (error, data, response) => {
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
 **updateADatabaseRequest** | [**UpdateADatabaseRequest**](UpdateADatabaseRequest.md)|  | [optional] 

### Return type

[**UpdateADatabase200Response**](UpdateADatabase200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

