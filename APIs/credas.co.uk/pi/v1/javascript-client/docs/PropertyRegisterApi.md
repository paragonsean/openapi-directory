# CredasApi.PropertyRegisterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPropertyRegisterCheck**](PropertyRegisterApi.md#addPropertyRegisterCheck) | **POST** /api/property-register | Creates new property registry check against the registration.
[**getPropertyRegisterCheckResult**](PropertyRegisterApi.md#getPropertyRegisterCheckResult) | **GET** /api/property-register/{id} | Retrieves property registry check associated with the registration.



## addPropertyRegisterCheck

> CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse addPropertyRegisterCheck(apikey, opts)

Creates new property registry check against the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.PropertyRegisterApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsPropertyRegisterPropertyRegisterCheckRequest': new CredasApi.CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest() // CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest | Object containing check details.
};
apiInstance.addPropertyRegisterCheck(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsPropertyRegisterPropertyRegisterCheckRequest** | [**CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest**](CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest.md)| Object containing check details. | [optional] 

### Return type

[**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## getPropertyRegisterCheckResult

> CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse getPropertyRegisterCheckResult(id, apikey)

Retrieves property registry check associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.PropertyRegisterApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getPropertyRegisterCheckResult(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

