# NordigenAccountInformationServicesApi.TokenApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jWTObtain**](TokenApi.md#jWTObtain) | **POST** /api/v2/token/new/ | 
[**jWTRefresh**](TokenApi.md#jWTRefresh) | **POST** /api/v2/token/refresh/ | 



## jWTObtain

> SpectacularJWTObtain jWTObtain(jWTObtainPairRequest)



Obtain JWT pair

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.TokenApi();
let jWTObtainPairRequest = new NordigenAccountInformationServicesApi.JWTObtainPairRequest(); // JWTObtainPairRequest | 
apiInstance.jWTObtain(jWTObtainPairRequest, (error, data, response) => {
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
 **jWTObtainPairRequest** | [**JWTObtainPairRequest**](JWTObtainPairRequest.md)|  | 

### Return type

[**SpectacularJWTObtain**](SpectacularJWTObtain.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## jWTRefresh

> SpectacularJWTRefresh jWTRefresh(jWTRefreshRequest)



Refresh access token

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.TokenApi();
let jWTRefreshRequest = new NordigenAccountInformationServicesApi.JWTRefreshRequest(); // JWTRefreshRequest | 
apiInstance.jWTRefresh(jWTRefreshRequest, (error, data, response) => {
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
 **jWTRefreshRequest** | [**JWTRefreshRequest**](JWTRefreshRequest.md)|  | 

### Return type

[**SpectacularJWTRefresh**](SpectacularJWTRefresh.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

