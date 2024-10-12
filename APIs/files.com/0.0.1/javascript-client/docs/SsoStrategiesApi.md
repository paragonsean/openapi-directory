# FilesComApi.SsoStrategiesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSsoStrategies**](SsoStrategiesApi.md#getSsoStrategies) | **GET** /sso_strategies | List Sso Strategies
[**getSsoStrategiesId**](SsoStrategiesApi.md#getSsoStrategiesId) | **GET** /sso_strategies/{id} | Show Sso Strategy
[**postSsoStrategiesIdSync**](SsoStrategiesApi.md#postSsoStrategiesIdSync) | **POST** /sso_strategies/{id}/sync | Synchronize provisioning data with the SSO remote server.



## getSsoStrategies

> [SsoStrategyEntity] getSsoStrategies(opts)

List Sso Strategies

List Sso Strategies

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SsoStrategiesApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getSsoStrategies(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[SsoStrategyEntity]**](SsoStrategyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSsoStrategiesId

> SsoStrategyEntity getSsoStrategiesId(id)

Show Sso Strategy

Show Sso Strategy

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SsoStrategiesApi();
let id = 56; // Number | Sso Strategy ID.
apiInstance.getSsoStrategiesId(id, (error, data, response) => {
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
 **id** | **Number**| Sso Strategy ID. | 

### Return type

[**SsoStrategyEntity**](SsoStrategyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postSsoStrategiesIdSync

> postSsoStrategiesIdSync(id)

Synchronize provisioning data with the SSO remote server.

Synchronize provisioning data with the SSO remote server.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SsoStrategiesApi();
let id = 56; // Number | Sso Strategy ID.
apiInstance.postSsoStrategiesIdSync(id, (error, data, response) => {
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
 **id** | **Number**| Sso Strategy ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

