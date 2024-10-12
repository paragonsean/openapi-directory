# AgcoApi.GlobalImageCategoriesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalImageCategoriesGetFile**](GlobalImageCategoriesApi.md#globalImageCategoriesGetFile) | **GET** /api/v2/GlobalImageCategories/{ID} | Gets a file&#39;s metadata.
[**globalImageCategoriesGetFiles**](GlobalImageCategoriesApi.md#globalImageCategoriesGetFiles) | **GET** /api/v2/GlobalImageCategories | Get a paged response of file metadata.
[**globalImageCategoriesPostFile**](GlobalImageCategoriesApi.md#globalImageCategoriesPostFile) | **POST** /api/v2/GlobalImageCategories | Create the metadata for a file before uploading. The State should be &#39;Created&#39;.



## globalImageCategoriesGetFile

> GlobalResourcesSharedModelsGlobalImageCategory globalImageCategoriesGetFile(ID)

Gets a file&#39;s metadata.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImageCategoriesApi();
let ID = "ID_example"; // String | The file's id.
apiInstance.globalImageCategoriesGetFile(ID, (error, data, response) => {
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
 **ID** | **String**| The file&#39;s id. | 

### Return type

[**GlobalResourcesSharedModelsGlobalImageCategory**](GlobalResourcesSharedModelsGlobalImageCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImageCategoriesGetFiles

> APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory globalImageCategoriesGetFiles(opts)

Get a paged response of file metadata.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImageCategoriesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.globalImageCategoriesGetFiles(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory**](APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## globalImageCategoriesPostFile

> String globalImageCategoriesPostFile(globalResourcesSharedModelsGlobalImageCategory)

Create the metadata for a file before uploading. The State should be &#39;Created&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.GlobalImageCategoriesApi();
let globalResourcesSharedModelsGlobalImageCategory = new AgcoApi.GlobalResourcesSharedModelsGlobalImageCategory(); // GlobalResourcesSharedModelsGlobalImageCategory | The file's metadata.
apiInstance.globalImageCategoriesPostFile(globalResourcesSharedModelsGlobalImageCategory, (error, data, response) => {
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
 **globalResourcesSharedModelsGlobalImageCategory** | [**GlobalResourcesSharedModelsGlobalImageCategory**](GlobalResourcesSharedModelsGlobalImageCategory.md)| The file&#39;s metadata. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

