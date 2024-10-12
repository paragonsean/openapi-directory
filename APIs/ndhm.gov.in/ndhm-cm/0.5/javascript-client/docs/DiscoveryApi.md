# HealthDataConsentManager.DiscoveryApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05CareContextsOnDiscoverPost**](DiscoveryApi.md#v05CareContextsOnDiscoverPost) | **POST** /v0.5/care-contexts/on-discover | Response to patient&#39;s account discovery request



## v05CareContextsOnDiscoverPost

> v05CareContextsOnDiscoverPost(authorization, patientDiscoveryResult)

Response to patient&#39;s account discovery request

Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.DiscoveryApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientDiscoveryResult = new HealthDataConsentManager.PatientDiscoveryResult(); // PatientDiscoveryResult | 
apiInstance.v05CareContextsOnDiscoverPost(authorization, patientDiscoveryResult, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **patientDiscoveryResult** | [**PatientDiscoveryResult**](PatientDiscoveryResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

