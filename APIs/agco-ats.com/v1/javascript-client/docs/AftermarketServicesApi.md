# AgcoApi.AftermarketServicesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aftermarketServicesGetCerts**](AftermarketServicesApi.md#aftermarketServicesGetCerts) | **GET** /api/v2/AftermarketServices/Certificates | No Documentation Found.
[**aftermarketServicesGetConnectionStatus**](AftermarketServicesApi.md#aftermarketServicesGetConnectionStatus) | **GET** /api/v2/AftermarketServices/Hello | Check whether there is connectivity to AGCO Power Web Services
[**aftermarketServicesGetEngineIQACodes**](AftermarketServicesApi.md#aftermarketServicesGetEngineIQACodes) | **GET** /api/v2/AftermarketServices/Engines/{serialNumber}/IQACodes | Get injector codes given engine.
[**aftermarketServicesGetProductionData**](AftermarketServicesApi.md#aftermarketServicesGetProductionData) | **GET** /api/v2/AftermarketServices/Engines/{serialNumber}/ProductionData | Get production calibration data for given engine.
[**aftermarketServicesGetUserStatus**](AftermarketServicesApi.md#aftermarketServicesGetUserStatus) | **GET** /api/v2/AftermarketServices/UserStatuses | Retrieve the status of an EDT Kit Registration with AGCO Power Web Services
[**aftermarketServicesPutECU**](AftermarketServicesApi.md#aftermarketServicesPutECU) | **PUT** /api/v2/AftermarketServices/ECUs/{serialNumber} | Activate or Deactivate an ECU, or Report an ECU as Damaged.
[**aftermarketServicesPutIQACodes**](AftermarketServicesApi.md#aftermarketServicesPutIQACodes) | **PUT** /api/v2/AftermarketServices/Engines/{serialNumber}/IQACodes | Report the IQA codes used by an engine
[**aftermarketServicesUpdateUserStatus**](AftermarketServicesApi.md#aftermarketServicesUpdateUserStatus) | **PUT** /api/v2/AftermarketServices/UserStatuses | Update the status of an EDT Kit Registration with AGCO Power Web Services



## aftermarketServicesGetCerts

> Object aftermarketServicesGetCerts()

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
apiInstance.aftermarketServicesGetCerts((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesGetConnectionStatus

> Boolean aftermarketServicesGetConnectionStatus()

Check whether there is connectivity to AGCO Power Web Services

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
apiInstance.aftermarketServicesGetConnectionStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesGetEngineIQACodes

> [String] aftermarketServicesGetEngineIQACodes(serialNumber, eDTInstanceId)

Get injector codes given engine.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let serialNumber = "serialNumber_example"; // String | The serial number of the engine.
let eDTInstanceId = "eDTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
apiInstance.aftermarketServicesGetEngineIQACodes(serialNumber, eDTInstanceId, (error, data, response) => {
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
 **serialNumber** | **String**| The serial number of the engine. | 
 **eDTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesGetProductionData

> [AGCOPowerServicesModelsProductionData] aftermarketServicesGetProductionData(serialNumber, eDTInstanceId)

Get production calibration data for given engine.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let serialNumber = "serialNumber_example"; // String | The serial number of the engine.
let eDTInstanceId = "eDTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
apiInstance.aftermarketServicesGetProductionData(serialNumber, eDTInstanceId, (error, data, response) => {
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
 **serialNumber** | **String**| The serial number of the engine. | 
 **eDTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | 

### Return type

[**[AGCOPowerServicesModelsProductionData]**](AGCOPowerServicesModelsProductionData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesGetUserStatus

> AGCOPowerServicesModelsUserStatus aftermarketServicesGetUserStatus(voucherCode, dealerCode)

Retrieve the status of an EDT Kit Registration with AGCO Power Web Services

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let voucherCode = "voucherCode_example"; // String | 
let dealerCode = "dealerCode_example"; // String | 
apiInstance.aftermarketServicesGetUserStatus(voucherCode, dealerCode, (error, data, response) => {
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
 **voucherCode** | **String**|  | 
 **dealerCode** | **String**|  | 

### Return type

[**AGCOPowerServicesModelsUserStatus**](AGCOPowerServicesModelsUserStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesPutECU

> AGCOPowerServicesModelsECU aftermarketServicesPutECU(serialNumber, eDTInstanceId, aGCOPowerServicesModelsECU)

Activate or Deactivate an ECU, or Report an ECU as Damaged.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let serialNumber = "serialNumber_example"; // String | The serial number of the ECU.
let eDTInstanceId = "eDTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
let aGCOPowerServicesModelsECU = new AgcoApi.AGCOPowerServicesModelsECU(); // AGCOPowerServicesModelsECU | The ecu to modify.
apiInstance.aftermarketServicesPutECU(serialNumber, eDTInstanceId, aGCOPowerServicesModelsECU, (error, data, response) => {
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
 **serialNumber** | **String**| The serial number of the ECU. | 
 **eDTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | 
 **aGCOPowerServicesModelsECU** | [**AGCOPowerServicesModelsECU**](AGCOPowerServicesModelsECU.md)| The ecu to modify. | 

### Return type

[**AGCOPowerServicesModelsECU**](AGCOPowerServicesModelsECU.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesPutIQACodes

> Boolean aftermarketServicesPutIQACodes(serialNumber, eDTInstanceId, requestBody)

Report the IQA codes used by an engine

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let serialNumber = "serialNumber_example"; // String | The serial number of the Engine
let eDTInstanceId = "eDTInstanceId_example"; // String | The EDT Instance Id of the kit calling this method.
let requestBody = ["null"]; // [String] | A string array of IQA codes in physical order
apiInstance.aftermarketServicesPutIQACodes(serialNumber, eDTInstanceId, requestBody, (error, data, response) => {
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
 **serialNumber** | **String**| The serial number of the Engine | 
 **eDTInstanceId** | **String**| The EDT Instance Id of the kit calling this method. | 
 **requestBody** | [**[String]**](String.md)| A string array of IQA codes in physical order | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## aftermarketServicesUpdateUserStatus

> Boolean aftermarketServicesUpdateUserStatus(aGCOPowerServicesModelsUserStatus)

Update the status of an EDT Kit Registration with AGCO Power Web Services

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AftermarketServicesApi();
let aGCOPowerServicesModelsUserStatus = new AgcoApi.AGCOPowerServicesModelsUserStatus(); // AGCOPowerServicesModelsUserStatus | 
apiInstance.aftermarketServicesUpdateUserStatus(aGCOPowerServicesModelsUserStatus, (error, data, response) => {
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
 **aGCOPowerServicesModelsUserStatus** | [**AGCOPowerServicesModelsUserStatus**](AGCOPowerServicesModelsUserStatus.md)|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

