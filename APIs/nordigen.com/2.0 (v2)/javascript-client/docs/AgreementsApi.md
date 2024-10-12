# NordigenAccountInformationServicesApi.AgreementsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptEUA**](AgreementsApi.md#acceptEUA) | **PUT** /api/v2/agreements/enduser/{id}/accept/ | 
[**createEUAV2**](AgreementsApi.md#createEUAV2) | **POST** /api/v2/agreements/enduser/ | 
[**deleteEUAByIdV2**](AgreementsApi.md#deleteEUAByIdV2) | **DELETE** /api/v2/agreements/enduser/{id}/ | 
[**retrieveAllEUAsForAnEndUserV2**](AgreementsApi.md#retrieveAllEUAsForAnEndUserV2) | **GET** /api/v2/agreements/enduser/ | 
[**retrieveEUAByIdV2**](AgreementsApi.md#retrieveEUAByIdV2) | **GET** /api/v2/agreements/enduser/{id}/ | 



## acceptEUA

> EndUserAgreement acceptEUA(id, enduserAcceptanceDetailsRequest)



Accept an end-user agreement via the API

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AgreementsApi();
let id = "id_example"; // String | A UUID string identifying this end user agreement.
let enduserAcceptanceDetailsRequest = new NordigenAccountInformationServicesApi.EnduserAcceptanceDetailsRequest(); // EnduserAcceptanceDetailsRequest | 
apiInstance.acceptEUA(id, enduserAcceptanceDetailsRequest, (error, data, response) => {
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
 **id** | **String**| A UUID string identifying this end user agreement. | 
 **enduserAcceptanceDetailsRequest** | [**EnduserAcceptanceDetailsRequest**](EnduserAcceptanceDetailsRequest.md)|  | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## createEUAV2

> EndUserAgreement createEUAV2(endUserAgreementRequest)



API endpoints related to end-user agreements.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AgreementsApi();
let endUserAgreementRequest = new NordigenAccountInformationServicesApi.EndUserAgreementRequest(); // EndUserAgreementRequest | 
apiInstance.createEUAV2(endUserAgreementRequest, (error, data, response) => {
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
 **endUserAgreementRequest** | [**EndUserAgreementRequest**](EndUserAgreementRequest.md)|  | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## deleteEUAByIdV2

> deleteEUAByIdV2(id)



Delete an end user agreement

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AgreementsApi();
let id = "id_example"; // String | A UUID string identifying this end user agreement.
apiInstance.deleteEUAByIdV2(id, (error, data, response) => {
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
 **id** | **String**| A UUID string identifying this end user agreement. | 

### Return type

null (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAllEUAsForAnEndUserV2

> PaginatedEndUserAgreementList retrieveAllEUAsForAnEndUserV2(opts)



API endpoints related to end-user agreements.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AgreementsApi();
let opts = {
  'limit': 100, // Number | Number of results to return per page.
  'offset': 1 // Number | The initial index from which to return the results.
};
apiInstance.retrieveAllEUAsForAnEndUserV2(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **Number**| The initial index from which to return the results. | [optional] [default to 1]

### Return type

[**PaginatedEndUserAgreementList**](PaginatedEndUserAgreementList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveEUAByIdV2

> EndUserAgreement retrieveEUAByIdV2(id)



Retrieve end user agreement by ID

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AgreementsApi();
let id = "id_example"; // String | A UUID string identifying this end user agreement.
apiInstance.retrieveEUAByIdV2(id, (error, data, response) => {
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
 **id** | **String**| A UUID string identifying this end user agreement. | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

