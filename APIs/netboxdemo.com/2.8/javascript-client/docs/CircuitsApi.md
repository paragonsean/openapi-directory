# NetBoxApi.CircuitsApi

All URIs are relative to *https://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**circuitsCircuitTerminationsCreate**](CircuitsApi.md#circuitsCircuitTerminationsCreate) | **POST** /circuits/circuit-terminations/ | 
[**circuitsCircuitTerminationsDelete**](CircuitsApi.md#circuitsCircuitTerminationsDelete) | **DELETE** /circuits/circuit-terminations/{id}/ | 
[**circuitsCircuitTerminationsList**](CircuitsApi.md#circuitsCircuitTerminationsList) | **GET** /circuits/circuit-terminations/ | 
[**circuitsCircuitTerminationsPartialUpdate**](CircuitsApi.md#circuitsCircuitTerminationsPartialUpdate) | **PATCH** /circuits/circuit-terminations/{id}/ | 
[**circuitsCircuitTerminationsRead**](CircuitsApi.md#circuitsCircuitTerminationsRead) | **GET** /circuits/circuit-terminations/{id}/ | 
[**circuitsCircuitTerminationsUpdate**](CircuitsApi.md#circuitsCircuitTerminationsUpdate) | **PUT** /circuits/circuit-terminations/{id}/ | 
[**circuitsCircuitTypesCreate**](CircuitsApi.md#circuitsCircuitTypesCreate) | **POST** /circuits/circuit-types/ | 
[**circuitsCircuitTypesDelete**](CircuitsApi.md#circuitsCircuitTypesDelete) | **DELETE** /circuits/circuit-types/{id}/ | 
[**circuitsCircuitTypesList**](CircuitsApi.md#circuitsCircuitTypesList) | **GET** /circuits/circuit-types/ | 
[**circuitsCircuitTypesPartialUpdate**](CircuitsApi.md#circuitsCircuitTypesPartialUpdate) | **PATCH** /circuits/circuit-types/{id}/ | 
[**circuitsCircuitTypesRead**](CircuitsApi.md#circuitsCircuitTypesRead) | **GET** /circuits/circuit-types/{id}/ | 
[**circuitsCircuitTypesUpdate**](CircuitsApi.md#circuitsCircuitTypesUpdate) | **PUT** /circuits/circuit-types/{id}/ | 
[**circuitsCircuitsCreate**](CircuitsApi.md#circuitsCircuitsCreate) | **POST** /circuits/circuits/ | 
[**circuitsCircuitsDelete**](CircuitsApi.md#circuitsCircuitsDelete) | **DELETE** /circuits/circuits/{id}/ | 
[**circuitsCircuitsList**](CircuitsApi.md#circuitsCircuitsList) | **GET** /circuits/circuits/ | 
[**circuitsCircuitsPartialUpdate**](CircuitsApi.md#circuitsCircuitsPartialUpdate) | **PATCH** /circuits/circuits/{id}/ | 
[**circuitsCircuitsRead**](CircuitsApi.md#circuitsCircuitsRead) | **GET** /circuits/circuits/{id}/ | 
[**circuitsCircuitsUpdate**](CircuitsApi.md#circuitsCircuitsUpdate) | **PUT** /circuits/circuits/{id}/ | 
[**circuitsProvidersCreate**](CircuitsApi.md#circuitsProvidersCreate) | **POST** /circuits/providers/ | 
[**circuitsProvidersDelete**](CircuitsApi.md#circuitsProvidersDelete) | **DELETE** /circuits/providers/{id}/ | 
[**circuitsProvidersGraphs**](CircuitsApi.md#circuitsProvidersGraphs) | **GET** /circuits/providers/{id}/graphs/ | 
[**circuitsProvidersList**](CircuitsApi.md#circuitsProvidersList) | **GET** /circuits/providers/ | 
[**circuitsProvidersPartialUpdate**](CircuitsApi.md#circuitsProvidersPartialUpdate) | **PATCH** /circuits/providers/{id}/ | 
[**circuitsProvidersRead**](CircuitsApi.md#circuitsProvidersRead) | **GET** /circuits/providers/{id}/ | 
[**circuitsProvidersUpdate**](CircuitsApi.md#circuitsProvidersUpdate) | **PUT** /circuits/providers/{id}/ | 



## circuitsCircuitTerminationsCreate

> CircuitTermination circuitsCircuitTerminationsCreate(writableCircuitTermination)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let writableCircuitTermination = new NetBoxApi.WritableCircuitTermination(); // WritableCircuitTermination | 
apiInstance.circuitsCircuitTerminationsCreate(writableCircuitTermination, (error, data, response) => {
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
 **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitTerminationsDelete

> circuitsCircuitTerminationsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit termination.
apiInstance.circuitsCircuitTerminationsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit termination. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## circuitsCircuitTerminationsList

> CircuitsCircuitTerminationsList200Response circuitsCircuitTerminationsList(opts)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let opts = {
  'termSide': "termSide_example", // String | 
  'portSpeed': "portSpeed_example", // String | 
  'upstreamSpeed': "upstreamSpeed_example", // String | 
  'xconnectId': "xconnectId_example", // String | 
  'q': "q_example", // String | 
  'circuitId': "circuitId_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'termSideN': "termSideN_example", // String | 
  'portSpeedN': "portSpeedN_example", // String | 
  'portSpeedLte': "portSpeedLte_example", // String | 
  'portSpeedLt': "portSpeedLt_example", // String | 
  'portSpeedGte': "portSpeedGte_example", // String | 
  'portSpeedGt': "portSpeedGt_example", // String | 
  'upstreamSpeedN': "upstreamSpeedN_example", // String | 
  'upstreamSpeedLte': "upstreamSpeedLte_example", // String | 
  'upstreamSpeedLt': "upstreamSpeedLt_example", // String | 
  'upstreamSpeedGte': "upstreamSpeedGte_example", // String | 
  'upstreamSpeedGt': "upstreamSpeedGt_example", // String | 
  'xconnectIdN': "xconnectIdN_example", // String | 
  'xconnectIdIc': "xconnectIdIc_example", // String | 
  'xconnectIdNic': "xconnectIdNic_example", // String | 
  'xconnectIdIew': "xconnectIdIew_example", // String | 
  'xconnectIdNiew': "xconnectIdNiew_example", // String | 
  'xconnectIdIsw': "xconnectIdIsw_example", // String | 
  'xconnectIdNisw': "xconnectIdNisw_example", // String | 
  'xconnectIdIe': "xconnectIdIe_example", // String | 
  'xconnectIdNie': "xconnectIdNie_example", // String | 
  'circuitIdN': "circuitIdN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.circuitsCircuitTerminationsList(opts, (error, data, response) => {
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
 **termSide** | **String**|  | [optional] 
 **portSpeed** | **String**|  | [optional] 
 **upstreamSpeed** | **String**|  | [optional] 
 **xconnectId** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **circuitId** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **termSideN** | **String**|  | [optional] 
 **portSpeedN** | **String**|  | [optional] 
 **portSpeedLte** | **String**|  | [optional] 
 **portSpeedLt** | **String**|  | [optional] 
 **portSpeedGte** | **String**|  | [optional] 
 **portSpeedGt** | **String**|  | [optional] 
 **upstreamSpeedN** | **String**|  | [optional] 
 **upstreamSpeedLte** | **String**|  | [optional] 
 **upstreamSpeedLt** | **String**|  | [optional] 
 **upstreamSpeedGte** | **String**|  | [optional] 
 **upstreamSpeedGt** | **String**|  | [optional] 
 **xconnectIdN** | **String**|  | [optional] 
 **xconnectIdIc** | **String**|  | [optional] 
 **xconnectIdNic** | **String**|  | [optional] 
 **xconnectIdIew** | **String**|  | [optional] 
 **xconnectIdNiew** | **String**|  | [optional] 
 **xconnectIdIsw** | **String**|  | [optional] 
 **xconnectIdNisw** | **String**|  | [optional] 
 **xconnectIdIe** | **String**|  | [optional] 
 **xconnectIdNie** | **String**|  | [optional] 
 **circuitIdN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**CircuitsCircuitTerminationsList200Response**](CircuitsCircuitTerminationsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitTerminationsPartialUpdate

> CircuitTermination circuitsCircuitTerminationsPartialUpdate(id, writableCircuitTermination)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit termination.
let writableCircuitTermination = new NetBoxApi.WritableCircuitTermination(); // WritableCircuitTermination | 
apiInstance.circuitsCircuitTerminationsPartialUpdate(id, writableCircuitTermination, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit termination. | 
 **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitTerminationsRead

> CircuitTermination circuitsCircuitTerminationsRead(id)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit termination.
apiInstance.circuitsCircuitTerminationsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit termination. | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitTerminationsUpdate

> CircuitTermination circuitsCircuitTerminationsUpdate(id, writableCircuitTermination)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit termination.
let writableCircuitTermination = new NetBoxApi.WritableCircuitTermination(); // WritableCircuitTermination | 
apiInstance.circuitsCircuitTerminationsUpdate(id, writableCircuitTermination, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit termination. | 
 **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitTypesCreate

> CircuitType circuitsCircuitTypesCreate(circuitType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let circuitType = new NetBoxApi.CircuitType(); // CircuitType | 
apiInstance.circuitsCircuitTypesCreate(circuitType, (error, data, response) => {
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
 **circuitType** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitTypesDelete

> circuitsCircuitTypesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit type.
apiInstance.circuitsCircuitTypesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit type. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## circuitsCircuitTypesList

> CircuitsCircuitTypesList200Response circuitsCircuitTypesList(opts)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let opts = {
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.circuitsCircuitTypesList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**CircuitsCircuitTypesList200Response**](CircuitsCircuitTypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitTypesPartialUpdate

> CircuitType circuitsCircuitTypesPartialUpdate(id, circuitType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit type.
let circuitType = new NetBoxApi.CircuitType(); // CircuitType | 
apiInstance.circuitsCircuitTypesPartialUpdate(id, circuitType, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit type. | 
 **circuitType** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitTypesRead

> CircuitType circuitsCircuitTypesRead(id)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit type.
apiInstance.circuitsCircuitTypesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit type. | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitTypesUpdate

> CircuitType circuitsCircuitTypesUpdate(id, circuitType)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit type.
let circuitType = new NetBoxApi.CircuitType(); // CircuitType | 
apiInstance.circuitsCircuitTypesUpdate(id, circuitType, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit type. | 
 **circuitType** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitsCreate

> Circuit circuitsCircuitsCreate(writableCircuit)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let writableCircuit = new NetBoxApi.WritableCircuit(); // WritableCircuit | 
apiInstance.circuitsCircuitsCreate(writableCircuit, (error, data, response) => {
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
 **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitsDelete

> circuitsCircuitsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit.
apiInstance.circuitsCircuitsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## circuitsCircuitsList

> CircuitsCircuitsList200Response circuitsCircuitsList(opts)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let opts = {
  'id': "id_example", // String | 
  'cid': "cid_example", // String | 
  'installDate': "installDate_example", // String | 
  'commitRate': "commitRate_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'providerId': "providerId_example", // String | 
  'provider': "provider_example", // String | 
  'typeId': "typeId_example", // String | 
  'type': "type_example", // String | 
  'status': "status_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'cidN': "cidN_example", // String | 
  'cidIc': "cidIc_example", // String | 
  'cidNic': "cidNic_example", // String | 
  'cidIew': "cidIew_example", // String | 
  'cidNiew': "cidNiew_example", // String | 
  'cidIsw': "cidIsw_example", // String | 
  'cidNisw': "cidNisw_example", // String | 
  'cidIe': "cidIe_example", // String | 
  'cidNie': "cidNie_example", // String | 
  'installDateN': "installDateN_example", // String | 
  'installDateLte': "installDateLte_example", // String | 
  'installDateLt': "installDateLt_example", // String | 
  'installDateGte': "installDateGte_example", // String | 
  'installDateGt': "installDateGt_example", // String | 
  'commitRateN': "commitRateN_example", // String | 
  'commitRateLte': "commitRateLte_example", // String | 
  'commitRateLt': "commitRateLt_example", // String | 
  'commitRateGte': "commitRateGte_example", // String | 
  'commitRateGt': "commitRateGt_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'providerIdN': "providerIdN_example", // String | 
  'providerN': "providerN_example", // String | 
  'typeIdN': "typeIdN_example", // String | 
  'typeN': "typeN_example", // String | 
  'statusN': "statusN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'tagN': "tagN_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.circuitsCircuitsList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **cid** | **String**|  | [optional] 
 **installDate** | **String**|  | [optional] 
 **commitRate** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **providerId** | **String**|  | [optional] 
 **provider** | **String**|  | [optional] 
 **typeId** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **cidN** | **String**|  | [optional] 
 **cidIc** | **String**|  | [optional] 
 **cidNic** | **String**|  | [optional] 
 **cidIew** | **String**|  | [optional] 
 **cidNiew** | **String**|  | [optional] 
 **cidIsw** | **String**|  | [optional] 
 **cidNisw** | **String**|  | [optional] 
 **cidIe** | **String**|  | [optional] 
 **cidNie** | **String**|  | [optional] 
 **installDateN** | **String**|  | [optional] 
 **installDateLte** | **String**|  | [optional] 
 **installDateLt** | **String**|  | [optional] 
 **installDateGte** | **String**|  | [optional] 
 **installDateGt** | **String**|  | [optional] 
 **commitRateN** | **String**|  | [optional] 
 **commitRateLte** | **String**|  | [optional] 
 **commitRateLt** | **String**|  | [optional] 
 **commitRateGte** | **String**|  | [optional] 
 **commitRateGt** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **providerIdN** | **String**|  | [optional] 
 **providerN** | **String**|  | [optional] 
 **typeIdN** | **String**|  | [optional] 
 **typeN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**CircuitsCircuitsList200Response**](CircuitsCircuitsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitsPartialUpdate

> Circuit circuitsCircuitsPartialUpdate(id, writableCircuit)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit.
let writableCircuit = new NetBoxApi.WritableCircuit(); // WritableCircuit | 
apiInstance.circuitsCircuitsPartialUpdate(id, writableCircuit, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit. | 
 **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsCircuitsRead

> Circuit circuitsCircuitsRead(id)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit.
apiInstance.circuitsCircuitsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit. | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsCircuitsUpdate

> Circuit circuitsCircuitsUpdate(id, writableCircuit)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this circuit.
let writableCircuit = new NetBoxApi.WritableCircuit(); // WritableCircuit | 
apiInstance.circuitsCircuitsUpdate(id, writableCircuit, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this circuit. | 
 **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsProvidersCreate

> Provider circuitsProvidersCreate(provider)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let provider = new NetBoxApi.Provider(); // Provider | 
apiInstance.circuitsProvidersCreate(provider, (error, data, response) => {
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
 **provider** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsProvidersDelete

> circuitsProvidersDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this provider.
apiInstance.circuitsProvidersDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this provider. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## circuitsProvidersGraphs

> Provider circuitsProvidersGraphs(id)



A convenience method for rendering graphs for a particular provider.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this provider.
apiInstance.circuitsProvidersGraphs(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsProvidersList

> CircuitsProvidersList200Response circuitsProvidersList(opts)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let opts = {
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'asn': "asn_example", // String | 
  'account': "account_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'asnN': "asnN_example", // String | 
  'asnLte': "asnLte_example", // String | 
  'asnLt': "asnLt_example", // String | 
  'asnGte': "asnGte_example", // String | 
  'asnGt': "asnGt_example", // String | 
  'accountN': "accountN_example", // String | 
  'accountIc': "accountIc_example", // String | 
  'accountNic': "accountNic_example", // String | 
  'accountIew': "accountIew_example", // String | 
  'accountNiew': "accountNiew_example", // String | 
  'accountIsw': "accountIsw_example", // String | 
  'accountNisw': "accountNisw_example", // String | 
  'accountIe': "accountIe_example", // String | 
  'accountNie': "accountNie_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'tagN': "tagN_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.circuitsProvidersList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **asn** | **String**|  | [optional] 
 **account** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **asnN** | **String**|  | [optional] 
 **asnLte** | **String**|  | [optional] 
 **asnLt** | **String**|  | [optional] 
 **asnGte** | **String**|  | [optional] 
 **asnGt** | **String**|  | [optional] 
 **accountN** | **String**|  | [optional] 
 **accountIc** | **String**|  | [optional] 
 **accountNic** | **String**|  | [optional] 
 **accountIew** | **String**|  | [optional] 
 **accountNiew** | **String**|  | [optional] 
 **accountIsw** | **String**|  | [optional] 
 **accountNisw** | **String**|  | [optional] 
 **accountIe** | **String**|  | [optional] 
 **accountNie** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**CircuitsProvidersList200Response**](CircuitsProvidersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsProvidersPartialUpdate

> Provider circuitsProvidersPartialUpdate(id, provider)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this provider.
let provider = new NetBoxApi.Provider(); // Provider | 
apiInstance.circuitsProvidersPartialUpdate(id, provider, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this provider. | 
 **provider** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## circuitsProvidersRead

> Provider circuitsProvidersRead(id)



Call to super to allow for caching

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this provider.
apiInstance.circuitsProvidersRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## circuitsProvidersUpdate

> Provider circuitsProvidersUpdate(id, provider)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.CircuitsApi();
let id = 56; // Number | A unique integer value identifying this provider.
let provider = new NetBoxApi.Provider(); // Provider | 
apiInstance.circuitsProvidersUpdate(id, provider, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this provider. | 
 **provider** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

