# SliceboxApi.SCUsApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scusGet**](SCUsApi.md#scusGet) | **GET** /scus | 
[**scusIdDelete**](SCUsApi.md#scusIdDelete) | **DELETE** /scus/{id} | 
[**scusIdSendPost**](SCUsApi.md#scusIdSendPost) | **POST** /scus/{id}/send | 
[**scusPost**](SCUsApi.md#scusPost) | **POST** /scus | 



## scusGet

> [Scu] scusGet(opts)



get a list of DICOM SCUs. Each SCU is a client for sending DICOM images to an SCP, e.g. a PACS system.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCUsApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of SCUs
  'count': 20 // Number | size of returned slice of SCUs
};
apiInstance.scusGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of SCUs | [optional] [default to 0]
 **count** | **Number**| size of returned slice of SCUs | [optional] [default to 20]

### Return type

[**[Scu]**](Scu.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## scusIdDelete

> scusIdDelete(id)



remove the SCU corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCUsApi();
let id = 789; // Number | id of SCU to remove
apiInstance.scusIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of SCU to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## scusIdSendPost

> scusIdSendPost(id, imageids)



send the images with the supplied image IDs to a DICOM SCP using the the SCU with the supplied scu ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCUsApi();
let id = 789; // Number | id of SCU to use for sending
let imageids = [null]; // [Number] | array of ids of images to send
apiInstance.scusIdSendPost(id, imageids, (error, data, response) => {
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
 **id** | **Number**| id of SCU to use for sending | 
 **imageids** | [**[Number]**](Number.md)| array of ids of images to send | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## scusPost

> Scu scusPost(opts)



add a new SCU for sending DICOM images

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCUsApi();
let opts = {
  'scu': new SliceboxApi.Scu() // Scu | SCU information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.scusPost(opts, (error, data, response) => {
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
 **scu** | [**Scu**](Scu.md)| SCU information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Scu**](Scu.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

