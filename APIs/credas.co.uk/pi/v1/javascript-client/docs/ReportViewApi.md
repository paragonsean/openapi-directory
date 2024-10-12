# CredasApi.ReportViewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReportViewByReferenceId**](ReportViewApi.md#getReportViewByReferenceId) | **POST** /api/report-view/by-referenceid | Retrieves secure links to registration details pages searching by the Reference Id.
[**getReportViewByRegistrationId**](ReportViewApi.md#getReportViewByRegistrationId) | **POST** /api/report-view/by-registrationid | Retrieves secure link to registration details page searching by the Registration Id.



## getReportViewByReferenceId

> CredasApiModelsReportViewGetReportViewResponse getReportViewByReferenceId(apikey, opts)

Retrieves secure links to registration details pages searching by the Reference Id.

It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ReportViewApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsReportViewGetReportViewByReferenceIdRequest': new CredasApi.CredasApiModelsReportViewGetReportViewByReferenceIdRequest() // CredasApiModelsReportViewGetReportViewByReferenceIdRequest | Request object
};
apiInstance.getReportViewByReferenceId(apikey, opts, (error, data, response) => {
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
 **credasApiModelsReportViewGetReportViewByReferenceIdRequest** | [**CredasApiModelsReportViewGetReportViewByReferenceIdRequest**](CredasApiModelsReportViewGetReportViewByReferenceIdRequest.md)| Request object | [optional] 

### Return type

[**CredasApiModelsReportViewGetReportViewResponse**](CredasApiModelsReportViewGetReportViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## getReportViewByRegistrationId

> CredasApiModelsReportViewGetReportViewResponse getReportViewByRegistrationId(apikey, opts)

Retrieves secure link to registration details page searching by the Registration Id.

It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.ReportViewApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsReportViewGetReportViewByRegistrationIdRequest': new CredasApi.CredasApiModelsReportViewGetReportViewByRegistrationIdRequest() // CredasApiModelsReportViewGetReportViewByRegistrationIdRequest | Request object
};
apiInstance.getReportViewByRegistrationId(apikey, opts, (error, data, response) => {
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
 **credasApiModelsReportViewGetReportViewByRegistrationIdRequest** | [**CredasApiModelsReportViewGetReportViewByRegistrationIdRequest**](CredasApiModelsReportViewGetReportViewByRegistrationIdRequest.md)| Request object | [optional] 

### Return type

[**CredasApiModelsReportViewGetReportViewResponse**](CredasApiModelsReportViewGetReportViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

