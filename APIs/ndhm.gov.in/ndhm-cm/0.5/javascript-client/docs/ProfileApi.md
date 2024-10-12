# HealthDataConsentManager.ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsProfileOnSharePost**](ProfileApi.md#v05PatientsProfileOnSharePost) | **POST** /v0.5/patients/profile/on-share | Response to patient&#39;s share profile request



## v05PatientsProfileOnSharePost

> v05PatientsProfileOnSharePost(authorization, shareProfileResult)

Response to patient&#39;s share profile request

Result of patient share profile request at HIP end. 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ProfileApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let shareProfileResult = new HealthDataConsentManager.ShareProfileResult(); // ShareProfileResult | 
apiInstance.v05PatientsProfileOnSharePost(authorization, shareProfileResult, (error, data, response) => {
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
 **shareProfileResult** | [**ShareProfileResult**](ShareProfileResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

