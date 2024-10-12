# AgcoApi.ContentSubmissionTypesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentSubmissionTypesDeleteContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesDeleteContentSubmissionType) | **DELETE** /api/v2/ContentSubmissionTypes/{id} | Remove a Content Submission Type
[**contentSubmissionTypesGetContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesGetContentSubmissionType) | **GET** /api/v2/ContentSubmissionTypes/{id} | Retrieves a Content Submission Type by its ID.
[**contentSubmissionTypesGetContentSubmissionTypes**](ContentSubmissionTypesApi.md#contentSubmissionTypesGetContentSubmissionTypes) | **GET** /api/v2/ContentSubmissionTypes | Returns available Content Submission Types.
[**contentSubmissionTypesPostContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesPostContentSubmissionType) | **POST** /api/v2/ContentSubmissionTypes | Add a Content Submission Type
[**contentSubmissionTypesPutContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesPutContentSubmissionType) | **PUT** /api/v2/ContentSubmissionTypes/{id} | Update a Content Submission Type



## contentSubmissionTypesDeleteContentSubmissionType

> contentSubmissionTypesDeleteContentSubmissionType(id)

Remove a Content Submission Type

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionTypesApi();
let id = 56; // Number | The ID of the Content Submission Type
apiInstance.contentSubmissionTypesDeleteContentSubmissionType(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Content Submission Type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSubmissionTypesGetContentSubmissionType

> ContentSubmissionSharedBusinessEntitiesContentSubmissionType contentSubmissionTypesGetContentSubmissionType(id)

Retrieves a Content Submission Type by its ID.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionTypesApi();
let id = 56; // Number | The ID of the Content Submission Type
apiInstance.contentSubmissionTypesGetContentSubmissionType(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Content Submission Type | 

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionTypesGetContentSubmissionTypes

> [ContentSubmissionSharedBusinessEntitiesContentSubmissionType] contentSubmissionTypesGetContentSubmissionTypes(opts)

Returns available Content Submission Types.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionTypesApi();
let opts = {
  'enabled': true // Boolean | 
};
apiInstance.contentSubmissionTypesGetContentSubmissionTypes(opts, (error, data, response) => {
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
 **enabled** | **Boolean**|  | [optional] 

### Return type

[**[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionTypesPostContentSubmissionType

> Number contentSubmissionTypesPostContentSubmissionType(contentSubmissionSharedBusinessEntitiesContentSubmissionType)

Add a Content Submission Type

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionTypesApi();
let contentSubmissionSharedBusinessEntitiesContentSubmissionType = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionType(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionType | The Content Submission Type
apiInstance.contentSubmissionTypesPostContentSubmissionType(contentSubmissionSharedBusinessEntitiesContentSubmissionType, (error, data, response) => {
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
 **contentSubmissionSharedBusinessEntitiesContentSubmissionType** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)| The Content Submission Type | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## contentSubmissionTypesPutContentSubmissionType

> contentSubmissionTypesPutContentSubmissionType(id, contentSubmissionSharedBusinessEntitiesContentSubmissionType)

Update a Content Submission Type

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ContentSubmissionTypesApi();
let id = 56; // Number | The ID of the Content Submission Type
let contentSubmissionSharedBusinessEntitiesContentSubmissionType = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmissionType(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionType | The Content Submission Type
apiInstance.contentSubmissionTypesPutContentSubmissionType(id, contentSubmissionSharedBusinessEntitiesContentSubmissionType, (error, data, response) => {
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
 **id** | **Number**| The ID of the Content Submission Type | 
 **contentSubmissionSharedBusinessEntitiesContentSubmissionType** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)| The Content Submission Type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

