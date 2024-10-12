# RadioMusicServices.CategoriesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List of categories
[**categoriesIdGet**](CategoriesApi.md#categoriesIdGet) | **GET** /categories/{id} | Category by ID



## categoriesGet

> CategoriesResponse categoriesGet(xAPIKey, opts)

List of categories

Retrieve Categories 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.CategoriesApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'kind': "kind_example" // String | Filter by provided query. E.g. 'promoted' returns promoted categories
};
apiInstance.categoriesGet(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **kind** | **String**| Filter by provided query. E.g. &#39;promoted&#39; returns promoted categories | [optional] 

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdGet

> CategoriesResponse categoriesIdGet(xAPIKey, id)

Category by ID

Retrieve Categories by ID 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.CategoriesApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let id = "id_example"; // String | Retrieve information about the category. E.g. 'sport-football-europeanchampionship'
apiInstance.categoriesIdGet(xAPIKey, id, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **id** | **String**| Retrieve information about the category. E.g. &#39;sport-football-europeanchampionship&#39; | 

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

