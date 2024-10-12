# Gateway.ProfileApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsProfileOnSharePost**](ProfileApi.md#v05PatientsProfileOnSharePost) | **POST** /v0.5/patients/profile/on-share | Response to patient&#39;s share profile request
[**v05PatientsProfileSharePost**](ProfileApi.md#v05PatientsProfileSharePost) | **POST** /v0.5/patients/profile/share | Share patient profile details



## v05PatientsProfileOnSharePost

> v05PatientsProfileOnSharePost(authorization, X_CM_ID, shareProfileResult)

Response to patient&#39;s share profile request

Result of patient share profile request at HIP end. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.ProfileApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let shareProfileResult = new Gateway.ShareProfileResult(); // ShareProfileResult | 
apiInstance.v05PatientsProfileOnSharePost(authorization, X_CM_ID, shareProfileResult, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **shareProfileResult** | [**ShareProfileResult**](ShareProfileResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05PatientsProfileSharePost

> v05PatientsProfileSharePost(authorization, X_HIP_ID, shareProfileRequest)

Share patient profile details

Request for sharing patient&#39;s profile details to HIP 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.ProfileApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let shareProfileRequest = new Gateway.ShareProfileRequest(); // ShareProfileRequest | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **shareProfileRequest** | [**ShareProfileRequest**](ShareProfileRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

