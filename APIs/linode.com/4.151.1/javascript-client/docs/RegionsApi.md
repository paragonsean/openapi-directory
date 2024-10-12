# LinodeApi.RegionsApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRegion**](RegionsApi.md#getRegion) | **GET** /regions/{regionId} | Region View
[**getRegions**](RegionsApi.md#getRegions) | **GET** /regions | Regions List



## getRegion

> Region getRegion(regionId)

Region View

Returns a single Region. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.RegionsApi();
let regionId = "regionId_example"; // String | ID of the Region to look up.
apiInstance.getRegion(regionId, (error, data, response) => {
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
 **regionId** | **String**| ID of the Region to look up. | 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegions

> GetRegions200Response getRegions()

Regions List

Lists the Regions available for Linode services. Not all services are guaranteed to be available in all Regions. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.RegionsApi();
apiInstance.getRegions((error, data, response) => {
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

[**GetRegions200Response**](GetRegions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

