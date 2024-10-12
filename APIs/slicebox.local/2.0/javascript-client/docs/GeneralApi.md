# SliceboxApi.GeneralApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destinationsGet**](GeneralApi.md#destinationsGet) | **GET** /destinations | 
[**sourcesGet**](GeneralApi.md#sourcesGet) | **GET** /sources | 
[**systemHealthGet**](GeneralApi.md#systemHealthGet) | **GET** /system/health | 
[**systemStopPost**](GeneralApi.md#systemStopPost) | **POST** /system/stop | 



## destinationsGet

> [Destination] destinationsGet()



Returns a list of currently available destinations. Possible destinations are box - sending data to a remote box, and scu - sending data a receiving SCP.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.GeneralApi();
apiInstance.destinationsGet((error, data, response) => {
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

[**[Destination]**](Destination.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## sourcesGet

> [Source] sourcesGet()



Returns a list of currently available data sources. Possible source types are user - data imported by an API call by a user, box - data received from a remote box, directory - data imported via a watched directory, import - data imported into slicebox using import sessions, or scp - data received from a PACS.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.GeneralApi();
apiInstance.sourcesGet((error, data, response) => {
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

[**[Source]**](Source.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## systemHealthGet

> systemHealthGet()



No-op route for checking whether the service is alive or not

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.GeneralApi();
apiInstance.systemHealthGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## systemStopPost

> systemStopPost()



stop and shut down slicebox

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.GeneralApi();
apiInstance.systemStopPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

