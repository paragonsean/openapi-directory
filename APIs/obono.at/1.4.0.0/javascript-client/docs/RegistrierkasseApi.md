# ObonoRksvApi.RegistrierkasseApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDEP**](RegistrierkasseApi.md#getDEP) | **GET** /registrierkassen/{registrierkasseUuid}/dep | 
[**getRegistrierkasse**](RegistrierkasseApi.md#getRegistrierkasse) | **GET** /registrierkassen/{registrierkasseUuid} | 



## getDEP

> getDEP(registrierkasseUuid)



Generates a DEP file.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.RegistrierkasseApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the DEP file.
apiInstance.getDEP(registrierkasseUuid, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the DEP file. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRegistrierkasse

> Registrierkasse getRegistrierkasse(registrierkasseUuid)



Returns information about a particular &#x60;Registrierkasse&#x60;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.RegistrierkasseApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of a particular `Registrierkasse` to fetch.
apiInstance.getRegistrierkasse(registrierkasseUuid, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Registrierkasse&#x60; to fetch. | 

### Return type

[**Registrierkasse**](Registrierkasse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

