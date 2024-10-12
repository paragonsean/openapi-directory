# SliceboxApi.DirectoriesApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directorywatchesGet**](DirectoriesApi.md#directorywatchesGet) | **GET** /directorywatches | 
[**directorywatchesIdDelete**](DirectoriesApi.md#directorywatchesIdDelete) | **DELETE** /directorywatches/{id} | 
[**directorywatchesPost**](DirectoriesApi.md#directorywatchesPost) | **POST** /directorywatches | 



## directorywatchesGet

> [WatchedDirectory] directorywatchesGet(opts)



get a list of watch directories. Each watch directory and its sub-directories are watched for incoming DICOM files, which are read and imported into slicebox.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.DirectoriesApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of watched directories
  'count': 20 // Number | size of returned slice of watched directories
};
apiInstance.directorywatchesGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of watched directories | [optional] [default to 0]
 **count** | **Number**| size of returned slice of watched directories | [optional] [default to 20]

### Return type

[**[WatchedDirectory]**](WatchedDirectory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## directorywatchesIdDelete

> directorywatchesIdDelete(id)



stop watching and remove the directory corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.DirectoriesApi();
let id = 789; // Number | id of directory to stop watching
apiInstance.directorywatchesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of directory to stop watching | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directorywatchesPost

> WatchedDirectory directorywatchesPost(opts)



add a new directory to watch for incoming DICOM files

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.DirectoriesApi();
let opts = {
  'watchedDirectory': new SliceboxApi.WatchedDirectory() // WatchedDirectory | directory to setup a watch for. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.directorywatchesPost(opts, (error, data, response) => {
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
 **watchedDirectory** | [**WatchedDirectory**](WatchedDirectory.md)| directory to setup a watch for. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**WatchedDirectory**](WatchedDirectory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

