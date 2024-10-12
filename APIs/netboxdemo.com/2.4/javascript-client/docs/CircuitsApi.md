# NetBoxApi.CircuitsApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**circuitsChoicesList**](CircuitsApi.md#circuitsChoicesList) | **GET** /circuits/_choices/ | 
[**circuitsChoicesRead**](CircuitsApi.md#circuitsChoicesRead) | **GET** /circuits/_choices/{id}/ | 
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



## circuitsChoicesList

> circuitsChoicesList()





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
apiInstance.circuitsChoicesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## circuitsChoicesRead

> circuitsChoicesRead(id)





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
let id = "id_example"; // String | 
apiInstance.circuitsChoicesRead(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


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
  'portSpeed': 3.4, // Number | 
  'upstreamSpeed': 3.4, // Number | 
  'xconnectId': "xconnectId_example", // String | 
  'q': "q_example", // String | 
  'circuitId': "circuitId_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
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
 **portSpeed** | **Number**|  | [optional] 
 **upstreamSpeed** | **Number**|  | [optional] 
 **xconnectId** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **circuitId** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
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
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
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
  'cid': "cid_example", // String | 
  'installDate': "installDate_example", // String | 
  'commitRate': 3.4, // Number | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'providerId': "providerId_example", // String | 
  'provider': "provider_example", // String | 
  'typeId': "typeId_example", // String | 
  'type': "type_example", // String | 
  'status': "status_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'tag': "tag_example", // String | 
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
 **cid** | **String**|  | [optional] 
 **installDate** | **String**|  | [optional] 
 **commitRate** | **Number**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **providerId** | **String**|  | [optional] 
 **provider** | **String**|  | [optional] 
 **typeId** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
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
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'asn': 3.4, // Number | 
  'account': "account_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'tag': "tag_example", // String | 
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **asn** | **Number**|  | [optional] 
 **account** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
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

