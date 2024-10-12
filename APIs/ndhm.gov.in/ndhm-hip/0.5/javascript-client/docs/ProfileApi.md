# HealthRepositoryProviderSpecificationsForHip.ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsProfileSharePost**](ProfileApi.md#v05PatientsProfileSharePost) | **POST** /v0.5/patients/profile/share | Share patient profile details



## v05PatientsProfileSharePost

> v05PatientsProfileSharePost(authorization, X_HIP_ID, shareProfileRequest)

Share patient profile details

Request for sharing patient&#39;s profile details to HIP 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.ProfileApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let shareProfileRequest = new HealthRepositoryProviderSpecificationsForHip.ShareProfileRequest(); // ShareProfileRequest | 
apiInstance.v05PatientsProfileSharePost(authorization, X_HIP_ID, shareProfileRequest, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **shareProfileRequest** | [**ShareProfileRequest**](ShareProfileRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

