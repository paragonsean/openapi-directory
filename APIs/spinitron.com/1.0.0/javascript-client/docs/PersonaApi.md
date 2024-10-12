# SpinitronV2Api.PersonaApi

All URIs are relative to *https://spinitron.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**personasGet**](PersonaApi.md#personasGet) | **GET** /personas | Get Personas
[**personasIdGet**](PersonaApi.md#personasIdGet) | **GET** /personas/{id} | Get Persona by id



## personasGet

> PersonasGet200Response personasGet(opts)

Get Personas

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.PersonaApi();
let opts = {
  'name': "name_example", // String | Filter by Persona name
  'count': 20, // Number | Amount of items to return
  'page': 56, // Number | Offset, used together with count
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.personasGet(opts, (error, data, response) => {
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
 **name** | **String**| Filter by Persona name | [optional] 
 **count** | **Number**| Amount of items to return | [optional] [default to 20]
 **page** | **Number**| Offset, used together with count | [optional] 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**PersonasGet200Response**](PersonasGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## personasIdGet

> Persona personasIdGet(id, opts)

Get Persona by id

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.PersonaApi();
let id = 56; // Number | 
let opts = {
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.personasIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**Persona**](Persona.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

