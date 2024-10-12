# GeorgApi.GeorgApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoComplete**](GeorgApi.md#autoComplete) | **GET** /autocomplete | Search
[**getReverseGeoCode**](GeorgApi.md#getReverseGeoCode) | **GET** /reverse | Get reverse geocoding
[**search**](GeorgApi.md#search) | **GET** /search | Get geocoding
[**searchCoordinates**](GeorgApi.md#searchCoordinates) | **GET** /coordinates | Search coordinates in different formate
[**uploadFile**](GeorgApi.md#uploadFile) | **POST** /upload | Batch upload



## autoComplete

> String autoComplete(opts)

Search

Return search results in json

### Example

```javascript
import GeorgApi from 'georg_api';

let apiInstance = new GeorgApi.GeorgApi();
let opts = {
  'text': "text_example", // String | 
  'sources': "sources_example", // String | 
  'layers': "layers_example", // String | 
  'countryCode': "countryCode_example", // String | 
  'size': 56 // Number | 
};
apiInstance.autoComplete(opts, (error, data, response) => {
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
 **text** | **String**|  | [optional] 
 **sources** | **String**|  | [optional] 
 **layers** | **String**|  | [optional] 
 **countryCode** | **String**|  | [optional] 
 **size** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReverseGeoCode

> String getReverseGeoCode(opts)

Get reverse geocoding

Return search results in json

### Example

```javascript
import GeorgApi from 'georg_api';

let apiInstance = new GeorgApi.GeorgApi();
let opts = {
  'lat': 3.4, // Number | 
  'lng': 3.4 // Number | 
};
apiInstance.getReverseGeoCode(opts, (error, data, response) => {
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
 **lat** | **Number**|  | [optional] 
 **lng** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> String search(opts)

Get geocoding

Return search results in json

### Example

```javascript
import GeorgApi from 'georg_api';

let apiInstance = new GeorgApi.GeorgApi();
let opts = {
  'text': "text_example", // String | 
  'sources': "sources_example", // String | 
  'layers': "layers_example", // String | 
  'countryCode': "countryCode_example", // String | 
  'size': 56 // Number | 
};
apiInstance.search(opts, (error, data, response) => {
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
 **text** | **String**|  | [optional] 
 **sources** | **String**|  | [optional] 
 **layers** | **String**|  | [optional] 
 **countryCode** | **String**|  | [optional] 
 **size** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCoordinates

> String searchCoordinates(opts)

Search coordinates in different formate

Return search results in json

### Example

```javascript
import GeorgApi from 'georg_api';

let apiInstance = new GeorgApi.GeorgApi();
let opts = {
  'coordinates': "coordinates_example" // String | 
};
apiInstance.searchCoordinates(opts, (error, data, response) => {
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
 **coordinates** | **String**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadFile

> uploadFile(opts)

Batch upload

Upload csv file with minimum two columns (Id, SourceLocality). Return search results in json

### Example

```javascript
import GeorgApi from 'georg_api';

let apiInstance = new GeorgApi.GeorgApi();
let opts = {
  'type': "type_example", // String | 
  'formData': {key: new GeorgApi.InputPart()}, // {String: InputPart} | 
  'formDataMap': {key: null}, // {String: [InputPart]} | 
  'parts': [new GeorgApi.InputPart()], // [InputPart] | 
  'preamble': "preamble_example" // String | 
};
apiInstance.uploadFile(opts, (error, data, response) => {
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
 **type** | **String**|  | [optional] 
 **formData** | [**{String: InputPart}**](Object.md)|  | [optional] 
 **formDataMap** | [**{String: [InputPart]}**](Object.md)|  | [optional] 
 **parts** | [**[InputPart]**](InputPart.md)|  | [optional] 
 **preamble** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

