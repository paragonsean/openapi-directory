# ApiV100.EstimationApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimationApiAll**](EstimationApi.md#estimationApiAll) | **GET** /api/estimation/all | Return all estimation for the account
[**estimationApiChangeStatus**](EstimationApi.md#estimationApiChangeStatus) | **POST** /api/estimation/changestatus | Change estimation status
[**estimationApiConvert**](EstimationApi.md#estimationApiConvert) | **POST** /api/estimation/convert | Convert the estimation to an invoice
[**estimationApiDelete**](EstimationApi.md#estimationApiDelete) | **POST** /api/estimation/delete | Delete an existing estimation
[**estimationApiDetails**](EstimationApi.md#estimationApiDetails) | **GET** /api/estimation/details | Return estimation data
[**estimationApiNew**](EstimationApi.md#estimationApiNew) | **POST** /api/estimation/new | Create an estimation
[**estimationApiSendToClient**](EstimationApi.md#estimationApiSendToClient) | **POST** /api/estimation/sendtoclient | Send the provided estimation to the client
[**estimationApiStatus**](EstimationApi.md#estimationApiStatus) | **GET** /api/estimation/status | Retrieve the status of the estimation
[**estimationApiUpdate**](EstimationApi.md#estimationApiUpdate) | **POST** /api/estimation/update | Update an existing estimation
[**estimationApiUri**](EstimationApi.md#estimationApiUri) | **GET** /api/estimation/uri | Return the unique url to the client&#39;s invoice



## estimationApiAll

> ListResultEstimationDetailsApiModel estimationApiAll(xAuthKey, xAuthSecret, opts)

Return all estimation for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.estimationApiAll(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**ListResultEstimationDetailsApiModel**](ListResultEstimationDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiChangeStatus

> Boolean estimationApiChangeStatus(xAuthKey, xAuthSecret, estimationChangeStatusApiModel)

Change estimation status

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let estimationChangeStatusApiModel = new ApiV100.EstimationChangeStatusApiModel(); // EstimationChangeStatusApiModel | 
apiInstance.estimationApiChangeStatus(xAuthKey, xAuthSecret, estimationChangeStatusApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **estimationChangeStatusApiModel** | [**EstimationChangeStatusApiModel**](EstimationChangeStatusApiModel.md)|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiConvert

> InvoiceFullDetailsApiModel estimationApiConvert(xAuthKey, xAuthSecret, body)

Convert the estimation to an invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let body = 56; // Number | 
apiInstance.estimationApiConvert(xAuthKey, xAuthSecret, body, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **body** | **Number**|  | 

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiDelete

> Number estimationApiDelete(xAuthKey, xAuthSecret, estimationDeleteApiModel)

Delete an existing estimation

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let estimationDeleteApiModel = new ApiV100.EstimationDeleteApiModel(); // EstimationDeleteApiModel | 
apiInstance.estimationApiDelete(xAuthKey, xAuthSecret, estimationDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **estimationDeleteApiModel** | [**EstimationDeleteApiModel**](EstimationDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiDetails

> EstimationFullDetailsApiModel estimationApiDetails(id, xAuthKey, xAuthSecret)

Return estimation data

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.estimationApiDetails(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiNew

> EstimationFullDetailsApiModel estimationApiNew(xAuthKey, xAuthSecret, estimationCreateApiModel)

Create an estimation

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let estimationCreateApiModel = new ApiV100.EstimationCreateApiModel(); // EstimationCreateApiModel | 
apiInstance.estimationApiNew(xAuthKey, xAuthSecret, estimationCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **estimationCreateApiModel** | [**EstimationCreateApiModel**](EstimationCreateApiModel.md)|  | 

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiSendToClient

> Number estimationApiSendToClient(xAuthKey, xAuthSecret, sendEstimationToClientApiModel)

Send the provided estimation to the client

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let sendEstimationToClientApiModel = new ApiV100.SendEstimationToClientApiModel(); // SendEstimationToClientApiModel | 
apiInstance.estimationApiSendToClient(xAuthKey, xAuthSecret, sendEstimationToClientApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **sendEstimationToClientApiModel** | [**SendEstimationToClientApiModel**](SendEstimationToClientApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiStatus

> String estimationApiStatus(id, xAuthKey, xAuthSecret)

Retrieve the status of the estimation

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.estimationApiStatus(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiUpdate

> EstimationFullDetailsApiModel estimationApiUpdate(xAuthKey, xAuthSecret, estimationUpdateApiModel)

Update an existing estimation

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let estimationUpdateApiModel = new ApiV100.EstimationUpdateApiModel(); // EstimationUpdateApiModel | 
apiInstance.estimationApiUpdate(xAuthKey, xAuthSecret, estimationUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **estimationUpdateApiModel** | [**EstimationUpdateApiModel**](EstimationUpdateApiModel.md)|  | 

### Return type

[**EstimationFullDetailsApiModel**](EstimationFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## estimationApiUri

> EstimationUriApiModel estimationApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.EstimationApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.estimationApiUri(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**EstimationUriApiModel**](EstimationUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

