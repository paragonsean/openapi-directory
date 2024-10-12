# BatchService.CertificatesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateAdd**](CertificatesApi.md#certificateAdd) | **POST** /certificates | 
[**certificateCancelDeletion**](CertificatesApi.md#certificateCancelDeletion) | **POST** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint})/canceldelete | 
[**certificateDelete**](CertificatesApi.md#certificateDelete) | **DELETE** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) | 
[**certificateGet**](CertificatesApi.md#certificateGet) | **GET** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) | 
[**certificateList**](CertificatesApi.md#certificateList) | **GET** /certificates | 



## certificateAdd

> certificateAdd(apiVersion, certificateAddParameter, opts)



Adds a certificate to the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let certificateAddParameter = new BatchService.CertificateAddParameter(); // CertificateAddParameter | The certificate to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateAdd(apiVersion, certificateAddParameter, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **certificateAddParameter** | [**CertificateAddParameter**](CertificateAddParameter.md)| The certificate to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## certificateCancelDeletion

> certificateCancelDeletion(thumbprintAlgorithm, thumbprint, apiVersion, opts)



Cancels a failed deletion of a certificate from the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
let thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate being deleted.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateCancelDeletion(thumbprintAlgorithm, thumbprint, apiVersion, opts, (error, data, response) => {
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
 **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | 
 **thumbprint** | **String**| The thumbprint of the certificate being deleted. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateDelete

> certificateDelete(thumbprintAlgorithm, thumbprint, apiVersion, opts)



Deletes a certificate from the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
let thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate to be deleted.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateDelete(thumbprintAlgorithm, thumbprint, apiVersion, opts, (error, data, response) => {
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
 **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | 
 **thumbprint** | **String**| The thumbprint of the certificate to be deleted. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateGet

> Certificate certificateGet(thumbprintAlgorithm, thumbprint, apiVersion, opts)



Gets information about the specified certificate.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
let thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate to get.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateGet(thumbprintAlgorithm, thumbprint, apiVersion, opts, (error, data, response) => {
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
 **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | 
 **thumbprint** | **String**| The thumbprint of the certificate to get. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateList

> CertificateListResult certificateList(apiVersion, opts)



Lists all of the certificates that have been added to the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'select': "select_example", // String | An OData $select clause.
  'maxresults': 56, // Number | The maximum number of items to return in the response.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Whether the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **select** | **String**| An OData $select clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

