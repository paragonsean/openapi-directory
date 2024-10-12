# SmartMe.PicoLoadmanagementGroupApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPicoLoadmanagementgroupGet**](PicoLoadmanagementGroupApi.md#apiPicoLoadmanagementgroupGet) | **GET** /api/pico/loadmanagementgroup | GET: api/pico/loadmanagementgroup                            Returns all available load management groups
[**picoLoadmanagementGroupGet**](PicoLoadmanagementGroupApi.md#picoLoadmanagementGroupGet) | **GET** /api/pico/loadmanagementgroup/{id} | GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it&#39;s id



## apiPicoLoadmanagementgroupGet

> [PicoLoadmanagementGroupDto] apiPicoLoadmanagementgroupGet()

GET: api/pico/loadmanagementgroup                            Returns all available load management groups

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoLoadmanagementGroupApi();
apiInstance.apiPicoLoadmanagementgroupGet((error, data, response) => {
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

[**[PicoLoadmanagementGroupDto]**](PicoLoadmanagementGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## picoLoadmanagementGroupGet

> PicoLoadmanagementGroupDto picoLoadmanagementGroupGet(id)

GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it&#39;s id

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoLoadmanagementGroupApi();
let id = "id_example"; // String | 
apiInstance.picoLoadmanagementGroupGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**PicoLoadmanagementGroupDto**](PicoLoadmanagementGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

