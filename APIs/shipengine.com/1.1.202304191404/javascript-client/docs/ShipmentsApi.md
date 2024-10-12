# ShipEngineApi.ShipmentsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelShipments**](ShipmentsApi.md#cancelShipments) | **PUT** /v1/shipments/{shipment_id}/cancel | Cancel a Shipment
[**createShipments**](ShipmentsApi.md#createShipments) | **POST** /v1/shipments | Create Shipments
[**getShipmentByExternalId**](ShipmentsApi.md#getShipmentByExternalId) | **GET** /v1/shipments/external_shipment_id/{external_shipment_id} | Get Shipment By External ID
[**getShipmentById**](ShipmentsApi.md#getShipmentById) | **GET** /v1/shipments/{shipment_id} | Get Shipment By ID
[**listShipmentRates**](ShipmentsApi.md#listShipmentRates) | **GET** /v1/shipments/{shipment_id}/rates | Get Shipment Rates
[**listShipments**](ShipmentsApi.md#listShipments) | **GET** /v1/shipments | List Shipments
[**parseShipment**](ShipmentsApi.md#parseShipment) | **PUT** /v1/shipments/recognize | Parse shipping info
[**tagShipment**](ShipmentsApi.md#tagShipment) | **POST** /v1/shipments/{shipment_id}/tags/{tag_name} | Add Tag to Shipment
[**untagShipment**](ShipmentsApi.md#untagShipment) | **DELETE** /v1/shipments/{shipment_id}/tags/{tag_name} | Remove Tag from Shipment
[**updateShipment**](ShipmentsApi.md#updateShipment) | **PUT** /v1/shipments/{shipment_id} | Update Shipment By ID



## cancelShipments

> String cancelShipments(shipmentId)

Cancel a Shipment

Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first An example use case would be if a batch label creation job is going to run at a set time and only queries &#x60;pending&#x60; shipments. Marking a shipment as cancelled would remove it from this process 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
apiInstance.cancelShipments(shipmentId, (error, data, response) => {
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

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## createShipments

> CreateShipmentsResponseBody createShipments(createShipmentsRequestBody)

Create Shipments

Create one or multiple shipments.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let createShipmentsRequestBody = new ShipEngineApi.CreateShipmentsRequestBody(); // CreateShipmentsRequestBody | 
apiInstance.createShipments(createShipmentsRequestBody, (error, data, response) => {
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
 **createShipmentsRequestBody** | [**CreateShipmentsRequestBody**](CreateShipmentsRequestBody.md)|  | 

### Return type

[**CreateShipmentsResponseBody**](CreateShipmentsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getShipmentByExternalId

> GetShipmentByExternalIdResponseBody getShipmentByExternalId(externalShipmentId)

Get Shipment By External ID

Query Shipments created using your own custom ID convention using this endpint

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let externalShipmentId = "0bcb569d-1727-4ff9-ab49-b2fec0cee5ae"; // String | 
apiInstance.getShipmentByExternalId(externalShipmentId, (error, data, response) => {
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

### Return type

[**GetShipmentByExternalIdResponseBody**](GetShipmentByExternalIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShipmentById

> GetShipmentByIdResponseBody getShipmentById(shipmentId)

Get Shipment By ID

Get an individual shipment based on its ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
apiInstance.getShipmentById(shipmentId, (error, data, response) => {
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

### Return type

[**GetShipmentByIdResponseBody**](GetShipmentByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShipmentRates

> ListShipmentRatesResponseBody listShipmentRates(shipmentId, opts)

Get Shipment Rates

Get Rates for the shipment information associated with the shipment ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
let opts = {
  'createdAtStart': new Date("2019-03-12T19:24:13.657Z") // Date | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
};
apiInstance.listShipmentRates(shipmentId, opts, (error, data, response) => {
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
 **createdAtStart** | **Date**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] 

### Return type

[**ListShipmentRatesResponseBody**](ListShipmentRatesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShipments

> ListShipmentsResponseBody listShipments(opts)

List Shipments

Get list of Shipments

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let opts = {
  'shipmentStatus': new ShipEngineApi.ShipmentStatus(), // ShipmentStatus | 
  'batchId': "batchId_example", // String | Batch ID
  'tag': "Letters_to_santa", // String | Search for shipments based on the custom tag added to the shipment object
  'createdAtStart': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
  'createdAtEnd': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
  'modifiedAtStart': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time)
  'modifiedAtEnd': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time)
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pageSize': 50, // Number | The number of results to return per response.
  'salesOrderId': "salesOrderId_example", // String | Sales Order ID
  'sortDir': new ShipEngineApi.SortDir(), // SortDir | Controls the sort order of the query.
  'sortBy': new ShipEngineApi.ShipmentsSortBy() // ShipmentsSortBy | 
};
apiInstance.listShipments(opts, (error, data, response) => {
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
 **shipmentStatus** | [**ShipmentStatus**](.md)|  | [optional] 
 **batchId** | **String**| Batch ID | [optional] 
 **tag** | **String**| Search for shipments based on the custom tag added to the shipment object | [optional] 
 **createdAtStart** | **Date**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] 
 **createdAtEnd** | **Date**| Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time) | [optional] 
 **modifiedAtStart** | **Date**| Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time) | [optional] 
 **modifiedAtEnd** | **Date**| Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time) | [optional] 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per response. | [optional] [default to 25]
 **salesOrderId** | **String**| Sales Order ID | [optional] 
 **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] 
 **sortBy** | [**ShipmentsSortBy**](.md)|  | [optional] 

### Return type

[**ListShipmentsResponseBody**](ListShipmentsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## parseShipment

> ParseShipmentResponseBody parseShipment(parseShipmentRequestBody)

Parse shipping info

The shipment-recognition API makes it easy for you to extract shipping data from unstructured text, including people&#39;s names, addresses, package weights and dimensions, insurance and delivery requirements, and more.  Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine&#39;s shipment-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed shipment data is returned in the same structure that&#39;s used for other ShipEngine APIs, so you can easily use the parsed data to create a shipping label.  &gt; **Note:** Shipment recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let parseShipmentRequestBody = {"shipment":{"service_code":"usps_first_class_mail","ship_from":{"address_line1":"587 Shotwell St.","address_line2":"Suite 201","address_residential_indicator":true,"city_locality":"San Francisco","company_name":"My Awesome Store","country_code":"US","phone":"555-555-5555","postal_code":94110,"state_province":"CA"}},"text":"I have a 4oz package that's 5x10x14in, and I need to ship it to Margie McMiller at 3800 North Lamar suite 200 in austin, tx 78652. Please send it via USPS first class and require an adult signature. It also needs to be insured for $400.\n"}; // ParseShipmentRequestBody | The only required field is `text`, which is the text to be parsed. You can optionally also provide a `shipment` containing any already-known values. For example, you probably already know the `ship_from` address, and you may also already know what carrier and service you want to use. 
apiInstance.parseShipment(parseShipmentRequestBody, (error, data, response) => {
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
 **parseShipmentRequestBody** | [**ParseShipmentRequestBody**](ParseShipmentRequestBody.md)| The only required field is &#x60;text&#x60;, which is the text to be parsed. You can optionally also provide a &#x60;shipment&#x60; containing any already-known values. For example, you probably already know the &#x60;ship_from&#x60; address, and you may also already know what carrier and service you want to use.  | 

### Return type

[**ParseShipmentResponseBody**](ParseShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagShipment

> TagShipmentResponseBody tagShipment(shipmentId, tagName)

Add Tag to Shipment

Add a tag to the shipment object

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
let tagName = "tagName_example"; // String | 
apiInstance.tagShipment(shipmentId, tagName, (error, data, response) => {
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
 **tagName** | **String**|  | 

### Return type

[**TagShipmentResponseBody**](TagShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## untagShipment

> String untagShipment(shipmentId, tagName)

Remove Tag from Shipment

Remove an existing tag from the Shipment object

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
let tagName = "tagName_example"; // String | 
apiInstance.untagShipment(shipmentId, tagName, (error, data, response) => {
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
 **tagName** | **String**|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## updateShipment

> UpdateShipmentResponseBody updateShipment(shipmentId, updateShipmentRequestBody)

Update Shipment By ID

Update a shipment object based on its ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ShipmentsApi();
let shipmentId = "shipmentId_example"; // String | Shipment ID
let updateShipmentRequestBody = new ShipEngineApi.UpdateShipmentRequestBody(); // UpdateShipmentRequestBody | 
apiInstance.updateShipment(shipmentId, updateShipmentRequestBody, (error, data, response) => {
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
 **updateShipmentRequestBody** | [**UpdateShipmentRequestBody**](UpdateShipmentRequestBody.md)|  | 

### Return type

[**UpdateShipmentResponseBody**](UpdateShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

