# ColorNameApi.DefaultApi

All URIs are relative to *https://api.color.pizza/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listsGet**](DefaultApi.md#listsGet) | **GET** /lists/ | Get all colors of the default color name list
[**namesGet**](DefaultApi.md#namesGet) | **GET** /names/ | Get all colors of the default color name list
[**rootGet**](DefaultApi.md#rootGet) | **GET** / | Get all colors of the default color name list
[**swatchGet**](DefaultApi.md#swatchGet) | **GET** /swatch/ | Generate a color swatch for any color



## listsGet

> ListsGet200Response listsGet()

Get all colors of the default color name list

### Example

```javascript
import ColorNameApi from 'color_name_api';

let apiInstance = new ColorNameApi.DefaultApi();
apiInstance.listsGet((error, data, response) => {
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

[**ListsGet200Response**](ListsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## namesGet

> Get200Response namesGet(name, opts)

Get all colors of the default color name list

### Example

```javascript
import ColorNameApi from 'color_name_api';

let apiInstance = new ColorNameApi.DefaultApi();
let name = "name_example"; // String | The name of the color to retrieve (min 3 characters)
let opts = {
  'list': new ColorNameApi.PossibleLists() // PossibleLists | The name of the color name list to use
};
apiInstance.namesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the color to retrieve (min 3 characters) | 
 **list** | [**PossibleLists**](.md)| The name of the color name list to use | [optional] 

### Return type

[**Get200Response**](Get200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rootGet

> Get200Response rootGet(opts)

Get all colors of the default color name list

### Example

```javascript
import ColorNameApi from 'color_name_api';

let apiInstance = new ColorNameApi.DefaultApi();
let opts = {
  'list': new ColorNameApi.PossibleLists(), // PossibleLists | The name of the color name list to use
  'values': "values_example", // String | The hex values of the colors to retrieve without '#'
  'noduplicates': true // Boolean | Allow duplicate names or not
};
apiInstance.rootGet(opts, (error, data, response) => {
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
 **list** | [**PossibleLists**](.md)| The name of the color name list to use | [optional] 
 **values** | **String**| The hex values of the colors to retrieve without &#39;#&#39; | [optional] 
 **noduplicates** | **Boolean**| Allow duplicate names or not | [optional] 

### Return type

[**Get200Response**](Get200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## swatchGet

> String swatchGet(color, opts)

Generate a color swatch for any color

### Example

```javascript
import ColorNameApi from 'color_name_api';

let apiInstance = new ColorNameApi.DefaultApi();
let color = "color_example"; // String | The hex value of the color to retrieve without '#'
let opts = {
  'name': "name_example" // String | The name of the color
};
apiInstance.swatchGet(color, opts, (error, data, response) => {
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
 **color** | **String**| The hex value of the color to retrieve without &#39;#&#39; | 
 **name** | **String**| The name of the color | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, application/json

