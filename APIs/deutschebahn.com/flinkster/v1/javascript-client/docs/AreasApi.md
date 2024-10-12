# FlinksterApiNg.AreasApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArea**](AreasApi.md#getArea) | **GET** /areas/{areaUID} | Get area by UID.
[**listAreas**](AreasApi.md#listAreas) | **GET** /areas | List Areas by Criteria.



## getArea

> AreaJO getArea(areaUID, opts)

Get area by UID.

Search for a specific area by UID.

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.AreasApi();
let areaUID = "areaUID_example"; // String | The Area UID 
let opts = {
  'expand': "expand_example" // String | Expand Provider
};
apiInstance.getArea(areaUID, opts, (error, data, response) => {
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
 **areaUID** | **String**| The Area UID  | 
 **expand** | **String**| Expand Provider | [optional] 

### Return type

[**AreaJO**](AreaJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAreas

> AreaJO listAreas(opts)

List Areas by Criteria.

Search for areas (locations of rental objects) by criteria.

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.AreasApi();
let opts = {
  'lat': 3.4, // Number | 
  'lon': 3.4, // Number | 
  'radius': 56, // Number | 
  'offset': 56, // Number | 
  'limit': 56, // Number | 
  'expand': "expand_example", // String | 
  'type': "type_example", // String | 
  'provider': "provider_example", // String | 
  'providernetwork': "providernetwork_example" // String | 
};
apiInstance.listAreas(opts, (error, data, response) => {
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
 **lon** | **Number**|  | [optional] 
 **radius** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **expand** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **provider** | **String**|  | [optional] 
 **providernetwork** | **String**|  | [optional] 

### Return type

[**AreaJO**](AreaJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

