# NeoWsNearEarthObjectWebService.NeoApi

All URIs are relative to *http://www.neowsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browseNearEarthObjects**](NeoApi.md#browseNearEarthObjects) | **GET** /rest/v1/neo/browse | Browse the Near Earth Objects service
[**retrieveNearEarthObjectById**](NeoApi.md#retrieveNearEarthObjectById) | **GET** /rest/v1/neo/{asteroid_id} | Find Near Earth Objects by id



## browseNearEarthObjects

> NearEarthObject browseNearEarthObjects(opts)

Browse the Near Earth Objects service

Retieve a paginated list of Near Earth Objects

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.NeoApi();
let opts = {
  'page': 0, // Number | page
  'size': 20 // Number | size
};
apiInstance.browseNearEarthObjects(opts, (error, data, response) => {
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
 **page** | **Number**| page | [optional] [default to 0]
 **size** | **Number**| size | [optional] [default to 20]

### Return type

[**NearEarthObject**](NearEarthObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveNearEarthObjectById

> NearEarthObject retrieveNearEarthObjectById(asteroidId)

Find Near Earth Objects by id

Retrieve a Near Earth Objects with a given id

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.NeoApi();
let asteroidId = "asteroidId_example"; // String | ID of Near Earth Object - (ex: 3729835)
apiInstance.retrieveNearEarthObjectById(asteroidId, (error, data, response) => {
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
 **asteroidId** | **String**| ID of Near Earth Object - (ex: 3729835) | 

### Return type

[**NearEarthObject**](NearEarthObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

