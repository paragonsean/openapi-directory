# ImporterExporterDetailsApi.APIsApi

All URIs are relative to *https://apisetu.gov.in/dgft*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importerExporterCodeVerificationAPI**](APIsApi.md#importerExporterCodeVerificationAPI) | **GET** /v1/iec/{iec} | Importer-Exporter Code (IEC) Verification API.



## importerExporterCodeVerificationAPI

> ImporterExporterCodeVerificationAPI200Response importerExporterCodeVerificationAPI(iec)

Importer-Exporter Code (IEC) Verification API.

Description of Importer-Exporter Code (IEC) Verification API.

### Example

```javascript
import ImporterExporterDetailsApi from 'importer_exporter_details_api';
let defaultClient = ImporterExporterDetailsApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImporterExporterDetailsApi.APIsApi();
let iec = "iec_example"; // String | Importer-Exporter code
apiInstance.importerExporterCodeVerificationAPI(iec, (error, data, response) => {
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
 **iec** | **String**| Importer-Exporter code | 

### Return type

[**ImporterExporterCodeVerificationAPI200Response**](ImporterExporterCodeVerificationAPI200Response.md)

### Authorization

[clientId](../README.md#clientId), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

