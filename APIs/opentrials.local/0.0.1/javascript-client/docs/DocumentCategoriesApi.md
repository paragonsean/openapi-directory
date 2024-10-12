# OpenTrialsApi.DocumentCategoriesApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDocumentCategories**](DocumentCategoriesApi.md#listDocumentCategories) | **GET** /document_categories | 



## listDocumentCategories

> DocumentCategoryList listDocumentCategories()



Returns document categories

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.DocumentCategoriesApi();
apiInstance.listDocumentCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentCategoryList**](DocumentCategoryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

