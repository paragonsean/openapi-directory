# PosApi.ModifierGroupsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modifierGroupsAdd**](ModifierGroupsApi.md#modifierGroupsAdd) | **POST** /pos/modifier-groups | Create Modifier Group
[**modifierGroupsAll**](ModifierGroupsApi.md#modifierGroupsAll) | **GET** /pos/modifier-groups | List Modifier Groups
[**modifierGroupsDelete**](ModifierGroupsApi.md#modifierGroupsDelete) | **DELETE** /pos/modifier-groups/{id} | Delete Modifier Group
[**modifierGroupsOne**](ModifierGroupsApi.md#modifierGroupsOne) | **GET** /pos/modifier-groups/{id} | Get Modifier Group
[**modifierGroupsUpdate**](ModifierGroupsApi.md#modifierGroupsUpdate) | **PATCH** /pos/modifier-groups/{id} | Update Modifier Group



## modifierGroupsAdd

> CreateModifierGroupResponse modifierGroupsAdd(xApideckConsumerId, xApideckAppId, modifierGroup, opts)

Create Modifier Group

Create Modifier Group

### Example

```javascript
import PosApi from 'pos_api';
let defaultClient = PosApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PosApi.ModifierGroupsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let modifierGroup = new PosApi.ModifierGroup(); // ModifierGroup | 
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example" // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
};
apiInstance.modifierGroupsAdd(xApideckConsumerId, xApideckAppId, modifierGroup, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **modifierGroup** | [**ModifierGroup**](ModifierGroup.md)|  | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 

### Return type

[**CreateModifierGroupResponse**](CreateModifierGroupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modifierGroupsAll

> GetModifierGroupsResponse modifierGroupsAll(xApideckConsumerId, xApideckAppId, opts)

List Modifier Groups

List Modifier Groups

### Example

```javascript
import PosApi from 'pos_api';
let defaultClient = PosApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PosApi.ModifierGroupsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20, // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.modifierGroupsAll(xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetModifierGroupsResponse**](GetModifierGroupsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modifierGroupsDelete

> DeleteModifierGroupResponse modifierGroupsDelete(id, xApideckConsumerId, xApideckAppId, opts)

Delete Modifier Group

Delete Modifier Group

### Example

```javascript
import PosApi from 'pos_api';
let defaultClient = PosApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PosApi.ModifierGroupsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.modifierGroupsDelete(id, xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**DeleteModifierGroupResponse**](DeleteModifierGroupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modifierGroupsOne

> GetModifierGroupResponse modifierGroupsOne(id, xApideckConsumerId, xApideckAppId, opts)

Get Modifier Group

Get Modifier Group

### Example

```javascript
import PosApi from 'pos_api';
let defaultClient = PosApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PosApi.ModifierGroupsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false, // Boolean | Include raw response. Mostly used for debugging purposes
  'fields': "id,updated_at" // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
};
apiInstance.modifierGroupsOne(id, xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]
 **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] 

### Return type

[**GetModifierGroupResponse**](GetModifierGroupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modifierGroupsUpdate

> UpdateModifierGroupResponse modifierGroupsUpdate(id, xApideckConsumerId, xApideckAppId, modifierGroup, opts)

Update Modifier Group

Update Modifier Group

### Example

```javascript
import PosApi from 'pos_api';
let defaultClient = PosApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PosApi.ModifierGroupsApi();
let id = "id_example"; // String | ID of the record you are acting upon.
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let modifierGroup = new PosApi.ModifierGroup(); // ModifierGroup | 
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.modifierGroupsUpdate(id, xApideckConsumerId, xApideckAppId, modifierGroup, opts, (error, data, response) => {
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
 **id** | **String**| ID of the record you are acting upon. | 
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **modifierGroup** | [**ModifierGroup**](ModifierGroup.md)|  | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**UpdateModifierGroupResponse**](UpdateModifierGroupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

