# SliceboxApi.SCPsApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scpsGet**](SCPsApi.md#scpsGet) | **GET** /scps | 
[**scpsIdDelete**](SCPsApi.md#scpsIdDelete) | **DELETE** /scps/{id} | 
[**scpsPost**](SCPsApi.md#scpsPost) | **POST** /scps | 



## scpsGet

> [Scp] scpsGet(opts)



get a list of DICOM SCPs. Each SCP is a server for receiving DICOM images from e.g. a PACS system.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCPsApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of SCPs
  'count': 20 // Number | size of returned slice of SCPs
};
apiInstance.scpsGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of SCPs | [optional] [default to 0]
 **count** | **Number**| size of returned slice of SCPs | [optional] [default to 20]

### Return type

[**[Scp]**](Scp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## scpsIdDelete

> scpsIdDelete(id)



shut down and remove the SCP corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCPsApi();
let id = 789; // Number | id of SCP to remove
apiInstance.scpsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of SCP to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## scpsPost

> Scp scpsPost(opts)



add a new SCP for receiving DICOM images

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SCPsApi();
let opts = {
  'scp': new SliceboxApi.Scp() // Scp | SCP information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.scpsPost(opts, (error, data, response) => {
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
 **scp** | [**Scp**](Scp.md)| SCP information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Scp**](Scp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

