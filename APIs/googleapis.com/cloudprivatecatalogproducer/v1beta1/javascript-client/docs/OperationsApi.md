# CloudPrivateCatalogProducer.OperationsApi

All URIs are relative to *https://cloudprivatecatalogproducer.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudprivatecatalogproducerOperationsCancel**](OperationsApi.md#cloudprivatecatalogproducerOperationsCancel) | **POST** /v1beta1/{name}:cancel | 
[**cloudprivatecatalogproducerOperationsList**](OperationsApi.md#cloudprivatecatalogproducerOperationsList) | **GET** /v1beta1/operations | 



## cloudprivatecatalogproducerOperationsCancel

> Object cloudprivatecatalogproducerOperationsCancel(name, opts)



Starts asynchronous cancellation on a long-running operation.  The server makes a best effort to cancel the operation, but success is not guaranteed.  If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;.  Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.OperationsApi();
let name = "name_example"; // String | The name of the operation resource to be cancelled.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'body': {key: null} // Object | 
};
apiInstance.cloudprivatecatalogproducerOperationsCancel(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the operation resource to be cancelled. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerOperationsList

> GoogleLongrunningListOperationsResponse cloudprivatecatalogproducerOperationsList(opts)



Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.  NOTE: the &#x60;name&#x60; binding allows API services to override the binding to use different resource name schemes, such as &#x60;users/_*_/operations&#x60;. To override the binding, API services can add a binding such as &#x60;\&quot;/v1/{name&#x3D;users/_*}/operations\&quot;&#x60; to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.OperationsApi();
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'filter': "filter_example", // String | The standard list filter.
  'name': "name_example", // String | The name of the operation's parent resource.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example" // String | The standard list page token.
};
apiInstance.cloudprivatecatalogproducerOperationsList(opts, (error, data, response) => {
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
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **name** | **String**| The name of the operation&#39;s parent resource. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

