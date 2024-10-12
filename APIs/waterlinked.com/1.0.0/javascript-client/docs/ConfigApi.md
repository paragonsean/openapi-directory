# TheWaterLinkedUnderwaterGpsApi.ConfigApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configGet**](ConfigApi.md#configGet) | **GET** /api/v1/config/generic | Get config
[**configGetAntennaConfig**](ConfigApi.md#configGetAntennaConfig) | **GET** /api/v1/config/antenna | GetAntennaConfig config
[**configGetIP**](ConfigApi.md#configGetIP) | **GET** /api/v1/config/ip | GetIP config
[**configGetWIFI**](ConfigApi.md#configGetWIFI) | **GET** /api/v1/config/wifi | GetWIFI config
[**configListReceiver**](ConfigApi.md#configListReceiver) | **GET** /api/v1/config/receivers/ | ListReceiver config
[**configModify**](ConfigApi.md#configModify) | **PUT** /api/v1/config/generic | Modify config
[**configModifyAntennaConfig**](ConfigApi.md#configModifyAntennaConfig) | **PUT** /api/v1/config/antenna | ModifyAntennaConfig config
[**configModifyIP**](ConfigApi.md#configModifyIP) | **PUT** /api/v1/config/ip | ModifyIP config
[**configModifyReceiver**](ConfigApi.md#configModifyReceiver) | **PUT** /api/v1/config/receivers/{ID} | ModifyReceiver config
[**configModifyWIFI**](ConfigApi.md#configModifyWIFI) | **PUT** /api/v1/config/wifi | ModifyWIFI config
[**configShowReceiver**](ConfigApi.md#configShowReceiver) | **GET** /api/v1/config/receivers/{ID} | ShowReceiver config



## configGet

> WaterlinkedConfiguration configGet()

Get config

Get generic configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
apiInstance.configGet((error, data, response) => {
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

[**WaterlinkedConfiguration**](WaterlinkedConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.configuration+json, application/vnd.waterlinked.operation_response+json


## configGetAntennaConfig

> WaterlinkedAntennaConfig configGetAntennaConfig()

GetAntennaConfig config

Get Antenna configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
apiInstance.configGetAntennaConfig((error, data, response) => {
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

[**WaterlinkedAntennaConfig**](WaterlinkedAntennaConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.antenna_config+json


## configGetIP

> WaterlinkedIpConfig configGetIP()

GetIP config

Get IP configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
apiInstance.configGetIP((error, data, response) => {
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

[**WaterlinkedIpConfig**](WaterlinkedIpConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.ip_config+json


## configGetWIFI

> WaterlinkedWifiConfig configGetWIFI()

GetWIFI config

Get WIFI configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
apiInstance.configGetWIFI((error, data, response) => {
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

[**WaterlinkedWifiConfig**](WaterlinkedWifiConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.wifi_config+json


## configListReceiver

> [WaterlinkedReceiver] configListReceiver()

ListReceiver config

(Re)Load current receiver settings and return them

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
apiInstance.configListReceiver((error, data, response) => {
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

[**[WaterlinkedReceiver]**](WaterlinkedReceiver.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.receiver+json; type=collection


## configModify

> WaterlinkedOperationResponse configModify(payload)

Modify config

Modify generic configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.ModifyConfigPayload(); // ModifyConfigPayload | Configuration parameters
apiInstance.configModify(payload, (error, data, response) => {
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
 **payload** | [**ModifyConfigPayload**](ModifyConfigPayload.md)| Configuration parameters | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## configModifyAntennaConfig

> WaterlinkedOperationResponse configModifyAntennaConfig(payload)

ModifyAntennaConfig config

Modify Antenna configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.ModifyAntennaConfigConfigPayload(); // ModifyAntennaConfigConfigPayload | Configuration parameters for antenna set up
apiInstance.configModifyAntennaConfig(payload, (error, data, response) => {
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
 **payload** | [**ModifyAntennaConfigConfigPayload**](ModifyAntennaConfigConfigPayload.md)| Configuration parameters for antenna set up | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## configModifyIP

> WaterlinkedOperationResponse configModifyIP(payload)

ModifyIP config

Modify IP configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.ModifyIPConfigPayload(); // ModifyIPConfigPayload | Configuration parameters
apiInstance.configModifyIP(payload, (error, data, response) => {
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
 **payload** | [**ModifyIPConfigPayload**](ModifyIPConfigPayload.md)| Configuration parameters | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## configModifyReceiver

> configModifyReceiver(ID, payload)

ModifyReceiver config

Modify receiver configuration, does not apply the change until generic modify is called. Calling list will discard changes

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let ID = 56; // Number | Identifier
let payload = new TheWaterLinkedUnderwaterGpsApi.ModifyReceiverConfigPayload(); // ModifyReceiverConfigPayload | A receiver configuration
apiInstance.configModifyReceiver(ID, payload, (error, data, response) => {
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
 **ID** | **Number**| Identifier | 
 **payload** | [**ModifyReceiverConfigPayload**](ModifyReceiverConfigPayload.md)| A receiver configuration | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configModifyWIFI

> WaterlinkedOperationResponse configModifyWIFI(payload)

ModifyWIFI config

Modify WIFI configuration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.ModifyWIFIConfigPayload(); // ModifyWIFIConfigPayload | Configuration parameters
apiInstance.configModifyWIFI(payload, (error, data, response) => {
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
 **payload** | [**ModifyWIFIConfigPayload**](ModifyWIFIConfigPayload.md)| Configuration parameters | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## configShowReceiver

> WaterlinkedReceiver configShowReceiver(ID)

ShowReceiver config

Get receiver configuration by id

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ConfigApi();
let ID = 56; // Number | Identifier
apiInstance.configShowReceiver(ID, (error, data, response) => {
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
 **ID** | **Number**| Identifier | 

### Return type

[**WaterlinkedReceiver**](WaterlinkedReceiver.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.receiver+json

