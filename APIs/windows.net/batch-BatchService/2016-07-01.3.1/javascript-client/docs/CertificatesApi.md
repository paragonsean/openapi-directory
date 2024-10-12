# BatchService.CertificatesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateAdd**](CertificatesApi.md#certificateAdd) | **POST** /certificates | Adds a certificate to the specified account.
[**certificateCancelDeletion**](CertificatesApi.md#certificateCancelDeletion) | **POST** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint})/canceldelete | Cancels a failed deletion of a certificate from the specified account.
[**certificateDelete**](CertificatesApi.md#certificateDelete) | **DELETE** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) | Deletes a certificate from the specified account.
[**certificateGet**](CertificatesApi.md#certificateGet) | **GET** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) | 
[**certificateList**](CertificatesApi.md#certificateList) | **GET** /certificates | Lists all of the certificates that have been added to the specified account.



## certificateAdd

> certificateAdd(apiVersion, certificate, opts)

Adds a certificate to the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let certificate = new BatchService.CertificateAddParameter(); // CertificateAddParameter | The certificate to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.certificateAdd(apiVersion, certificate, opts, (error, data, response) => {
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
 **certificate** | [**CertificateAddParameter**](CertificateAddParameter.md)| The certificate to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
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

If you try to delete a certificate that is being used by a pool or compute node, the status of the certificate changes to deletefailed. If you decide that you want to continue using the certificate, you can use this operation to set the status of the certificate back to active. If you intend to delete the certificate, you do not need to run this operation after the deletion failed. You must make sure that the certificate is not being used by any resources, and then you can try again to delete the certificate.

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
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
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
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
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

You cannot delete a certificate if a resource (pool or compute node) is using it. Before you can delete a certificate, you must therefore make sure that the certificate is not associated with any existing pools, the certificate is not installed on any compute nodes (even if you remove a certificate from a pool, it is not removed from existing compute nodes in that pool until they restart), and no running tasks depend on the certificate. If you try to delete a certificate that is in use, the deletion fails. The certificate status changes to deletefailed. You can use Cancel Delete Certificate to set the status back to active if you decide that you want to continue using the certificate.

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
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
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
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
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
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
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
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
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
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 certificates can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
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
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 certificates can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

