# BbcIPlayerBusinessLayer.CategoriesApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategories**](CategoriesApi.md#getCategories) | **GET** /categories | Get categories
[**getSubCategories**](CategoriesApi.md#getSubCategories) | **GET** /categories/{category} | Get sub-categories



## getCategories

> Object getCategories(lang)

Get categories

Get the list of all the categories in TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.CategoriesApi();
let lang = "lang_example"; // String | The language for any applicable localised strings.
apiInstance.getCategories(lang, (error, data, response) => {
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
 **lang** | **String**| The language for any applicable localised strings. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubCategories

> Object getSubCategories(category, lang)

Get sub-categories

Get sub-categories

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.CategoriesApi();
let category = "category_example"; // String | The category identifier to return results from.
let lang = "lang_example"; // String | The language for any applicable localised strings.
apiInstance.getSubCategories(category, lang, (error, data, response) => {
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
 **category** | **String**| The category identifier to return results from. | 
 **lang** | **String**| The language for any applicable localised strings. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

