# InstanceMetadataClient.GetMetadataInformationApi

All URIs are relative to *http://169.254.169.254/metadata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identityGetInfo**](GetMetadataInformationApi.md#identityGetInfo) | **GET** /identity/info | 



## identityGetInfo

> IdentityInfoResponse identityGetInfo(metadata, apiVersion)



Get information about AAD Metadata

### Example

```javascript
import InstanceMetadataClient from 'instance_metadata_client';

let apiInstance = new InstanceMetadataClient.GetMetadataInformationApi();
let metadata = "metadata_example"; // String | This must be set to 'true'.
let apiVersion = "apiVersion_example"; // String | This is the API version to use.
apiInstance.identityGetInfo(metadata, apiVersion, (error, data, response) => {
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
 **metadata** | **String**| This must be set to &#39;true&#39;. | 
 **apiVersion** | **String**| This is the API version to use. | 

### Return type

[**IdentityInfoResponse**](IdentityInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

