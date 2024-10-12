# EveSwaggerInterface.RoutesApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRouteOriginDestination**](RoutesApi.md#getRouteOriginDestination) | **GET** /route/{origin}/{destination}/ | Get route



## getRouteOriginDestination

> [Number] getRouteOriginDestination(destination, origin, opts)

Get route

Get the systems between origin and destination  --- Alternate route: &#x60;/dev/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/legacy/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/v1/route/{origin}/{destination}/&#x60;  --- This route is cached for up to 86400 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.RoutesApi();
let destination = 56; // Number | destination solar system ID
let origin = 56; // Number | origin solar system ID
let opts = {
  'avoid': [null], // [Number] | avoid solar system ID(s)
  'connections': [null], // [[Number]] | connected solar system pairs
  'datasource': "'tranquility'", // String | The server name you would like data from
  'flag': "'shortest'", // String | route security preference
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getRouteOriginDestination(destination, origin, opts, (error, data, response) => {
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
 **destination** | **Number**| destination solar system ID | 
 **origin** | **Number**| origin solar system ID | 
 **avoid** | [**[Number]**](Number.md)| avoid solar system ID(s) | [optional] 
 **connections** | [**[[Number]]**]([Number].md)| connected solar system pairs | [optional] 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **flag** | **String**| route security preference | [optional] [default to &#39;shortest&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**[Number]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

