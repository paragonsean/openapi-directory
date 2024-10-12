# InstanceMetadataClient.DefaultApi

All URIs are relative to *https://169.254.169.254/metadata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attestedGetDocument**](DefaultApi.md#attestedGetDocument) | **GET** /attested/document | 
[**instancesGetMetadata**](DefaultApi.md#instancesGetMetadata) | **GET** /instance | 



## attestedGetDocument

> AttestedData attestedGetDocument(apiVersion, metadata, opts)



Get Attested Data for the Virtual Machine.

### Example

```javascript
import InstanceMetadataClient from 'instance_metadata_client';
let defaultClient = InstanceMetadataClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstanceMetadataClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | This is the API version to use.
let metadata = "metadata_example"; // String | This must be set to 'true'.
let opts = {
  'nonce': "nonce_example" // String | This is a string of up to 32 random alphanumeric characters.
};
apiInstance.attestedGetDocument(apiVersion, metadata, opts, (error, data, response) => {
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
 **apiVersion** | **String**| This is the API version to use. | 
 **metadata** | **String**| This must be set to &#39;true&#39;. | 
 **nonce** | **String**| This is a string of up to 32 random alphanumeric characters. | [optional] 

### Return type

[**AttestedData**](AttestedData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## instancesGetMetadata

> Instance instancesGetMetadata(apiVersion, metadata)



Get Instance Metadata for the Virtual Machine.

### Example

```javascript
import InstanceMetadataClient from 'instance_metadata_client';
let defaultClient = InstanceMetadataClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstanceMetadataClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | This is the API version to use.
let metadata = "metadata_example"; // String | This must be set to 'true'.
apiInstance.instancesGetMetadata(apiVersion, metadata, (error, data, response) => {
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
 **apiVersion** | **String**| This is the API version to use. | 
 **metadata** | **String**| This must be set to &#39;true&#39;. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

