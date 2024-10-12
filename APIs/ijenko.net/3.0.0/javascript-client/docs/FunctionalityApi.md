# IoEIoTApiToCreateEndUserApplications.FunctionalityApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deviceAddFunctionality_0**](FunctionalityApi.md#deviceAddFunctionality_0) | **POST** /devices/{deviceId}/functionalities | Add dynamically a functionality
[**functionalitiesGet**](FunctionalityApi.md#functionalitiesGet) | **GET** /functionalities/{functionalityId} | Information about a Functionality
[**functionalityGetMetadata**](FunctionalityApi.md#functionalityGetMetadata) | **GET** /functionalities/{functionalityId}/metadata | List metadata
[**functionalityGetTags**](FunctionalityApi.md#functionalityGetTags) | **GET** /functionalities/{functionalityId}/tags | List tags
[**functionalityPatch**](FunctionalityApi.md#functionalityPatch) | **PATCH** /functionalities/{functionalityId} | Modify a Functionality
[**functionalityPatchMetadata**](FunctionalityApi.md#functionalityPatchMetadata) | **PATCH** /functionalities/{functionalityId}/metadata | Modify metadata
[**functionalityPatchTags**](FunctionalityApi.md#functionalityPatchTags) | **PATCH** /functionalities/{functionalityId}/tags | Modify tags
[**functionalitySet**](FunctionalityApi.md#functionalitySet) | **PUT** /functionalities/{functionalityId}/attributes/{attributeName} | Modify an Attribute value
[**functionalityValue**](FunctionalityApi.md#functionalityValue) | **GET** /functionalities/{functionalityId}/attributes/{attributeName} | Get an Attribute value
[**functionalityValues**](FunctionalityApi.md#functionalityValues) | **GET** /functionalities/{functionalityId}/attributes | Get history of multiple attributes
[**placeFunctionalities**](FunctionalityApi.md#placeFunctionalities) | **GET** /places/{placeId}/functionalities | List Functionalities



## deviceAddFunctionality_0

> FunctionalityCreated deviceAddFunctionality_0(deviceId, functionalityInfo)

Add dynamically a functionality

Add a *Functionality* to the device.  Required parameters are : - functionality class - endpoint  Each device class has its own restrictions on which Functionality classes can be added and on which endpoints. Only a few devices allow to add Functionalities.  |Device class|Functionality class|Endpoints| |------------|-------------------|---------| |MINT        |CurrentPeriod      |1,2,3    | |MINT        |ElectricityRates   |1,2,3    | |MINT        |GenericRate        |1,2,3    |  **Note**: requires full access to the *Account*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
let functionalityInfo = new IoEIoTApiToCreateEndUserApplications.FunctionalityNew(); // FunctionalityNew | 
apiInstance.deviceAddFunctionality_0(deviceId, functionalityInfo, (error, data, response) => {
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
 **deviceId** | **String**| Unique identifier of a *Device*. | 
 **functionalityInfo** | [**FunctionalityNew**](FunctionalityNew.md)|  | 

### Return type

[**FunctionalityCreated**](FunctionalityCreated.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalitiesGet

> Functionality functionalitiesGet(functionalityId)

Information about a Functionality

Get the *Functionality*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
apiInstance.functionalitiesGet(functionalityId, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 

### Return type

[**Functionality**](Functionality.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionalityGetMetadata

> {String: Object} functionalityGetMetadata(functionalityId)

List metadata

Get the metadata.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
apiInstance.functionalityGetMetadata(functionalityId, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionalityGetTags

> [String] functionalityGetTags(functionalityId)

List tags

Get the tags of a *Functionality*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
apiInstance.functionalityGetTags(functionalityId, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 

### Return type

**[String]**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionalityPatch

> functionalityPatch(functionalityId, functionalityPatch)

Modify a Functionality

Modify information about a *Functionality*: its name. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let functionalityPatch = new IoEIoTApiToCreateEndUserApplications.FunctionalityPatch(); // FunctionalityPatch | 
apiInstance.functionalityPatch(functionalityId, functionalityPatch, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **functionalityPatch** | [**FunctionalityPatch**](FunctionalityPatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalityPatchMetadata

> {String: Object} functionalityPatchMetadata(functionalityId, metadataPatch)

Modify metadata

Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let metadataPatch = new IoEIoTApiToCreateEndUserApplications.MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
apiInstance.functionalityPatchMetadata(functionalityId, metadataPatch, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalityPatchTags

> [String] functionalityPatchTags(functionalityId, tagsPatch)

Modify tags

Modify the tags of a *Functionality*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let tagsPatch = new IoEIoTApiToCreateEndUserApplications.TagsPatch(); // TagsPatch | Modifications to apply to the tags list of the resource. 
apiInstance.functionalityPatchTags(functionalityId, tagsPatch, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **tagsPatch** | [**TagsPatch**](TagsPatch.md)| Modifications to apply to the tags list of the resource.  | 

### Return type

**[String]**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalitySet

> functionalitySet(functionalityId, attributeName, value)

Modify an Attribute value

Modify the value of the *Attribute*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let attributeName = "attributeName_example"; // String | Identifier of an *Attribute* inside a *Functionality*.
let value = {key: null}; // Object | New value for the *Attribute*.
apiInstance.functionalitySet(functionalityId, attributeName, value, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **attributeName** | **String**| Identifier of an *Attribute* inside a *Functionality*. | 
 **value** | **Object**| New value for the *Attribute*. | 

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalityValue

> AttributeValue functionalityValue(functionalityId, attributeName)

Get an Attribute value

Get the *Attribute* value and the last time when it changed.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let attributeName = "attributeName_example"; // String | Identifier of an *Attribute* inside a *Functionality*.
apiInstance.functionalityValue(functionalityId, attributeName, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **attributeName** | **String**| Identifier of an *Attribute* inside a *Functionality*. | 

### Return type

[**AttributeValue**](AttributeValue.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionalityValues

> {String: [AttributeValue]} functionalityValues(functionalityId, opts)

Get history of multiple attributes

Get the values of multiple *Attributes* and their history.  If the &#x60;names&#x60; parameter is not given, all the attributes of the *Functionality* are returned. As the list may be huge, this must be avoided.  If the &#x60;to&#x60; parameter is set, &#x60;from&#x60; must also be set.  If &#x60;from&#x60; is not set, only the last value is returned.  The &#x60;surround&#x60; parameter allows to ask also for one value beyond each interval boundaries.  The request may fail if too many values are asked. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let opts = {
  'names': ["null"], // [String] | One or multiple *Attribute* names separated by commas
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Beginning of the time interval.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | End of the interval. Default: now. 
  'surround': true // Boolean | If true, return also one value before from and one value after to
};
apiInstance.functionalityValues(functionalityId, opts, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **names** | [**[String]**](String.md)| One or multiple *Attribute* names separated by commas | [optional] 
 **from** | **Date**| Beginning of the time interval. | [optional] 
 **to** | **Date**| End of the interval. Default: now.  | [optional] 
 **surround** | **Boolean**| If true, return also one value before from and one value after to | [optional] 

### Return type

**{String: [AttributeValue]}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeFunctionalities

> [FunctionalityItem] placeFunctionalities(placeId, opts)

List Functionalities

Get the list of *Functionalities* available in this *Place*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.FunctionalityApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let opts = {
  'devices': "devices_example", // String | Devices selector. Device tags or device classes or device ids or '*' for any. Multiple values are separated by '|' and interpreted as « OR ».
  'functionalities': "functionalities_example", // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
  'embedMetadata': ["null"] // [String] | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
};
apiInstance.placeFunctionalities(placeId, opts, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **devices** | **String**| Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ». | [optional] 
 **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | [optional] 
 **embedMetadata** | [**[String]**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] 

### Return type

[**[FunctionalityItem]**](FunctionalityItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

