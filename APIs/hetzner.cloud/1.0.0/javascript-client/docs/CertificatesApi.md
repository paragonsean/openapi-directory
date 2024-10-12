# HetznerCloudApi.CertificatesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificatesGet**](CertificatesApi.md#certificatesGet) | **GET** /certificates | Get all Certificates
[**certificatesIdDelete**](CertificatesApi.md#certificatesIdDelete) | **DELETE** /certificates/{id} | Delete a Certificate
[**certificatesIdGet**](CertificatesApi.md#certificatesIdGet) | **GET** /certificates/{id} | Get a Certificate
[**certificatesIdPut**](CertificatesApi.md#certificatesIdPut) | **PUT** /certificates/{id} | Update a Certificate
[**certificatesPost**](CertificatesApi.md#certificatesPost) | **POST** /certificates | Create a Certificate



## certificatesGet

> CertificatesResponse certificatesGet(opts)

Get all Certificates

Returns all Certificate objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificatesApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example", // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
  'type': "type_example" // String | Can be used multiple times. The response will only contain Certificates matching the type.
};
apiInstance.certificatesGet(opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 
 **type** | **String**| Can be used multiple times. The response will only contain Certificates matching the type. | [optional] 

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesIdDelete

> certificatesIdDelete(id)

Delete a Certificate

Deletes a Certificate.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificatesApi();
let id = 56; // Number | ID of the resource
apiInstance.certificatesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## certificatesIdGet

> CertificateResponse certificatesIdGet(id)

Get a Certificate

Gets a specific Certificate object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificatesApi();
let id = 56; // Number | ID of the resource
apiInstance.certificatesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesIdPut

> CertificateResponse certificatesIdPut(id, opts)

Update a Certificate

Updates the Certificate properties.  Note that when updating labels, the Certificate’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Certificate object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificatesApi();
let id = 56; // Number | ID of the resource
let opts = {
  'updateCertificateRequest': new HetznerCloudApi.UpdateCertificateRequest() // UpdateCertificateRequest | 
};
apiInstance.certificatesIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 
 **updateCertificateRequest** | [**UpdateCertificateRequest**](UpdateCertificateRequest.md)|  | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificatesPost

> CreateCertificateResponse certificatesPost(opts)

Create a Certificate

Creates a new Certificate.  The default type **uploaded** allows for uploading your existing &#x60;certificate&#x60; and &#x60;private_key&#x60; in PEM format. You have to monitor its expiration date and handle renewal yourself.  In contrast, type **managed** requests a new Certificate from *Let&#39;s Encrypt* for the specified &#x60;domain_names&#x60;. Only domains managed by *Hetzner DNS* are supported. We handle renewal and timely alert the project owner via email if problems occur.  For type &#x60;managed&#x60; Certificates the &#x60;action&#x60; key of the response contains the Action that allows for tracking the issuance process. For type &#x60;uploaded&#x60; Certificates the &#x60;action&#x60; is always null. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificatesApi();
let opts = {
  'createCertificateRequest': {"domain_names":["example.com","webmail.example.com","www.example.com"],"name":"my website cert","type":"managed"} // CreateCertificateRequest | 
};
apiInstance.certificatesPost(opts, (error, data, response) => {
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
 **createCertificateRequest** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | [optional] 

### Return type

[**CreateCertificateResponse**](CreateCertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

