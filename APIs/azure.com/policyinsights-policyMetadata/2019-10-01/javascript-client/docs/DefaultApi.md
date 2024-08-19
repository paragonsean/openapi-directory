# PolicyMetadataClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyMetadataGetResource**](DefaultApi.md#policyMetadataGetResource) | **GET** /providers/Microsoft.PolicyInsights/policyMetadata/{resourceName} | 
[**policyMetadataList**](DefaultApi.md#policyMetadataList) | **GET** /providers/Microsoft.PolicyInsights/policyMetadata | 



## policyMetadataGetResource

> PolicyMetadata policyMetadataGetResource(resourceName, apiVersion)



Get policy metadata resource.

### Example

```javascript
import PolicyMetadataClient from 'policy_metadata_client';
let defaultClient = PolicyMetadataClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyMetadataClient.DefaultApi();
let resourceName = "resourceName_example"; // String | The name of the policy metadata resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.policyMetadataGetResource(resourceName, apiVersion, (error, data, response) => {
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
 **resourceName** | **String**| The name of the policy metadata resource. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PolicyMetadata**](PolicyMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyMetadataList

> PolicyMetadataCollection policyMetadataList(apiVersion, opts)



Get a list of the policy metadata resources.

### Example

```javascript
import PolicyMetadataClient from 'policy_metadata_client';
let defaultClient = PolicyMetadataClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyMetadataClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56 // Number | Maximum number of records to return.
};
apiInstance.policyMetadataList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 

### Return type

[**PolicyMetadataCollection**](PolicyMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

