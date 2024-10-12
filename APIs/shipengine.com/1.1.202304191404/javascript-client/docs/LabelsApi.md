# ShipEngineApi.LabelsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLabel**](LabelsApi.md#createLabel) | **POST** /v1/labels | Purchase Label
[**createLabelFromRate**](LabelsApi.md#createLabelFromRate) | **POST** /v1/labels/rates/{rate_id} | Purchase Label with Rate ID
[**createLabelFromShipment**](LabelsApi.md#createLabelFromShipment) | **POST** /v1/labels/shipment/{shipment_id} | Purchase Label with Shipment ID
[**createReturnLabel**](LabelsApi.md#createReturnLabel) | **POST** /v1/labels/{label_id}/return | Create a return label
[**getLabelByExternalShipmentId**](LabelsApi.md#getLabelByExternalShipmentId) | **GET** /v1/labels/external_shipment_id/{external_shipment_id} | Get Label By External Shipment ID
[**getLabelById**](LabelsApi.md#getLabelById) | **GET** /v1/labels/{label_id} | Get Label By ID
[**getTrackingLogFromLabel**](LabelsApi.md#getTrackingLogFromLabel) | **GET** /v1/labels/{label_id}/track | Get Label Tracking Information
[**listLabels**](LabelsApi.md#listLabels) | **GET** /v1/labels | List labels
[**voidLabel**](LabelsApi.md#voidLabel) | **PUT** /v1/labels/{label_id}/void | Void a Label By ID



## createLabel

> CreateLabelResponseBody createLabel(createLabelRequestBody)

Purchase Label

Purchase and print a label for shipment

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let createLabelRequestBody = new ShipEngineApi.CreateLabelRequestBody(); // CreateLabelRequestBody | 
apiInstance.createLabel(createLabelRequestBody, (error, data, response) => {
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
 **createLabelRequestBody** | [**CreateLabelRequestBody**](CreateLabelRequestBody.md)|  | 

### Return type

[**CreateLabelResponseBody**](CreateLabelResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLabelFromRate

> CreateLabelFromRateResponseBody createLabelFromRate(rateId, createLabelFromRateRequestBody)

Purchase Label with Rate ID

When retrieving rates for shipments using the &#x60;/rates&#x60; endpoint, the returned information contains a &#x60;rate_id&#x60; property that can be used to generate a label without having to refill in the shipment information repeatedly. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let rateId = "rateId_example"; // String | Rate ID
let createLabelFromRateRequestBody = new ShipEngineApi.CreateLabelFromRateRequestBody(); // CreateLabelFromRateRequestBody | 
apiInstance.createLabelFromRate(rateId, createLabelFromRateRequestBody, (error, data, response) => {
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
 **rateId** | **String**| Rate ID | 
 **createLabelFromRateRequestBody** | [**CreateLabelFromRateRequestBody**](CreateLabelFromRateRequestBody.md)|  | 

### Return type

[**CreateLabelFromRateResponseBody**](CreateLabelFromRateResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLabelFromShipment

> CreateLabelFromShipmentResponseBody createLabelFromShipment(shipmentId, createLabelFromShipmentRequestBody)

Purchase Label with Shipment ID

Purchase a label using a shipment ID that has already been created with the desired address and package info. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
let createLabelFromShipmentRequestBody = new ShipEngineApi.CreateLabelFromShipmentRequestBody(); // CreateLabelFromShipmentRequestBody | 
apiInstance.createLabelFromShipment(shipmentId, createLabelFromShipmentRequestBody, (error, data, response) => {
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
 **shipmentId** | **String**| Shipment ID | 
 **createLabelFromShipmentRequestBody** | [**CreateLabelFromShipmentRequestBody**](CreateLabelFromShipmentRequestBody.md)|  | 

### Return type

[**CreateLabelFromShipmentResponseBody**](CreateLabelFromShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReturnLabel

> CreateReturnLabelResponseBody createReturnLabel(labelId, createReturnLabelRequestBody)

Create a return label

Create a return label

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let labelId = "labelId_example"; // String | Label ID
let createReturnLabelRequestBody = new ShipEngineApi.CreateReturnLabelRequestBody(); // CreateReturnLabelRequestBody | 
apiInstance.createReturnLabel(labelId, createReturnLabelRequestBody, (error, data, response) => {
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
 **labelId** | **String**| Label ID | 
 **createReturnLabelRequestBody** | [**CreateReturnLabelRequestBody**](CreateReturnLabelRequestBody.md)|  | 

### Return type

[**CreateReturnLabelResponseBody**](CreateReturnLabelResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLabelByExternalShipmentId

> GetLabelByExternalShipmentIdResponseBody getLabelByExternalShipmentId(externalShipmentId, opts)

Get Label By External Shipment ID

Find a label by using the external shipment id that was used during label creation 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let externalShipmentId = "0bcb569d-1727-4ff9-ab49-b2fec0cee5ae"; // String | 
let opts = {
  'labelDownloadType': new ShipEngineApi.LabelDownloadType() // LabelDownloadType | 
};
apiInstance.getLabelByExternalShipmentId(externalShipmentId, opts, (error, data, response) => {
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
 **externalShipmentId** | **String**|  | 
 **labelDownloadType** | [**LabelDownloadType**](.md)|  | [optional] 

### Return type

[**GetLabelByExternalShipmentIdResponseBody**](GetLabelByExternalShipmentIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLabelById

> GetLabelByIdResponseBody getLabelById(labelId, opts)

Get Label By ID

Retrieve information for individual labels.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let labelId = "labelId_example"; // String | Label ID
let opts = {
  'labelDownloadType': new ShipEngineApi.LabelDownloadType() // LabelDownloadType | 
};
apiInstance.getLabelById(labelId, opts, (error, data, response) => {
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
 **labelId** | **String**| Label ID | 
 **labelDownloadType** | [**LabelDownloadType**](.md)|  | [optional] 

### Return type

[**GetLabelByIdResponseBody**](GetLabelByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackingLogFromLabel

> GetTrackingLogFromLabelResponseBody getTrackingLogFromLabel(labelId)

Get Label Tracking Information

Retrieve the label&#39;s tracking information

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let labelId = "labelId_example"; // String | Label ID
apiInstance.getTrackingLogFromLabel(labelId, (error, data, response) => {
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
 **labelId** | **String**| Label ID | 

### Return type

[**GetTrackingLogFromLabelResponseBody**](GetTrackingLogFromLabelResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLabels

> ListLabelsResponseBody listLabels(opts)

List labels

This endpoint returns a list of labels that you&#39;ve [created](https://www.shipengine.com/docs/labels/create-a-label/). You can optionally filter the results as well as control their sort order and the number of results returned at a time.  By default, all labels are returned, 25 at a time, starting with the most recently created ones.  You can combine multiple filter options to narrow-down the results.  For example, if you only want to get your UPS labels for your east coast warehouse you could query by both &#x60;warehouse_id&#x60; and &#x60;carrier_id&#x60; 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let opts = {
  'labelStatus': new ShipEngineApi.LabelStatus(), // LabelStatus | Only return labels that are currently in the specified status
  'serviceCode': "usps_first_class_mail", // String | Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/)
  'carrierId': "carrierId_example", // String | Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/)
  'trackingNumber': "9405511899223197428490", // String | Only return labels with a specific tracking number
  'batchId': "batchId_example", // String | Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/)
  'rateId': "rateId_example", // String | Rate ID
  'shipmentId': "shipmentId_example", // String | Shipment ID
  'warehouseId': "warehouseId_example", // String | Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/)
  'createdAtStart': new Date("2019-03-12T19:24:13.657Z"), // Date | Only return labels that were created on or after a specific date/time
  'createdAtEnd': new Date("2019-03-12T19:24:13.657Z"), // Date | Only return labels that were created on or before a specific date/time
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pageSize': 50, // Number | The number of results to return per response.
  'sortDir': new ShipEngineApi.SortDir(), // SortDir | Controls the sort order of the query.
  'sortBy': "'created_at'" // String | Controls which field the query is sorted by.
};
apiInstance.listLabels(opts, (error, data, response) => {
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
 **labelStatus** | [**LabelStatus**](.md)| Only return labels that are currently in the specified status | [optional] 
 **serviceCode** | **String**| Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) | [optional] 
 **carrierId** | **String**| Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/) | [optional] 
 **trackingNumber** | **String**| Only return labels with a specific tracking number | [optional] 
 **batchId** | **String**| Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/) | [optional] 
 **rateId** | **String**| Rate ID | [optional] 
 **shipmentId** | **String**| Shipment ID | [optional] 
 **warehouseId** | **String**| Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) | [optional] 
 **createdAtStart** | **Date**| Only return labels that were created on or after a specific date/time | [optional] 
 **createdAtEnd** | **Date**| Only return labels that were created on or before a specific date/time | [optional] 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per response. | [optional] [default to 25]
 **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] 
 **sortBy** | **String**| Controls which field the query is sorted by. | [optional] [default to &#39;created_at&#39;]

### Return type

[**ListLabelsResponseBody**](ListLabelsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## voidLabel

> VoidLabelResponseBody voidLabel(labelId)

Void a Label By ID

Void a label by ID to get a refund.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.LabelsApi();
let labelId = "labelId_example"; // String | Label ID
apiInstance.voidLabel(labelId, (error, data, response) => {
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
 **labelId** | **String**| Label ID | 

### Return type

[**VoidLabelResponseBody**](VoidLabelResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

