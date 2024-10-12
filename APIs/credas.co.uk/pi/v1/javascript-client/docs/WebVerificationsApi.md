# CredasApi.WebVerificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWebVerificationsByReferenceId**](WebVerificationsApi.md#getWebVerificationsByReferenceId) | **POST** /api/web-verifications/by-referenceid | Retrieves secure links to web verification pages searching by the Reference Id.
[**getWebVerificationsByRegistrationId**](WebVerificationsApi.md#getWebVerificationsByRegistrationId) | **POST** /api/web-verifications/by-registrationid | Retrieves secure link to web verification page searching by the Registration Id.



## getWebVerificationsByReferenceId

> CredasApiModelsWebVerificationsGetWebVerificationsResponse getWebVerificationsByReferenceId(apikey, opts)

Retrieves secure links to web verification pages searching by the Reference Id.

It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.WebVerificationsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest': new CredasApi.CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest() // CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest | 
};
apiInstance.getWebVerificationsByReferenceId(apikey, opts, (error, data, response) => {
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
 **credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest** | [**CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest**](CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest.md)|  | [optional] 

### Return type

[**CredasApiModelsWebVerificationsGetWebVerificationsResponse**](CredasApiModelsWebVerificationsGetWebVerificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## getWebVerificationsByRegistrationId

> CredasApiModelsWebVerificationsGetWebVerificationsResponse getWebVerificationsByRegistrationId(apikey, opts)

Retrieves secure link to web verification page searching by the Registration Id.

It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.WebVerificationsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest': new CredasApi.CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest() // CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest | 
};
apiInstance.getWebVerificationsByRegistrationId(apikey, opts, (error, data, response) => {
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
 **credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest** | [**CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest**](CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest.md)|  | [optional] 

### Return type

[**CredasApiModelsWebVerificationsGetWebVerificationsResponse**](CredasApiModelsWebVerificationsGetWebVerificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

