# CredasApi.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addIdDocumentImage**](ImagesApi.md#addIdDocumentImage) | **POST** /api/images/id-document | Add an id document image to the specified registration.
[**addLivenessImage**](ImagesApi.md#addLivenessImage) | **POST** /api/images/liveness | Add a liveness image (UAP) to the specified registration.
[**addSelfieImage**](ImagesApi.md#addSelfieImage) | **POST** /api/images/selfie | Add a selfie image to the registration.
[**getIdDocumentImages**](ImagesApi.md#getIdDocumentImages) | **GET** /api/images/id-document/{registrationId} | Get all id document images associated with a registration.
[**getLivenessImage**](ImagesApi.md#getLivenessImage) | **GET** /api/images/liveness/{registrationId} | Retrieve the liveness action image (UAP) associated with a registration.
[**getLivenessPerformedImage**](ImagesApi.md#getLivenessPerformedImage) | **GET** /api/images/liveness-performed/{registrationId} | Retrieve the liveness performed image associated with a registration.
[**getScanReportPdf**](ImagesApi.md#getScanReportPdf) | **GET** /api/images/scan-report-pdf/{scanId} | Returns a detailed report on the analysis that has taken place of a scanned document
[**getSelfieImage**](ImagesApi.md#getSelfieImage) | **GET** /api/images/selfie/{registrationId} | Retrieve the selfie image associated with a registration.



## addIdDocumentImage

> CredasApiModelsImagesAddIdDocumentImageResponse addIdDocumentImage(apikey, opts)

Add an id document image to the specified registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsImagesAddIdDocumentImageRequest': new CredasApi.CredasApiModelsImagesAddIdDocumentImageRequest() // CredasApiModelsImagesAddIdDocumentImageRequest | Object containing the id document image and registration id.
};
apiInstance.addIdDocumentImage(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsImagesAddIdDocumentImageRequest** | [**CredasApiModelsImagesAddIdDocumentImageRequest**](CredasApiModelsImagesAddIdDocumentImageRequest.md)| Object containing the id document image and registration id. | [optional] 

### Return type

[**CredasApiModelsImagesAddIdDocumentImageResponse**](CredasApiModelsImagesAddIdDocumentImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## addLivenessImage

> addLivenessImage(apikey, opts)

Add a liveness image (UAP) to the specified registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsImagesAddLivenessImageRequest': new CredasApi.CredasApiModelsImagesAddLivenessImageRequest() // CredasApiModelsImagesAddLivenessImageRequest | Object containing the liveness image and registration id.
};
apiInstance.addLivenessImage(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsImagesAddLivenessImageRequest** | [**CredasApiModelsImagesAddLivenessImageRequest**](CredasApiModelsImagesAddLivenessImageRequest.md)| Object containing the liveness image and registration id. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## addSelfieImage

> CredasApiModelsImagesAddSelfieImageResponse addSelfieImage(apikey, opts)

Add a selfie image to the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsImagesAddSelfieImageRequest': new CredasApi.CredasApiModelsImagesAddSelfieImageRequest() // CredasApiModelsImagesAddSelfieImageRequest | Object containing the selfie image and registration id.
};
apiInstance.addSelfieImage(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsImagesAddSelfieImageRequest** | [**CredasApiModelsImagesAddSelfieImageRequest**](CredasApiModelsImagesAddSelfieImageRequest.md)| Object containing the selfie image and registration id. | [optional] 

### Return type

[**CredasApiModelsImagesAddSelfieImageResponse**](CredasApiModelsImagesAddSelfieImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## getIdDocumentImages

> [CredasApiModelsImagesGetIdDocumentImageResponse] getIdDocumentImages(registrationId, apikey)

Get all id document images associated with a registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let registrationId = "registrationId_example"; // String | The id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getIdDocumentImages(registrationId, apikey, (error, data, response) => {
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
 **registrationId** | **String**| The id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**[CredasApiModelsImagesGetIdDocumentImageResponse]**](CredasApiModelsImagesGetIdDocumentImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getLivenessImage

> CredasApiModelsImagesGetLivenessImageResponse getLivenessImage(registrationId, apikey)

Retrieve the liveness action image (UAP) associated with a registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let registrationId = "registrationId_example"; // String | The id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getLivenessImage(registrationId, apikey, (error, data, response) => {
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
 **registrationId** | **String**| The id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsImagesGetLivenessImageResponse**](CredasApiModelsImagesGetLivenessImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getLivenessPerformedImage

> CredasApiModelsImagesGetLivenessPerformedImageResponse getLivenessPerformedImage(registrationId, apikey)

Retrieve the liveness performed image associated with a registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let registrationId = "registrationId_example"; // String | The id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getLivenessPerformedImage(registrationId, apikey, (error, data, response) => {
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
 **registrationId** | **String**| The id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsImagesGetLivenessPerformedImageResponse**](CredasApiModelsImagesGetLivenessPerformedImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getScanReportPdf

> Blob getScanReportPdf(scanId, apikey)

Returns a detailed report on the analysis that has taken place of a scanned document

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let scanId = "scanId_example"; // String | Id of the individual scanned document
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getScanReportPdf(scanId, apikey, (error, data, response) => {
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
 **scanId** | **String**| Id of the individual scanned document | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getSelfieImage

> CredasApiModelsImagesGetSelfieImageResponse getSelfieImage(registrationId, apikey)

Retrieve the selfie image associated with a registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ImagesApi();
let registrationId = "registrationId_example"; // String | The id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getSelfieImage(registrationId, apikey, (error, data, response) => {
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
 **registrationId** | **String**| The id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsImagesGetSelfieImageResponse**](CredasApiModelsImagesGetSelfieImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

